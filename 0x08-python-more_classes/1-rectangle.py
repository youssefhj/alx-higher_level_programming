#!/usr/bin/python3
"""
Rectangle class module
"""


class Rectangle:
    """Definition of the Rectangle class"""
    def __init__(self, width=0, height=0):
        """Constructor"""
        self.__width = width
        self.__height = height

    def width(self):
        """width getter"""
        return self.__width

    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0 :
            raise ValueError('width must be >= 0')

        self.__width = value

    def height(self):
        """height getter"""
        return self.__height

    def height(self, value):
        """heght setter"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value


