import unittest

import sail_race as sr


class WindTestCase(unittest.TestCase):

    def test_init_bearing(self):
        sr.die.seed(0)
        for _ in range(100):
            b = sr.init_bearing()
            self.assertEquals(b % 10, 0)
            self.assertIn(b // 10, range(36))

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
