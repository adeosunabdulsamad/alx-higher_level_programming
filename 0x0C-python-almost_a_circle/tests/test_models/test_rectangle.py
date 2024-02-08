#!/usr/bin/python3


from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    def test_constructor_without_width(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(10, 2, 0, 0, 13)
        r3 = Rectangle(5, 6)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 13)
        self.assertEqual(r3.id, 2)


if __name__ == '__main__':
    unittest.main()
