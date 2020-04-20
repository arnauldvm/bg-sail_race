import unittest

import sail_race as sr


class PointOfSailTestCase(unittest.TestCase):

    def test_boat_speed_into_the_wind(self):
        self.assertEquals(sr.PointOfSail.INTO_THE_WIND.boat_speed(1), 0)
        self.assertEquals(sr.PointOfSail.INTO_THE_WIND.boat_speed(2), 0)
        self.assertEquals(sr.PointOfSail.INTO_THE_WIND.boat_speed(3), 0)

    def test_boat_speed_close_reach(self):
        self.assertEquals(sr.PointOfSail.CLOSE_REACH.boat_speed(1), 1)
        self.assertEquals(sr.PointOfSail.CLOSE_REACH.boat_speed(2), 2)
        self.assertEquals(sr.PointOfSail.CLOSE_REACH.boat_speed(3), 3)

    def test_boat_speed_broad_reach(self):
        self.assertEquals(sr.PointOfSail.BROAD_REACH.boat_speed(1), 2)
        self.assertEquals(sr.PointOfSail.BROAD_REACH.boat_speed(2), 3)
        self.assertEquals(sr.PointOfSail.BROAD_REACH.boat_speed(3), 4)

    def test_boat_speed_running(self):
        self.assertEquals(sr.PointOfSail.RUNNING.boat_speed(1), 1)
        self.assertEquals(sr.PointOfSail.RUNNING.boat_speed(2), 2)
        self.assertEquals(sr.PointOfSail.RUNNING.boat_speed(3), 3)
