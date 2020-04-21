import argparse
from sys import stdout
from math import sin, cos, radians

from PIL import Image, ImageDraw, ImageFont

from .. import BoatBearing
from .boat import RESX as BOAT_RESX, RESY as BOAT_RESY, RADIUS

NAME = 'compass'
DESCRIPTION = 'Generate compas rose (format is PNG)'
RESX = BOAT_RESX+96
RESY = BOAT_RESY+96
TEXT_DIST = RADIUS+25
TEXT_SZ = 9


def fill_argparser(parser):
    parser.description = DESCRIPTION
    parser.add_argument(
        '-o', '--output', type=argparse.FileType('wb'), default=stdout.buffer,
        help="ignore for STDOUT"
    )


def compass(output_stream):
    img = Image.new(mode='1', size=(RESX, RESY), color=1)
    draw = ImageDraw.Draw(img)

    hex_vtx = [(RESX/2+RADIUS*cos(r), RESY/2+RADIUS*sin(r))
               for a in range(30, 360, 60) for r in [radians(a)]]
    draw.polygon(hex_vtx, outline=0)

    font = ImageFont.truetype("Arial Black", size=TEXT_SZ*2)
    small_font = ImageFont.truetype("Arial", size=round(TEXT_SZ*1.5))

    for brg in BoatBearing:
        a = radians(5-(brg.max+brg.min)/2)
        text = brg._name_
        y = RESY/2+TEXT_DIST*sin(a) - 2*TEXT_SZ
        x = RESX/2+TEXT_DIST*cos(a) - TEXT_SZ*len(text)/2
        draw.text([x, y], text, color=0, font=font)
        text = f"{(brg.min+360)%360} - {brg.max}"
        y = RESY/2+TEXT_DIST*sin(a) + TEXT_SZ/2
        x = RESX/2+TEXT_DIST*cos(a) - TEXT_SZ*len(text)*0.35
        draw.text([x, y], text, color=0, font=small_font)

    img.save(output_stream, "PNG")


def main(args):
    compass(args.output)
