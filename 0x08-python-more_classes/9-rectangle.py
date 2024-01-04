#!/usr/bin/python3
"""Define a rectangle."""


class Rectangle:
    """
    Class to represent a rectangle.

    Attributes:
    - number_of_instances (int): Number of rectangle instances
    - print_symbol (any): Symbol used as string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with the specified width and height.

        Parameters:
        - width (int): The width of the rectangle (default is 0).
        - height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Get width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the bigger rectangle based on the area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with width == height == size."""
        return cls(size, size)

    def __str__(self):
        """Return a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += str(self.print_symbol) * self.__width + "\n"
        return rectangle_str.rstrip()

    def __repr__(self):
        """Return a string representation of the rectangle."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
