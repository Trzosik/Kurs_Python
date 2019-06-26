import unittest
from fields import trapez


class TrapezTestCase(unittest.TestCase):

    def setUp(self):
        self.a = 6
        self.b = 8
        self.h = 4

    def test_trapez(self):
        self.assertEqual(trapez(self.a, self.b, self.h), 28)

    def tearDown(self):
        del self.a
        del self.b
        del self.h


if __name__ == '__main__':
    unittest.main()
