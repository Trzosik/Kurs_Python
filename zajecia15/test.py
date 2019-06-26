import unittest
from fields import rectangle
from fields import triangle
from fields import trapez
form fields import trapez2


class FieldsTestCase(unittest.TestCase):

    def setUp(self):
        self.a = 6
        self.b = 6

    def test_rectangle_with_correct_values(self):
        self.assertEqual(rectangle(self.a, self.b), 36)

    def test_triangle_with_correct_values(self):
        self.assertEqual(triangle(self.a, self.b), 18)

    def test_rectangle_with_incorrect_value(self):
        self.assertRaises(ValueError, rectangle, 'a', 4)

    def test_rectangle_with_correct_value(self):
        self.assertRaises(ValueError, rectangle, 4, 5)

    def test_triangle_with_incorrect_value(self):
        self.assertRaises(ValueError, triangle, 'm', 4)

    def test_triangle_with_correct_value(self):
        self.assertRaises(ValueError, triangle, 4, 5)

    def test_trapez_with_incorrect_value(self):
        self.assertRaises(ValueError, trapez, 'm', 5, 4)

    def test_trapez_with_correct_values(self):
        self.assertRaises(ValueError, trapez, 4, 5, 6)

    def tearDown(self):
        del self.a
        del self.b


if __name__ == '__main__':
    unittest.main()
