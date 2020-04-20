import unittest

import sail_race.draws as draws
import sail_race.wind as wind


class WindTestCase(unittest.TestCase):

    def test_init_bearing(self):
        draws.die.seed(0)
        for _ in range(100):
            b = wind.init_bearing()
            self.assertEquals(b % 10, 0)
            self.assertIn(b // 10, range(36))

    def test_init(self):
        draws.die.seed(0)
        for _ in range(100):
            w = wind.Wind()
            self.assertEquals(w.bearing() % 10, 0)
            self.assertIn(w.bearing() // 10, range(36))
            self.assertEqual(w.speed(), wind.INIT_SPEED)

    def test_iter(self):
        draws.die.seed(0)
        w = wind.Wind()
        print(w)
        wi = iter(w)
        for _ in range(1000):
            next(wi)
            # print(w)
            self.assertEquals(w.bearing() % 10, 0)
            self.assertIn(w.bearing() // 10, range(36))
            self.assertGreaterEqual(w.speed(), wind.MIN_SPEED)
            self.assertLessEqual(w.speed(), wind.GALE_SPEED)
        wi.stop()
