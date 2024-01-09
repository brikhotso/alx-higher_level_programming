#!/usr/bin/python3
"""Define class student"""


class Student:
    """Represent a student"""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        Parameters:
        - first_name (str): The first name of the student.
        - last_name (str): The last name of the student.
        - age (int): The age of the student.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Parameters:
        - attrs (list, optional): A list of attribute names to retrieve.
          If None, all attributes will be retrieved.

        Returns:
        dict: A dictionary containing the specified attributes
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance.

        Parameters:
        - json (dict): A dictionary containing attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)
