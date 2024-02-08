#!/usr/bin/python3
"""This is a rectangle module"""


from models.base import Base


class Rectangle(Base):
    """This is the rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """This is the rectangle class constructor"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
