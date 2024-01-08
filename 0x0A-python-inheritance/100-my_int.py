#!/usr/bin/python3
"""Define clsaa MyInt that inherits from int"""


class MyInt(int):
    """Class representing a rebel integer."""

    def __eq__(self, value):
        """Override the == operator."""
        return self.real != value

    def __ne__(self, value):
        """Override the != operator."""
        return self.real == value
