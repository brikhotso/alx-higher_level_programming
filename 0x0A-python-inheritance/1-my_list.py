#!/usr/bin/python3
""" contains class that inherits from list"""


class MyList(list):
    """Represent a list """

    def print_sorted(self):
        """prints the list sorted in ascending sort"""
        print(sorted(self))
