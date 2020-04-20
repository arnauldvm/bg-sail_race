from ..draws import _2d6_to_d36
from ..wind import INIT_SPEED, GALE_SPEED, MIN_SPEED, MAX_SPEED
from ..wind import wind_brg_evolution_table, wind_speed_evolution_table
from ..wind import WindSpeedEvolution

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
    print(f"2D6 |", end='')
    for d2 in range(1, 7):
        print(f"  {d2} ", end='')
    print()
    print("--- + --- --- --- --- --- ---")
    for d1 in range(1, 7):
        print(f" {d1}  |", end='')
        for d2 in range(1, 7):
            bearing = _2d6_to_d36([d1, d2])*10
            print(f" {bearing:3}", end='')
        print()


def table_next_wind():
    print("Next wind delta (bearing and speed):")
    print(f"2D6 |", end='')
    for d2 in range(1, 7):
        print(f"   {d2}  ", end='')
    print()
    print("--- + ----- ----- ----- ----- ----- -----")
    for d1 in range(1, 7):
        print(f" {d1}  |", end='')
        for d2 in range(1, 7):
            draw = _2d6_to_d36([d1, d2])
            bearing_delta = wind_brg_evolution_table[draw]
            speed_evolution = wind_speed_evolution_table[draw]
            if WindSpeedEvolution.INCR == speed_evolution:
                symbol = "+"
            elif WindSpeedEvolution.DECR == speed_evolution:
                symbol = "-"
            elif WindSpeedEvolution.SAME == speed_evolution:
                symbol = "="
            elif WindSpeedEvolution.GALE == speed_evolution:
                symbol = "g"
            print(f" {bearing_delta:+3}/{symbol}", end='')
        print()
    print(f"  Average speeds must always stay within [{MIN_SPEED}, {MAX_SPEED}]")
    print(f"  'g' means gale: temporary wind of speed {GALE_SPEED}")


def main(args):
    tables()
