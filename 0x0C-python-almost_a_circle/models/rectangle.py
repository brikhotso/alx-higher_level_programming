#!/usr/bin/python3
"""Contain class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class inherits from Base

    Attributes:
        __width (int): A private class attribute.
        __height (int): A private class attribute.
        __x (int): A private class attribute.
        __y (int): A private class attribute.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X-coordinate of the rectangle.
            y (int): Y-coordinate of the rectangle.
            id (int): If provided, assigns ID to instance; else,
                create a new ID based on current value of __nb_objects.
        Returns:
            None
        """
        super().__init__(id)

        self.check_positive_integer("width", width)
        self.check_positive_integer("height", height)
        self.check_non_negative_integer("x", x)
        self.check_non_negative_integer("y", y)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter method for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width attribute."""
        self.check_positive_integer("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter method for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height attribute."""
        self.check_positive_integer("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter method for the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for the x attribute."""
        self.check_non_negative_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter method for the y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for the y attribute."""
        self.check_non_negative_integer("y", value)
        self.__y = value

    def check_positive_integer(self, attribute_name, value):
        """
        Helper method to check if a value is a positive integer.

        Args:
            attribute_name (str): Name of attribute to check.
            value (int): The value to be checked.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not a positive integer.
        """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(attribute_name))
        if value <= 0:
            raise ValueError("{:s} must be > 0".format(attribute_name))

    def check_non_negative_integer(self, attribute_name, value):
        """
        Helper method to check if a value is a non-negative integer.

        Args:
            attribute_name (str): Name of attribute to check.
            value (int): The value to be checked.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not a non-negative integer.
        """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(attribute_name))
        if value < 0:
            raise ValueError("{:s} must be >= 0".format(attribute_name))

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.height * self.width

    def display(self):
        """
        Prints the Rectangle instance with the character #,
        considering x and y offsets.
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def to_dictionary(self):
        """Return a dictionary representation of the Rectangle instance."""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """Return a string representation of the Rectangle instance."""
        return ("[Rectangle] ({}) {}/{} - {}/{}".
                format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """
        Assigns arguments to attributes using both *args and **kwargs:

        - If *args is present and not empty, **kwargs will be skipped.
        - Each key in kwargs represents an attribute to the instance.
        """

        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
