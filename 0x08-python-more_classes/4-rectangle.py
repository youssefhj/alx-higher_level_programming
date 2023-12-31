#!/usr/bin/python3
"""
Defines a Rectangle class
"""


class Rectangle:
    """Respresent a Rectangle"""
    def __init__(self, width=0, height=0):
        """Constructor"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area getter"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter of rectangel"""
        if self.__width > 0 and self.__height > 0:
            return 2 * (self.__width + self.__height)
        return 0

    def __str__(self):
        """Return string with # forming a rectangle"""
        s = ""
        if self.__width != 0 and self.__height != 0:
            s += "\n".join("#" * self.__width for i in range(self.__height))

        return s

    def __repr__(self):
        """Representation of rectange object"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
