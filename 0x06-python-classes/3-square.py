#!/usr/bin/python3

""" Define a square of given size """


class Square:
    """This class represents a square with a given size."""
    def __init__(self, size=0):
        """
        Initializes a square instance with the specified size.

        Parameters:
        - size (int): The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
        int: The area of the square.
        """
        return self.__size * self.__size
