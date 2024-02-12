#!/usr/bin/python3


from models.square import Square
import unittest


class TestSquare(unittest.TestCase):
    def test_constructor_without_width(self):
        r1 = Square(10, 2, 0, 2)
        r2 = Square(10, 2, 0, 13)
        r3 = Square(5, 6, 0, 5)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r2.size, 10)
        self.assertEqual(r3.id, 5)

    def test_contructor_without_integer_one(self):
        with self.assertRaises(TypeError):
            Square("10")

    def test_constructor_less_than_zero(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_constructor_without_integer_two(self):
        r6 = Square(10)
        with self.assertRaises(TypeError):
            r6.x = {}

    def test_area_of_rectangle(self):
        r7 = Square(4, 0, 0, 4)
        x = r7.area()
        self.assertEqual(x, 16)


if __name__ == '__main__':
    unittest.main()
