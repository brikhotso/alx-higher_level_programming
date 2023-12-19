#!/usr/bin/python3

""" Define a square of given size """


class Square:
    """This class represents a square with a given size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square instance with the specified size and position.

        Parameters:
        - size (int): The size of the square (default is 0)
        - position (tuple): The position of the square (default is (0, 0))
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position to value."""
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
        int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square using '#' character.

        If size is 0, print an empty line.
        Use position to determine the starting position of the square.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
