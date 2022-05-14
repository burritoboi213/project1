import unittest
from dereck_martinez import *


class MyTestCase(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(circle_area(1), 3.141, delta=0.001)
        self.assertAlmostEqual(circle_area(0.5), 0.785, delta=0.001)

        with self.assertRaises(TypeError):
            circle_area('0.1')
        with self.assertRaises(ValueError):
            circle_area(0)
            circle_area(-1)

    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(2, 1), 2)
        self.assertAlmostEqual(rectangle_area(1.5, 1), 1.5, delta=0.001)
        self.assertAlmostEqual(rectangle_area(1, 1.6), 1.6, delta=0.001)
        self.assertAlmostEqual(rectangle_area(1.5, 2.1), 3.15, delta=0.001)

        with self.assertRaises(TypeError):
            rectangle_area(1, '1.5')
            rectangle_area('0', 1.5)
            rectangle_area('0', '1.5')
        with self.assertRaises(ValueError):
            rectangle_area(-1, 1.5)
            rectangle_area(1, -1.5)
            rectangle_area(-1, -1.5)
            rectangle_area(0, 1.5)
            rectangle_area(2, 0)
            rectangle_area(0, 0)

    def test_square_area(self):
        self.assertEqual(square_area(10), 100)
        self.assertAlmostEqual(square_area(0.1), 0.01, delta=0.001)

        with self.assertRaises(TypeError):
            square_area('0.1')
        with self.assertRaises(ValueError):
            square_area(0)
            square_area(-1)

    def test_triangle_area(self):
        self.assertEqual(triangle_area(2, 1), 1)
        self.assertAlmostEqual(triangle_area(1.5, 1), 0.75, delta=0.001)
        self.assertAlmostEqual(triangle_area(1, 1.6), 0.8, delta=0.001)
        self.assertAlmostEqual(triangle_area(1.5, 2.1), 1.575, delta=0.001)

        with self.assertRaises(TypeError):
            rectangle_area(1, '1.5')
            rectangle_area('0', 1.5)
            rectangle_area('0', '1.5')
        with self.assertRaises(ValueError):
            rectangle_area(-1, 1.5)
            rectangle_area(1, -1.5)
            rectangle_area(-1, -1.5)
            rectangle_area(0, 1.5)
            rectangle_area(2, 0)
            rectangle_area(0, 0)




if __name__ == '__main__':
    unittest.main()
