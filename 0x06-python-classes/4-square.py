#!/usr/bin/python3

""" Define a square of given size """


class Square:
    """This class represents a square with a given size."""

    def __init__(self, size=0):
        """
        Initializes a square instance with the specified size.

        Parameters:
        - size (int): The size of the square (default is 0)
        """
        self.size = size

    @property
    def size(self):
        """Retrieve size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size to value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
        int: The area of the square.
        """
        return self.__size * self.__size
