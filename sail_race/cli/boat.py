import argparse
from sys import stdout
from math import sin, cos, radians

from PIL import Image, ImageDraw, ImageFont

from .. import PointOfSail

# TODO: SHould replace this by SVG

NAME = 'boat'
DESCRIPTION = 'Generate boat token (format is PNG)'
RESX = 256
RESY = 256
RADIUS = 110
BOX_H = 160
BOX_W = 80
TEXT_DIST = RADIUS-30
TEXT_SZ = 7


def fill_argparser(parser):
    parser.description = DESCRIPTION
    parser.add_argument(
        '-o', '--output', type=argparse.FileType('wb'), default=stdout.buffer,
        help="ignore for STDOUT"
    )


def boat(output_stream):
    img = Image.new(mode='1', size=(RESX, RESY), color=1)
    draw = ImageDraw.Draw(img)

    hex_vtx = [(RESX/2+RADIUS*cos(r), RESY/2+RADIUS*sin(r))
               for a in range(0, 360, 60) for r in [radians(a)]]
    draw.polygon(hex_vtx, outline=0)
    for _ in range(3):
        draw.line([hex_vtx[_], hex_vtx[_+3]], fill=0)
    box_vtx = [RESX/2-BOX_W/2, RESY/2-BOX_H/2, RESX/2+BOX_W/2, RESY/2+BOX_H/2]
    draw.ellipse(box_vtx, fill=1)
    box_vtx = [RESX/2-BOX_W/2, RESY/2-BOX_H/2, RESX/2+BOX_W, RESY/2+BOX_H]
    draw.arc(box_vtx, 170, 250, fill=0)
    box_vtx = [RESX/2-BOX_W, RESY/2-BOX_H/2, RESX/2+BOX_W/2, RESY/2+BOX_H]
    draw.arc(box_vtx, -70, 10, fill=0)
    line_vtx = [RESX/2-BOX_W/2, RESY/2+0.4*BOX_H, RESX/2+BOX_W/2, RESY/2+0.4*BOX_H]
    draw.line(line_vtx, fill=0)

    font = ImageFont.truetype("Arial Black", size=TEXT_SZ*2)
    for pos in PointOfSail:
        a1 = 270-pos.bearing
        if pos.delta_speed is None:
            text = "STOP"
        else:
            text = f"{pos.delta_speed:+1}"
        y = RESY/2+TEXT_DIST*sin(radians(a1)) - TEXT_SZ
        x1 = RESX/2+TEXT_DIST*cos(radians(a1)) - TEXT_SZ*len(text)/2
        x2 = RESX/2-TEXT_DIST*cos(radians(a1)) - TEXT_SZ*len(text)/2
        draw.text([x1, y], text, color=0, font=font)
        if a1 % 180 != 90:
            draw.text([x2, y], text, color=0, font=font)

    img.save(output_stream, "PNG")


def main(args):
    boat(args.output)
