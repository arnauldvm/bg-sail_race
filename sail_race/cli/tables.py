from ..draws import _2d6_to_d36
from ..wind import INIT_SPEED

DESCRIPTION = 'Generate tables'


def fill_argparser(parser):
    parser.description = DESCRIPTION


def tables():
    table_init_speed()
    table_init_bearing()
    print()
    table_next_wind()


def table_init_speed():
    print(f"Initial wind speed: { INIT_SPEED}")


def table_init_bearing():
    print("Initial wind bearing:")
    print(f"  |", end='')
    for d2 in range(1, 7):
        print(f"  {d2} ", end='')
    print()
    print("- + --- --- --- --- --- ---")
    for d1 in range(1, 7):
        print(f"{d1} |", end='')
        for d2 in range(1, 7):
            bearing = _2d6_to_d36([d1, d2])*10
            print(f" {bearing:3}", end='')
        print()


def table_next_wind():
    None


def main(args):
    tables()
