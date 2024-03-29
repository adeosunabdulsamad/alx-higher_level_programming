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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """The getter property of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """The setter property of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """The getter property of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """The setter property of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """The getter property of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """The setter property of x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """The getter property of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """The setter property of y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """This function returns the area of the rectangle"""
        Rectangle_area = self.__width * self.__height
        return Rectangle_area

    def display(self):
        """This function displays the rectangle"""
        real_y = self.__y - 1
        if real_y > 0:
            print("\n" * real_y)
        for i in range(self.__height):
            display_width = "#" * self.__width
            display_x = " " * self.__x
            print(display_x + display_width)

    def __str__(self):
        """This is the string dunder method for rectangle class"""
        ide = self.id
        w = self.width
        h = self.height
        y = self.y
        x = self.x
        return f"[Rectangle] ({ide}) {x}/{y} - {w}/{h}"

    def update(self, *args, **kwargs):
        """This method updates the Rectangle Class"""
        if args:
            self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]

        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """This method converts the class to a dictionary"""
        dic = {}
        dic["id"] = self.id
        dic["width"] = self.width
        dic["height"] = self.height
        dic["y"] = self.y
        dic["x"] = self.x
        return dic
