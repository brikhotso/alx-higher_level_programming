#!/usr/bin/python3

""" Define a square of given size """


class Square:
    """This class represents a square with a given size."""

    def __init__(self, size=0):
        """
        Initializes a square instance with the specified size.

        Parameters:
        - size (number): The size of the square (default is 0)
        """
        self.size = size

    @property
    def size(self):
        """Retrieve size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size to value."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
        number: The area of the square.
        """
        return self.__size * self.__size

    def __eq__(self, other):
        """Equality comparator."""
        return self.size == other.size

    def __ne__(self, other):
        """Inequality comparator."""
        return self.size != other.size

    def __lt__(self, other):
        """Less than comparator."""
        return self.size < other.size

    def __le__(self, other):
        """Less than or equal comparator."""
        return self.size <= other.size

    def __gt__(self, other):
        """Greater than comparator."""
        return self.size > other.size

    def __ge__(self, other):
        """Greater than or equal comparator."""
        return self.size >= other.size
