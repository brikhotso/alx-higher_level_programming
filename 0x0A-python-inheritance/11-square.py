#!/usr/bin/python3
"""Contain class that defines a square inherited from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a Square."""

    def __init__(self, size):
        """Initialize a Square instance."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Return area of a square"""
        return self.__size ** 2

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] {}/{}".format(self._Rectangle__width,
                                       self._Rectangle__height)
