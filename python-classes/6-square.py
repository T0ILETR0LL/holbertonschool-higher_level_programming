#!/usr/bin/python3
"""Square class"""


class Square:
    '''Square is int'''
    def __init__(self, size=0, position=(0,0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(self.position, tuple):
            raise TypeError ("position must be a tuple of 2 positive intergers")
        if len(self.position) is not 2:
            raise TypeError ("position must be a tuple of 2 positive intergers")
        for coord in self.position: ##HERE##
            if type(value) is not int:
                raise TypeError("position must be a tuple of 2 positive intergers")
            if value < 0:
                raise TypeError("position must be a tuple of 2 positive intergers")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.position[1] > 0:
            print ("\n")
        if self.size is 0:
            print("")
        else:
            for i in range(self.size):
                for value in range(self.position[0]):
                    print (" ",end="")
                print("#" * self.size)
