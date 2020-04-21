from ..draws import seed
from ..wind import Wind, WindIterator

NAME = 'play'
DESCRIPTION = 'Prepare game'


def fill_argparser(parser):
    parser.description = DESCRIPTION
    parser.add_argument('-s', '--seed', type=int, help="ignore for random seed (systime based)")
    parser.add_argument('-n', '--count', type=int, required=True)


def play(seed_value, count):
    if (seed_value is not None):
        seed(seed_value)
    w = Wind()
    print(f"[Start] { w }")
    wi = iter(w)
    for _ in range(count):
        next(wi)
        print(f"[{_+1:5}] { w }")
    wi.stop()


def main(args):
    play(args.seed, args.count)
