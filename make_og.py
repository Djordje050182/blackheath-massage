#!/usr/bin/env python3
"""Generate a 1200x630 branded og-image.jpg matching the site palette."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630

# Palette (from index.html :root)
FOREST   = (15, 24, 19)
FOREST_2 = (44, 66, 52)
SANDSTONE_SOFT = (217, 171, 120)
PAPER    = (244, 243, 234)
SAGE     = (158, 176, 148)

# --- background: radial-ish gradient forest, brighter top-right (mirrors hero) ---
img = Image.new("RGB", (W, H), FOREST)
px = img.load()
cx, cy = W * 0.72, H * 0.18          # light origin top-right, like the hero
maxd = ((W) ** 2 + (H) ** 2) ** 0.5
for y in range(H):
    for x in range(W):
        d = (((x - cx) ** 2 + (y - cy) ** 2) ** 0.5) / maxd
        d = min(1.0, d * 1.18)
        # blend FOREST_2 (near light) -> FOREST (far)
        r = int(FOREST_2[0] + (FOREST[0] - FOREST_2[0]) * d)
        g = int(FOREST_2[1] + (FOREST[1] - FOREST_2[1]) * d)
        b = int(FOREST_2[2] + (FOREST[2] - FOREST_2[2]) * d)
        px[x, y] = (r, g, b)

draw = ImageDraw.Draw(img)

def font(path, size):
    return ImageFont.truetype(path, size)

BASKERVILLE = "/System/Library/Fonts/Supplemental/Baskerville.ttc"
BASK_ITAL   = "/System/Library/Fonts/Supplemental/Baskerville.ttc"  # face index for italic
AVENIR      = "/System/Library/Fonts/Avenir Next.ttc"

f_eyebrow = font(AVENIR, 24)
f_brand   = font(AVENIR, 30)
f_h1      = font(BASKERVILLE, 88)
f_h1i     = ImageFont.truetype(BASK_ITAL, 88, index=1)   # italic face
f_sub     = font(AVENIR, 30)

PAD = 84

def tracked(d, xy, text, fnt, fill, spacing=0):
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=fnt, fill=fill)
        w = d.textlength(ch, font=fnt)
        x += w + spacing
    return x

# --- top: leaf mark + brand ---
# simple leaf glyph drawn as two arcs
lx, ly = PAD, PAD
draw.line([(lx, ly+26),(lx+10, ly), (lx+20, ly+26)], fill=SANDSTONE_SOFT, width=3, joint="curve")
draw.line([(lx+10, ly), (lx+10, ly+30)], fill=SANDSTONE_SOFT, width=3)
draw.text((lx+34, ly+2), "Blackheath Massage Therapy", font=f_brand, fill=PAPER)

# --- eyebrow ---
ey = 250
tracked(draw, (PAD, ey), "MOBILE MASSAGE · BLUE MOUNTAINS, NSW", f_eyebrow, SANDSTONE_SOFT, spacing=4)

# --- headline (two lines, second italic sandstone) ---
draw.text((PAD, ey+44), "You find the place.", font=f_h1, fill=PAPER)
draw.text((PAD, ey+44+96), "I'll bring the table.", font=f_h1i, fill=SANDSTONE_SOFT)

# --- sub line ---
draw.text((PAD, ey+44+96+118), "Qualified, hands-on massage that comes to you.",
          font=f_sub, fill=(215, 216, 204))

# --- thin sandstone rule bottom-left ---
draw.rectangle([PAD, H-70, PAD+70, H-67], fill=SANDSTONE_SOFT)

img.save("og-image.jpg", "JPEG", quality=88, optimize=True)
print("wrote og-image.jpg", img.size)
