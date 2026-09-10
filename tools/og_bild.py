"""Vorschaubild (Open Graph, 1200 x 630) und Favicons für den Schnelleinstieg OGD.

Setzt zusammen: Züriblau-Fläche, weisses Logo «Stadt Zürich / Open Data» (SVG,
gerendert mit PyMuPDF), OGD-Sticker, Titel und Untertitel in Helvetica Neue
(WOFF2 -> TTF mit fontTools), unten die vier Farben der Kachelskala «Brücke».
"""
import io
import sys

import fitz
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

REPO = __file__.replace("\\", "/").rsplit("/tools/", 1)[0] + "/"
SHARED = REPO + "shared/"
OUT = sys.argv[1] if len(sys.argv) > 1 else SHARED  # Zielordner, Standard: shared/

W, H = 1200, 630
BLUE = (0x0F, 0x05, 0xA0)
WHITE = (255, 255, 255)
MARGIN = 72


def font(file, size):
    tt = TTFont(SHARED + "fonts/" + file)
    tt.flavor = None
    buf = io.BytesIO()
    tt.save(buf)
    buf.seek(0)
    return ImageFont.truetype(buf, size)


def svg_to_image(path, height):
    # PyMuPDF wertet <style>-Klassen nicht aus: das Rechteck mit fill:none
    # würde schwarz, die weissen Pfade ebenfalls. Klassen darum als
    # Attribute ausschreiben.
    import re
    svg = open(path, encoding="utf-8").read()
    svg = re.sub(r"<style.*?</style>", "", svg, flags=re.S)
    svg = svg.replace('class="st0"', 'fill="none"').replace('class="st1"', 'fill="#FFFFFF"')
    doc = fitz.open(stream=svg.encode("utf-8"), filetype="svg")
    page = doc[0]
    zoom = height / page.rect.height
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=True)
    return Image.frombytes("RGBA", (pix.width, pix.height), pix.samples)


img = Image.new("RGB", (W, H), BLUE)
draw = ImageDraw.Draw(img)

# Logo oben links
logo = svg_to_image(SHARED + "logo_stzh_ssz_open_data_rgb_weiss_digital.svg", 120)
img.paste(logo, (MARGIN, MARGIN), logo)

# Sticker oben rechts
def load_sticker():
    # Die PNG-Datei hat aussen einen 1px-Rahmen in 25 % Schwarz — abschneiden.
    im = Image.open(SHARED + "OGD_STICKER_final_zueriblau_hintergrund_quadr_noFill.png").convert("RGBA")
    return im.crop((2, 2, im.width - 2, im.height - 2))


sticker = load_sticker().resize((190, 190), Image.LANCZOS)
img.paste(sticker, (W - MARGIN - 190 + 14, MARGIN - 34), sticker)

# Titel zweizeilig, Untertitel
heavy = font("HelveticaNeueLTW05_85Heavy.woff2", 76)
regular = font("HelveticaNeueLTW01_55Roman.woff2", 34)

title_lines = ["Schnelleinstieg", "Open Government Data"]
line_h = 84
sub = "Entdecken Sie, was mit offenen Daten der Stadt Zürich möglich ist."

bar_h = 14
sub_y = H - bar_h - MARGIN - 40
title_y = sub_y - 28 - line_h * len(title_lines)
for i, line in enumerate(title_lines):
    draw.text((MARGIN - 4, title_y + i * line_h), line, font=heavy, fill=WHITE)
draw.text((MARGIN, sub_y), sub, font=regular, fill=(0xEF, 0xF5, 0xFF))

# Kachelskala «Brücke» als Band am unteren Rand, Reihenfolge wie die Kacheln
scale = [((0x1A, 0x3A, 0x88), (0x25, 0x50, 0xA0)),
         ((0x28, 0x70, 0xB8), (0x35, 0x90, 0xCC)),
         ((0x2A, 0x8C, 0xB8), (0x3A, 0x9F, 0xCC)),
         ((0x4A, 0xB0, 0xD0), (0x5C, 0xC0, 0xDE))]
seg = W / len(scale)
for i, (a, b) in enumerate(scale):
    x0, x1 = round(i * seg), round((i + 1) * seg)
    for x in range(x0, x1):
        t = (x - x0) / max(1, x1 - x0 - 1)
        col = tuple(round(a[k] + (b[k] - a[k]) * t) for k in range(3))
        draw.line([(x, H - bar_h), (x, H)], fill=col)

img.save(OUT + "og-bild.png", optimize=True)

# Favicons aus dem Sticker (transparenter Grund)
full = load_sticker()
full.resize((180, 180), Image.LANCZOS).save(OUT + "apple-touch-icon.png", optimize=True)
full.resize((32, 32), Image.LANCZOS).save(OUT + "favicon-32.png", optimize=True)

print("ok")
