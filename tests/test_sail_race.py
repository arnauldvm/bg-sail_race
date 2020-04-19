import unittest

import sail_race as sr


class SailRaceTestCase(unittest.TestCase):

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

    def test_init_bearing(self):
        sr.die.seed(0)
        for _ in range(100):
            b = sr.init_bearing()
            self.assertEquals(b % 10, 0)
            self.assertIn(b // 10, range(36))


class WindTestCase(unittest.TestCase):

    def test_init(self):
        sr.die.seed(0)
        for _ in range(100):
            w = sr.Wind()
            self.assertEquals(w.bearing() % 10, 0)
            self.assertIn(w.bearing() // 10, range(36))
            self.assertEqual(w.speed(), sr.INIT_SPEED)

    def test_iter(self):
        sr.die.seed(0)
        w = sr.Wind()
        print(w)
        wi = iter(w)
        for _ in range(1000):
            next(wi)
            # print(w)
            self.assertEquals(w.bearing() % 10, 0)
            self.assertIn(w.bearing() // 10, range(36))
            self.assertGreaterEqual(w.speed(), sr.MIN_SPEED)
            self.assertLessEqual(w.speed(), sr.GALE_SPEED)
        wi.stop()
