from sys import maxsize as maxint
from enum import IntEnum

from .draws import draw36


def init_bearing():
    return draw36()*10


wind_brg_evolution_table = [
    -30, -20, -10, +10, +20, +30,
    -20, -10, 000, 000, +10, +20,
    -10, 000, 000, 000, 000, +10,
    -10, 000, 000, 000, 000, +10,
    -20, -10, 000, 000, +10, +20,
    -30, -20, -10, +10, +20, +30,
]


MIN_SPEED = 1
MAX_SPEED = 3
GALE_SPEED = 3
INIT_SPEED = 2


def init_speed():
    return INIT_SPEED


class WindSpeedEvolution(IntEnum):
    DECR = -1
    SAME = 00
    INCR = +1
    GALE = maxint


GALE = WindSpeedEvolution.GALE
SAME = WindSpeedEvolution.SAME
DECR = WindSpeedEvolution.DECR
INCR = WindSpeedEvolution.INCR

wind_speed_evolution_table = [
    GALE, DECR, DECR, INCR, INCR, GALE,  # !
    SAME, SAME, INCR, DECR, SAME, SAME,
    INCR, DECR, SAME, SAME, INCR, DECR,
    DECR, INCR, SAME, SAME, DECR, INCR,
    SAME, SAME, DECR, INCR, SAME, SAME,
    GALE, INCR, INCR, DECR, DECR, GALE,  # !
]


class Wind():

    def __init__(self):
        super().__init__()
        self._bearing = init_bearing()
        self._avg_speed = init_speed()
        self._is_gale = False

    def _next(self):
        d = draw36()
        self._bearing = (self._bearing + wind_brg_evolution_table[d]) % 360
        speed_change = wind_speed_evolution_table[d]
        if WindSpeedEvolution.GALE == speed_change:
            self._is_gale = True
        else:
            self._is_gale = False
            self._avg_speed = max(min(
                self._avg_speed + speed_change,
                MAX_SPEED), MIN_SPEED)

    def speed(self):
        if self._is_gale:
            return GALE_SPEED
        else:
            return self._avg_speed

    def bearing(self):
        return self._bearing

    def __str__(self):
        return (
            f"BRG: {self.bearing():3}, SPD: { self.speed() }"
            f"{ ' GALE (avg:%d)' % self._avg_speed if self._is_gale else ''}"
        )

    def __iter__(self):
        return WindIterator(self)


class WindIterator:

    def __init__(self, wind):
        self._wind = wind
        self._is_finished = False

    def __next__(self):
        if self._is_finished:
            raise StopIteration
        self._wind._next()
        return self._wind

    def stop(self):
        self._is_finished = True
