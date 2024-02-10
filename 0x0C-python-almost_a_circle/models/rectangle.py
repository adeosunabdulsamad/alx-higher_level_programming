#!/usr/bin/python3
"""This is a rectangle module"""


from models.base import Base


class Rectangle(Base):
    """This is the rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """This is the rectangle class constructor"""
        super().__init__(id)
        self.__width = None
        self.__height = None
        self.__x = None
        self.__y = None
        self.set_width(width)
        self.set_height(height)
        self.set_x(x)
        self.set_y(y)
        params =[("width", self.__width), ("height", self.__height), ("x", self.__x), ("y", self.__y)]
    def set_width(self, width):
            if not isinstance(width, int):
                raise TypeError("width must be an integer")
            if width <= 0:
                raise ValueError("width must be > 0")
        for 
