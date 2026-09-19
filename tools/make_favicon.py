"""Generates the site's favicon set: the MML monogram set in Fraunces (the heading
face) on a terracotta rounded square, matching the palette in
_sass/theme/_default_light.scss.

Writes assets/favicon.svg and images/favicon.svg (letters as vector paths, so no
font needs to be installed to render them), images/favicon-{32,192,512}.png,
images/apple-touch-icon-180x180.png and images/favicon.ico.

Run from the repo root:
    pip install fonttools pillow
    python tools/make_favicon.py
Change TEXT / colours below and re-run to regenerate everything.
"""
import io, os, urllib.request
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
from PIL import Image, ImageDraw, ImageFont

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEXT = "MML"
BG = (194, 87, 26)          # --accent  #c2571a
FG = (251, 248, 243)        # --bg      #fbf8f3
BOX = 64.0                  # SVG viewBox side
TARGET_W = 50.0             # width the word occupies inside the box
RADIUS = 14                 # corner radius in box units
TRACKING = 0.02             # letter-spacing, fraction of the em

def fetch_fraunces():
    """Fraunces SemiBold as a TTF, via the Google Fonts CSS endpoint (an old UA gets a woff)."""
    css_url = "https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600"
    req = urllib.request.Request(css_url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:20.0) Gecko/20100101 Firefox/20.0"})
    css = urllib.request.urlopen(req).read().decode()
    url = css.split("url(")[1].split(")")[0]
    data = urllib.request.urlopen(url).read()
    font = TTFont(io.BytesIO(data))
    font.flavor = None           # woff -> plain ttf
    buf = io.BytesIO(); font.save(buf); buf.seek(0)
    return TTFont(buf), buf.getvalue()

def hexc(rgb): return "#%02x%02x%02x" % rgb

def main():
    font, ttf_bytes = fetch_fraunces()
    upm = font["head"].unitsPerEm
    cmap = font.getBestCmap(); glyphs = font.getGlyphSet(); hmtx = font["hmtx"]
    names = [cmap[ord(c)] for c in TEXT]

    # lay the letters out with tracking, measure the word
    x, segments = 0, []
    for n in names:
        segments.append((n, x)); x += hmtx[n][0] + TRACKING * upm
    bp = BoundsPen(glyphs)
    for n, dx in segments:
        glyphs[n].draw(TransformPen(bp, (1, 0, 0, 1, dx, 0)))
    xmin, ymin, xmax, ymax = bp.bounds

    # fit and centre it in the box
    scale = TARGET_W / (xmax - xmin)
    word_h = (ymax - ymin) * scale
    ox = (BOX - (xmax - xmin) * scale) / 2 - xmin * scale
    oy = (BOX + word_h) / 2 + ymin * scale

    pen = SVGPathPen(glyphs, ntos=lambda v: ("%.2f" % v).rstrip("0").rstrip("."))
    for n, dx in segments:
        glyphs[n].draw(TransformPen(pen, (scale, 0, 0, -scale, ox + dx * scale, oy)))
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">\n'
           '  <rect width="64" height="64" rx="%d" fill="%s"/>\n'
           '  <path d="%s" fill="%s"/>\n</svg>\n' % (RADIUS, hexc(BG), pen.getCommands(), hexc(FG)))
    for p in ("assets/favicon.svg", "images/favicon.svg"):
        with open(os.path.join(REPO, p), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(svg)

    def render(size):
        S = size * 4                                   # supersample, then shrink
        img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
        d = ImageDraw.Draw(img)
        d.rounded_rectangle([0, 0, S - 1, S - 1], radius=int(S * RADIUS / BOX), fill=BG + (255,))
        pil_font = ImageFont.truetype(io.BytesIO(ttf_bytes), int(S * scale * upm / BOX))
        asc = pil_font.getmetrics()[0]
        for i, (n, dx) in enumerate(segments):
            d.text((ox * S / BOX + dx * scale * S / BOX, oy * S / BOX - asc), TEXT[i], font=pil_font, fill=FG + (255,))
        return img.resize((size, size), Image.LANCZOS)

    for size, name in [(32, "images/favicon-32x32.png"), (192, "images/favicon-192x192.png"),
                       (512, "images/favicon-512x512.png"), (180, "images/apple-touch-icon-180x180.png")]:
        render(size).save(os.path.join(REPO, name), optimize=True)
    render(256).save(os.path.join(REPO, "images/favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
    print("favicon set written for", TEXT)

if __name__ == "__main__":
    main()
