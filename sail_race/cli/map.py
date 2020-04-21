import argparse
from sys import stdout
from math import sin, cos, radians, trunc
# from statistics import NormalDist  # need Python 3.8, use scipy instead
from scipy.stats import norm
from numpy.random.mtrand import RandomState

from PIL import Image, ImageDraw, ImageFont

# TODO: draw arrival line

NAME = 'map'
DESCRIPTION = 'Generate map of hexes (format is PNG)'


def fill_argparser(parser):
    parser.description = DESCRIPTION
    parser.add_argument(
        '-o', '--output', type=argparse.FileType('wb'), default=stdout.buffer,
        help="ignore for STDOUT"
    )
    parser.add_argument('-r', '--radius', type=int, default=12, help="radius in # of hexes")
    parser.add_argument('-S', '--hex-size', type=int, default=24, help="radius of one hex in pixels")
    parser.add_argument('-s', '--seed', type=int, help="ignore for random seed (systime based)")


def random_num(radius, randomizer, width):
    # res = randomizer.samples(1)[0]*width/radius
    res = randomizer['distri'].rvs(
        size=1,
        random_state=randomizer['random_state']
        )[0]*width/radius
    if res < 0:
        res = 0
    elif res >= width:
        res = width-1
    else:
        res = trunc(res)
    return res


def random_hex_in_sector(radius, randomizer):
    # There are:
    #  -> (n-1).n/2 hexes belonging only to the sector
    #  -> 2(n-1) hexes in common with the sibling sectors
    #  -> 1 hex in the center
    # (where n = radius)

    # Random distance from center
    dist = random_num(radius, randomizer, radius)
    shift = random_num(radius, randomizer, dist+1)
    return {'dist': dist, 'shift': shift}


def mark_hex(draw, font, img_size, hex, hex_size, mark, sector):
    x = 2*hex_size * cos(radians(30)) * hex['dist'] \
        - hex_size * cos(radians(30)) * hex['shift']
    y = 1.5*hex_size * hex['shift']
    a = radians(60 * (1-sector))
    xr = x*cos(a) - y*sin(a)
    yr = x*sin(a) + y*cos(a)
    draw.text([
        img_size/2+xr-0.3*hex_size,
        img_size/2+yr-0.7*hex_size
        ], mark, color=0, font=font)


def map(output_stream, radius, hex_size, seed):
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

    n_hexes = 3 * radius * radius - 3 * radius + 1
    # 6 . (n(n+1)/2 - 6n + 1 = 3n^2 - 3n - 1
    print(f"{n_hexes} hexes")

    # Create normal distribution
    # randomizer = NormalDist(mu=radius/2, sigma=radius/6, seed=seed)
    randomizer = {
        'distri': norm(loc=radius/2, scale=radius/6),
        'random_state': RandomState(seed=seed)
    }

    font = ImageFont.truetype("Arial Black", size=hex_size)

    # Start line is in lower sector (sector 0)
    # Choose 1 hex at random in sector
    hex_pos = random_hex_in_sector(radius, randomizer)
    print(f"Start: {hex_pos}")
    mark_hex(draw, font, img_size, hex_pos, hex_size, "#", 0)

    # Place buoys in sectors 1, 3, 5
    for buoy_num in range(1, 4):
        hex_pos = random_hex_in_sector(radius, randomizer)
        sector = 2*buoy_num-1
        print(f"Buoy #{buoy_num}: {hex_pos}")
        mark_hex(draw, font, img_size, hex_pos, hex_size, "O", sector)

    # Place random reefs in sectors 2, 4
    for sector in [2, 4]:
        num_reefs = random_num(radius, randomizer, radius)
        for _ in range(num_reefs):
            hex_pos = random_hex_in_sector(radius, randomizer)
            # TODO: should ignore positions of start line and buoys
            mark_hex(draw, font, img_size, hex_pos, hex_size, "*", sector)

    img.save(output_stream, "PNG")


def main(args):
    map(args.output, args.radius, args.hex_size, args.seed)
