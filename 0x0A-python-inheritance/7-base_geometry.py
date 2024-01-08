#!/usr/bin/python3
"""contain class thant define area"""


class BaseGeometry:
    """ Define class """

    def area(self):
        """
        Define area

        raise:
            Exception: area() is not implemented
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate value

        args:
            name (str): name of parameter
            value (int): paramenter to validate

        raises:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
