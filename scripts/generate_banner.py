"""Generate the profile's original, self-contained animation. Requires Pillow.
All geometry and animation are authored here. Fonts use locally installed Noto Sans.
"""
from pathlib import Path
import math
from PIL import Image, ImageDraw, ImageFont, PngImagePlugin

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
ASSETS.mkdir(exist_ok=True)
REGULAR = '/usr/share/fonts/noto/NotoSans-Regular.ttf'
BOLD = '/usr/share/fonts/noto/NotoSans-Bold.ttf'
BG, INK, SOFT, AMBER, MINT, LINE = '#102B33', '#F4F5EF', '#B4C9CB', '#F3BC64', '#9DD5C7', '#49646A'
W, H = 1280, 400

def font(size, bold=False):
    return ImageFont.truetype(BOLD if bold else REGULAR, size)

def draw_frame(progress):
    image = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(image)
    d.text((52, 35), 'Ignacio Albarracín', font=font(58, True), fill=INK)
    d.text((55, 115), 'Applied AI & software engineering', font=font(28), fill=SOFT)
    d.text((55, 167), 'From idea to deployed product.', font=font(35, True), fill=AMBER)
    labels = ['Context', 'Agents', 'Review', 'Ship']
    points = [(85, 295), (455, 295), (825, 295), (1195, 295)]
    for i in range(3):
        x, y = points[i]
        x2, y2 = points[i + 1]
        d.line((x + 17, y, x2 - 17, y2), fill=LINE, width=2)
    for (x, y), label in zip(points, labels):
        d.ellipse((x-11, y-11, x+11, y+11), fill=BG, outline=MINT, width=3)
        box = d.textbbox((0, 0), label, font=font(23))
        d.text((x-(box[2]-box[0])/2, y+26), label, font=font(23), fill=INK)
    # A single packet crosses the workflow; every frame keeps the full copy visible.
    position = progress * 3
    index = min(2, int(position))
    local = position-index
    eased = (1-math.cos(local*math.pi))/2
    x = points[index][0] + (points[index+1][0]-points[index][0])*eased
    d.ellipse((x-7, 288, x+7, 302), fill=AMBER)
    return image

frames = [draw_frame(i/83) for i in range(84)]
metadata = PngImagePlugin.PngInfo()
metadata.add_text('Source', 'Original code-generated artwork: scripts/generate_banner.py. Fonts: Noto Sans, SIL Open Font License.')
frames[0].save(ASSETS/'profile-static.png', pnginfo=metadata, optimize=True)
frames[0].save(ASSETS/'profile.gif', save_all=True, append_images=frames[1:], duration=85,
               loop=0, optimize=True, comment=b'Original code-generated artwork; source: scripts/generate_banner.py; Noto Sans (OFL).')
print(f'Generated {W}x{H}, {len(frames)} frames; {(ASSETS/"profile.gif").stat().st_size:,} bytes')
