#!/usr/bin/env python3
"""
Image generator for YourBrand LinkedIn posts.

Two modes, chosen per-post via front-matter:
  - card  : a branded quote/insight card (Pillow-free, matplotlib) for fact/quote posts
  - chart : a branded matplotlib chart for data-driven posts

Brand palette:
  Primary Blue #4F46E5 · Coral Orange #F59E0B · Charcoal #111827
  Purple #7C3AED · Yellow #FDE68A
"""
import os
import textwrap
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.image as mpimg

BLUE = "#4F46E5"
CORAL = "#F59E0B"
CHARCOAL = "#111827"
PURPLE = "#7C3AED"
YELLOW = "#FDE68A"
WHITE = "#FFFFFF"

PALETTE = {"blue": BLUE, "coral": CORAL, "charcoal": CHARCOAL,
           "purple": PURPLE, "yellow": YELLOW, "white": WHITE}

LOGO_PATH = os.path.join(os.path.dirname(__file__), "assets", "logo.png")
HANDLE = "YourBrand"
CTA = "Book a call · yourdomain.com/book"


def _color(name, default):
    if not name:
        return default
    return PALETTE.get(str(name).lower(), name)  # accept palette name or raw hex


def _place_logo_or_wordmark(fig, ax, y_center):
    """Logo image if assets/logo.png exists, else a text wordmark."""
    if os.path.exists(LOGO_PATH):
        try:
            img = mpimg.imread(LOGO_PATH)
            h, w = img.shape[0], img.shape[1]
            ratio = w / h
            box_w = 0.46
            box_h = box_w / ratio
            ax_logo = fig.add_axes([0.5 - box_w / 2, y_center - box_h / 2, box_w, box_h])
            ax_logo.imshow(img)
            ax_logo.axis("off")
            return
        except Exception:
            pass
    ax.text(0.5, y_center, HANDLE, ha="center", va="center",
            color=BLUE, fontsize=34, fontweight="bold", zorder=6)


def generate_card(headline, out_path, bg=YELLOW, accent=CORAL, panel=WHITE):
    bg = _color(bg, YELLOW)
    accent = _color(accent, CORAL)
    panel = _color(panel, WHITE)

    fig = plt.figure(figsize=(12, 12), dpi=100)
    fig.patch.set_facecolor(bg)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # Neo-comic: hard offset shadow + bordered panel
    ax.add_patch(Rectangle((0.11, 0.07), 0.80, 0.80, facecolor=CHARCOAL, zorder=1))
    ax.add_patch(Rectangle((0.09, 0.09), 0.80, 0.80, facecolor=panel,
                           edgecolor=CHARCOAL, linewidth=9, zorder=2))
    # left accent stripe inside panel
    ax.add_patch(Rectangle((0.09, 0.09), 0.05, 0.80, facecolor=accent,
                           edgecolor=CHARCOAL, linewidth=9, zorder=3))

    # logo / wordmark near top of panel
    _place_logo_or_wordmark(fig, ax, y_center=0.78)

    # headline (wrap kept narrow so lines never exceed the panel width)
    wrapped = "\n".join(textwrap.wrap(headline, width=16))
    fs = 56 if len(headline) <= 45 else (46 if len(headline) <= 75 else 38)
    ax.text(0.515, 0.47, wrapped, ha="center", va="center",
            color=CHARCOAL, fontsize=fs, fontweight="bold", zorder=5)

    # CTA footer
    ax.text(0.515, 0.155, CTA, ha="center", va="center",
            color=CHARCOAL, fontsize=18, fontweight="bold", zorder=5)

    fig.savefig(out_path, facecolor=bg)
    plt.close(fig)
    return out_path


def generate_chart(cfg, out_path):
    labels = cfg["labels"]
    values = cfg["values"]
    hi = cfg.get("highlight_index")
    colors = [CORAL if (hi is not None and i == hi) else BLUE for i in range(len(values))]

    fig, ax = plt.subplots(figsize=(12, 12), dpi=100)
    fig.patch.set_facecolor(WHITE)
    ax.set_facecolor(WHITE)

    bars = ax.bar(labels, values, color=colors, edgecolor=CHARCOAL, linewidth=3,
                  width=0.62, zorder=3)
    if cfg.get("title"):
        title = cfg["title"]
        wrapped = "\n".join(textwrap.wrap(title, width=30))
        tfs = 32 if len(title) <= 42 else 26
        ax.set_title(wrapped, fontsize=tfs, fontweight="bold", color=CHARCOAL, pad=26)
    if cfg.get("ylabel"):
        ax.set_ylabel(cfg["ylabel"], fontsize=22, color=CHARCOAL, fontweight="bold")

    for b, v in zip(bars, values):
        ax.text(b.get_x() + b.get_width() / 2, v, f"{v}", ha="center", va="bottom",
                fontsize=24, fontweight="bold", color=CHARCOAL)

    ax.tick_params(labelsize=20, colors=CHARCOAL, length=0)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_linewidth(3)
        ax.spines[s].set_color(CHARCOAL)
    ax.margins(y=0.18)

    if cfg.get("illustrative", True):
        ax.text(0.985, 0.96, "Illustrative example", transform=ax.transAxes,
                ha="right", va="top", fontsize=15, color=CORAL, fontweight="bold")
    fig.text(0.98, 0.025, f"{HANDLE} · yourdomain.com/book", ha="right",
             color=BLUE, fontsize=15, fontweight="bold")

    fig.tight_layout(rect=[0.02, 0.05, 0.98, 0.98])
    fig.savefig(out_path, facecolor=WHITE)
    plt.close(fig)
    return out_path


def build_image(meta, out_path):
    """Dispatch on meta['image']. Returns path or None."""
    kind = (meta.get("image") or "none").lower()
    if kind == "card":
        return generate_card(meta.get("headline", ""), out_path,
                             bg=meta.get("bg"), accent=meta.get("accent"))
    if kind == "chart":
        return generate_chart(meta, out_path)
    if kind == "custom":
        f = meta.get("file")
        return f if f and os.path.exists(f) else None
    return None


if __name__ == "__main__":
    # quick local smoke test
    generate_card("Discounts aren't growth. They're margin you gave away on schedule.",
                  "sample_card.png", bg="yellow", accent="coral")
    generate_chart({"title": "Blanket discount vs discount-over-AOV",
                    "labels": ["Blanket monthly", "Discount over AOV"],
                    "values": [78, 94], "ylabel": "Margin retained (%)",
                    "highlight_index": 1, "illustrative": True},
                   "sample_chart.png")
    print("wrote sample_card.png and sample_chart.png")
