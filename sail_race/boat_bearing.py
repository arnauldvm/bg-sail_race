from enum import Enum


class BoatBearing(Enum):
    E = (-20, 30)
    NE = (40, 90)
    NW = (100, 150)
    W = (160, 210)
    SW = (220, 270)
    SE = (280, 330)

    def __init__(self, min, max):
        self.min = min
        self.max = max
