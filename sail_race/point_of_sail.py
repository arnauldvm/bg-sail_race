from enum import Enum


class PointOfSail(Enum):
    INTO_THE_WIND = (0, None)
    CLOSE_REACH = (60, +0)
    BROAD_REACH = (120, +1)
    RUNNING = (180, +0)

    def __init__(self, bearing, delta_speed):
        self.bearing = bearing
        self.delta_speed = delta_speed

    def boat_speed(self, wind_speed):
        if self == PointOfSail.INTO_THE_WIND:
            return 0
        else:
            return wind_speed + self.delta_speed

# TODO: determine PointOfSail from BoatBearing and Wind.bearing()
