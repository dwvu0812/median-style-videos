#!/usr/bin/env python3
"""Avatar + banner for 'The Maths Inside' — Median black style.
Pure black bg, white type, periwinkle/mint accents only."""
from PIL import Image, ImageDraw, ImageFont
import os

OUT = os.path.expanduser("~/workspace/median-style-videos/videos/03-gps/channel-branding")
os.makedirs(OUT, exist_ok=True)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (154, 154, 154)
PERIWINKLE = (126, 155, 255)
MINT = (111, 207, 151)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def center_text(draw, cx, y, text, font, fill):
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    draw.text((cx - w / 2 - bbox[0], y), text, font=font, fill=fill)
    return bbox[3] - bbox[1]


# ---------- Avatar: 800x800, giant white sigma on black ----------
av = Image.new("RGB", (800, 800), BLACK)
d = ImageDraw.Draw(av)
sig = ImageFont.truetype(BOLD, 520)
bbox = d.textbbox((0, 0), "\u2211", font=sig)
w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
d.text(((800 - w) / 2 - bbox[0], (800 - h) / 2 - bbox[1] - 20),
       "\u2211", font=sig, fill=WHITE)
# small mint dot accent, bottom-right of the sigma
d.ellipse([618, 618, 650, 650], fill=MINT)
av.save(f"{OUT}/avatar.png")
print("avatar.png", av.size)

# ---------- Banner: 2560x1440, safe area 1546x423 centred ----------
# safe area: x 507..2053, y 508..932
bn = Image.new("RGB", (2560, 1440), BLACK)
d = ImageDraw.Draw(bn)
cx = 1280

# small periwinkle sigma above the title
sig_small = ImageFont.truetype(BOLD, 96)
center_text(d, cx, 540, "\u2211", sig_small, PERIWINKLE)

title_font = ImageFont.truetype(BOLD, 132)
center_text(d, cx, 668, "The Maths Inside", title_font, WHITE)

tag_font = ImageFont.truetype(REG, 54)
center_text(d, cx, 830, "The maths inside AI, made visible.", tag_font, GREY)

bn.save(f"{OUT}/banner.png")
print("banner.png", bn.size)
