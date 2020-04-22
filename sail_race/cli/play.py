from ..draws import seed
from ..wind import Wind, WindIterator

NAME = 'play'
DESCRIPTION = 'Prepare game'


def fill_argparser(parser):
    parser.description = DESCRIPTION
    parser.add_argument('-s', '--seed', type=int, help="ignore for random seed (systime based)")
    parser.add_argument('-n', '--count', type=int, required=True)
    parser.add_argument('-i', '--initial-bearing', type=int)


def play(seed_value, count, initial_bearing):
    if (seed_value is not None):
        seed(seed_value)
    w = Wind()
    if initial_bearing is not None:
        w._bearing = initial_bearing
    print(f"[Start] { w }")
    wi = iter(w)
    for _ in range(count):
        next(wi)
        print(f"[{_+1:5}] { w }")
    wi.stop()


def main(args):
    play(args.seed, args.count, args.initial_bearing)
