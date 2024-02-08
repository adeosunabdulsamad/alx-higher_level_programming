#!/usr/bin/python3


from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    def test_contructor_with_id(self):
        b = Base(12)
        self.assertEqual(b.id, 12)


if __name__ == '__main__':
    unittest.main()
