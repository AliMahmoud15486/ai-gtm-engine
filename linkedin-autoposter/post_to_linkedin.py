#!/usr/bin/env python3
"""
Autonomous LinkedIn poster for YourBrand.

Each run: take the next post from queue/ (alphabetical = publish order), generate its
image if the front-matter asks for one (card or chart), publish to Ali's profile via the
official UGC Posts API (w_member_social), then move the file to posted/.

Post files may start with a YAML front-matter block, e.g.:
    ---
    image: card            # card | chart | custom | none
    headline: "Short punchy line for the card"
    bg: yellow             # palette name or hex
    accent: coral
    ---
    The actual post body goes here...

If the image step fails for any reason, the post still goes out as text-only.

Env (GitHub Actions secrets):
  LINKEDIN_ACCESS_TOKEN   (required)  scopes: openid profile w_member_social
  LINKEDIN_AUTHOR_URN     (optional)  e.g. "urn:li:person:XXXX" (else resolved via /userinfo)
"""
import os
import sys
import glob
import shutil
import datetime
import requests
import yaml

import media_gen

API_UGC = "https://api.linkedin.com/v2/ugcPosts"
API_USERINFO = "https://api.linkedin.com/v2/userinfo"
API_REGISTER = "https://api.linkedin.com/v2/assets?action=registerUpload"
QUEUE_DIR = "queue"
POSTED_DIR = "posted"
TMP_IMAGE = "generated_post_image.png"


def fail(msg):
    print(f"::error::{msg}")
    sys.exit(1)


def warn(msg):
    print(f"::warning::{msg}")


def _headers(token):
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0",
    }


def get_author_urn(token):
    urn = os.environ.get("LINKEDIN_AUTHOR_URN", "").strip()
    if urn:
        return urn
    r = requests.get(API_USERINFO, headers={"Authorization": f"Bearer {token}"}, timeout=30)
    if r.status_code != 200:
        fail(f"Could not resolve author via /userinfo ({r.status_code}): {r.text}. "
             f"Add 'openid'+'profile' scopes to the token, or set LINKEDIN_AUTHOR_URN.")
    sub = r.json().get("sub")
    if not sub:
        fail(f"/userinfo returned no 'sub': {r.text}")
    return f"urn:li:person:{sub}"


def parse_front_matter(raw):
    if raw.startswith("---"):
        parts = raw.split("---", 2)
        if len(parts) >= 3:
            try:
                meta = yaml.safe_load(parts[1]) or {}
            except yaml.YAMLError as e:
                warn(f"front-matter parse failed ({e}); treating whole file as body.")
                return {}, raw.strip()
            return meta, parts[2].strip()
    return {}, raw.strip()


def next_post():
    files = sorted(glob.glob(os.path.join(QUEUE_DIR, "*.md")))
    return files[0] if files else None


def upload_image(token, author, path):
    """Register + upload an image; return its asset URN (raises on failure)."""
    body = {"registerUploadRequest": {
        "recipes": ["urn:li:digitalmediaRecipe:feedshare-image"],
        "owner": author,
        "serviceRelationships": [
            {"relationshipType": "OWNER", "identifier": "urn:li:userGeneratedContent"}
        ]}}
    r = requests.post(API_REGISTER, headers=_headers(token), json=body, timeout=30)
    if r.status_code not in (200, 201):
        raise RuntimeError(f"registerUpload {r.status_code}: {r.text}")
    v = r.json()["value"]
    asset = v["asset"]
    upload_url = (v["uploadMechanism"]
                  ["com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest"]["uploadUrl"])
    with open(path, "rb") as f:
        up = requests.put(upload_url, headers={"Authorization": f"Bearer {token}"},
                          data=f.read(), timeout=60)
    if up.status_code not in (200, 201):
        raise RuntimeError(f"binary upload {up.status_code}: {up.text}")
    return asset


def publish(token, author, text, asset=None):
    share = {"shareCommentary": {"text": text}, "shareMediaCategory": "NONE"}
    if asset:
        share["shareMediaCategory"] = "IMAGE"
        share["media"] = [{"status": "READY", "media": asset}]
    body = {
        "author": author,
        "lifecycleState": "PUBLISHED",
        "specificContent": {"com.linkedin.ugc.ShareContent": share},
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"},
    }
    r = requests.post(API_UGC, headers=_headers(token), json=body, timeout=30)
    if r.status_code not in (200, 201):
        fail(f"LinkedIn post failed ({r.status_code}): {r.text}")
    return r.headers.get("x-restli-id", "ok")


def main():
    token = os.environ.get("LINKEDIN_ACCESS_TOKEN", "").strip()
    if not token:
        fail("LINKEDIN_ACCESS_TOKEN is not set.")

    path = next_post()
    if not path:
        print("Queue is empty — nothing to post. Add files to queue/ to schedule more.")
        return

    with open(path, encoding="utf-8") as f:
        meta, body = parse_front_matter(f.read())
    if not body:
        fail(f"{path} has no post body.")

    author = get_author_urn(token)

    # Image is best-effort: never let it block the post.
    asset = None
    if (meta.get("image") or "none").lower() != "none":
        try:
            img_path = media_gen.build_image(meta, TMP_IMAGE)
            if img_path:
                asset = upload_image(token, author, img_path)
                print(f"Attached {meta.get('image')} image.")
        except Exception as e:
            warn(f"image step failed, posting text-only: {e}")
            asset = None

    post_id = publish(token, author, body, asset)

    os.makedirs(POSTED_DIR, exist_ok=True)
    stamp = datetime.datetime.utcnow().strftime("%Y%m%d")
    dest = os.path.join(POSTED_DIR, f"{stamp}-{os.path.basename(path)}")
    shutil.move(path, dest)
    if os.path.exists(TMP_IMAGE):
        os.remove(TMP_IMAGE)
    print(f"Posted {os.path.basename(path)} (id: {post_id}); moved to {dest}.")


if __name__ == "__main__":
    main()
