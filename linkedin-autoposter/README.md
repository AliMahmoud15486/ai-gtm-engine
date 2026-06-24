# Autonomous LinkedIn Poster

Posts content to **your** LinkedIn profile automatically, on a schedule, via GitHub Actions.
No always-on machine needed. After a one-time setup it runs itself: it publishes the next
file from `queue/`, generates a branded image (card or chart) if the post asks for one,
moves the file to `posted/`, and commits the change back.

```
queue/      → posts waiting to publish (alphabetical order = publish order)
posted/     → posts already published (audit trail)
post_to_linkedin.py     → the poster (LinkedIn UGC API, w_member_social)
media_gen.py            → branded card + chart image generator (edit brand constants up top)
.github/workflows/linkedin-poster.yml → the schedule (Mon/Wed/Fri 08:00 UTC by default)
```

## Post format
Each post is one `.md` file in `queue/`, optionally starting with YAML front-matter:

```
---
image: card            # card | chart | custom | none
headline: "Short punchy line for the card"
bg: yellow             # palette name or hex
accent: coral
---
Your post body goes here...
```

For a chart, instead use:
```
---
image: chart
title: "Your chart title"
labels: ["Before", "After"]
values: [78, 94]
ylabel: "Margin retained (%)"
highlight_index: 1
illustrative: true     # labels the chart "Illustrative example" if it isn't real data
---
Body...
```

## One-time setup
1. **Create a LinkedIn app** at https://www.linkedin.com/developers/apps (requires linking a LinkedIn Page).
   - Products → add **"Share on LinkedIn"** (`w_member_social`) and **"Sign In with LinkedIn using OpenID Connect"** (`openid`, `profile`).
2. **Generate an access token** (Auth tab → OAuth token generator) with scopes `openid profile w_member_social`. Copy it. (Tokens last ~60 days; regenerate + update the secret when it expires.)
3. **Use this folder as its own repo** (so `.github/workflows/` is at the repo root). Public or private.
4. **Add the token as a secret:** repo → Settings → Secrets and variables → Actions → New secret `LINKEDIN_ACCESS_TOKEN`. (Optional `LINKEDIN_AUTHOR_URN` = `urn:li:person:XXXX` if you skip the openid/profile scopes.)
5. **Test:** Actions tab → enable workflows → **LinkedIn Autoposter** → **Run workflow**. It publishes `queue/01-...` and moves it to `posted/`.

## Make it yours
- **Brand:** edit the constants at the top of `media_gen.py` (`HANDLE`, `CTA`, the color palette). Drop your logo at `assets/logo.png` (else a text wordmark is used).
- **Schedule:** edit the `cron` in the workflow (UTC).
- **Content:** add `.md` files to `queue/`. Filename order = publish order. An empty queue just no-ops.

## Security
- The token lives only in GitHub's encrypted secret store — never in code or commits.
- Posts only to the authenticated member's own profile via the official `w_member_social` scope. No password sharing, no scraping.
