import argparse
from sys import stdout
from math import sin, cos, radians

from PIL import Image, ImageDraw, ImageFont

DESCRIPTION = 'Generate map of hexes (format is PNG)'


def fill_argparser(parser):
    parser.description = DESCRIPTION
    parser.add_argument(
        '-o', '--output', type=argparse.FileType('wb'), default=stdout.buffer,
        help="ignore for STDOUT"
    )
    parser.add_argument('-r', '--radius', type=int, default=12, help="radius in # of hexes")
    parser.add_argument('-s', '--hex-size', type=int, default=24, help="radius of one hex in pixels")


def map(output_stream, radius, hex_size):
    margin = hex_size
    img_size = 4 * radius * hex_size + 2 * margin
    img = Image.new(mode='1', size=(img_size, img_size), color=1)
    draw = ImageDraw.Draw(img)

    hex_width = 2*hex_size*cos(radians(30))
    for i in range(radius):
        for j in range(radius):
            x = i*hex_width - j*hex_width/2
            y = j * 1.5 * hex_size
            hex_vtx = [(img_size/2+x+hex_size*cos(r), img_size/2+y+hex_size*sin(r))
                       for a in range(30, 360, 60) for r in [radians(a)]]
            draw.polygon(hex_vtx, outline=0)
            hex_vtx = [(img_size/2+x+hex_size*cos(r), img_size/2-y+hex_size*sin(r))
                       for a in range(30, 360, 60) for r in [radians(a)]]
            draw.polygon(hex_vtx, outline=0)
            hex_vtx = [(img_size/2-x+hex_size*cos(r), img_size/2+y+hex_size*sin(r))
                       for a in range(30, 360, 60) for r in [radians(a)]]
            draw.polygon(hex_vtx, outline=0)
            hex_vtx = [(img_size/2-x+hex_size*cos(r), img_size/2-y+hex_size*sin(r))
                       for a in range(30, 360, 60) for r in [radians(a)]]
            draw.polygon(hex_vtx, outline=0)
            # lots of hexes are overlapping, but htis keeps the code simple

    img.save(output_stream, "PNG")


def main(args):
    map(args.output, args.radius, args.hex_size)
