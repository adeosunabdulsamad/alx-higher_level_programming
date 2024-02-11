#!/usr/bin/python3


from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    def test_constructor_without_width(self):
        r1 = Rectangle(10, 2, 0, 0, 2)
        r2 = Rectangle(10, 2, 0, 0, 13)
        r3 = Rectangle(5, 6, 0, 0, 5)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r2.id, 13)
        self.assertEqual(r3.id, 5)

    def test_contructor_without_integer_one(self):
        with self.assertRaises(TypeError):
            Rectangle("10", 2)

    def test_constructor_less_than_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_constructor_without_integer_two(self):
        r6 = Rectangle(10, 12)
        with self.assertRaises(TypeError):
            r6.x = {}

    def test_area_of_rectangle(self):
        r7 = Rectangle(4, 5, 0, 0, 4)
        x = r7.area()
        self.assertEqual(x, 20)


if __name__ == '__main__':
    unittest.main()
