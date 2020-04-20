import unittest

import sail_race as sr


class DrawsTestCase(unittest.TestCase):

    def test_draw(self):
        sr.die.seed(0)
        for _ in range(100):
            d = sr.draw()
            self.assertEquals(len(d), 2)
            self.assertIn(d[0], range(1, 7))
            self.assertIn(d[1], range(1, 7))

    def test_draw36(self):
        sr.die.seed(0)
        for _ in range(100):
            d = sr.draw36()
            self.assertIn(d, range(36))
