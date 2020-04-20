import unittest

import sail_race.draws as draws


class DrawsTestCase(unittest.TestCase):

    def test_draw(self):
        draws.seed(0)
        for _ in range(100):
            d = draws.draw()
            self.assertEquals(len(d), 2)
            self.assertIn(d[0], range(1, 7))
            self.assertIn(d[1], range(1, 7))

    def test_draw36(self):
        draws.seed(0)
        for _ in range(100):
            d = draws.draw36()
            self.assertIn(d, range(36))
