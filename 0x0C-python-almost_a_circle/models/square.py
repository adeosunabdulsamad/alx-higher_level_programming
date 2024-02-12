#!/usr/bin/python3
"""This is the module for square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """This is the square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """This is the constructor method"""
        super().__init__(size, size, x, y, id)
        self.__size = size

    @property
    def size(self):
        """Size property of the class"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value

    def __str__(self):
        """This is a dunder method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
