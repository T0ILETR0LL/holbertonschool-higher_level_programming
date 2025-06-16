#!/usr/bin/python3
"""Square class"""


class Square:
    '''Square is int'''
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an interger")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
