#!/usr/bin/python3
"""Contain class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inherits from Rectangle

    Attributes:
        size (int): Private class attribute representing size of square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): Size of the square.
            x (int): X-coordinate of the square.
            y (int): Y-coordinate of the square.
            id (int): If provided, assigns ID to instance; else,
                create a new ID based on the current value of __nb_objects.
        Returns:
            None
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for the size attribute."""
        self.width = value
        self.height = value

    def to_dictionary(self):
        """Return a dictionary representation of the Square instance."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """Return a string representation of the Square instance."""
        return ("[Square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """
        Assigns arguments to attributes using both *args and **kwargs:

        - If *args is present and not empty, **kwargs will be skipped.
        - Each key in kwargs represents an attribute to the instance.
        """

        if args:
            attributes = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
