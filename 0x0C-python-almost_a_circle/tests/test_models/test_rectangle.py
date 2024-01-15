#!/usr/bin/python3
"""
Module: test_models.test_rectangle

Contains unit tests for the Rectangle class and its related methods.
"""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class and its methods.
    """

    def test_create_instance_with_id(self):
        """
        Test creating an instance of Rectangle with a specified ID.
        """
        r = Rectangle(5, 10, id=10)
        self.assertEqual(r.id, 10)

    def test_create_instance_with_zero_width(self):
        """
        Test creating an instance of Rectangle with zero width.
        """
        with self.assertRaises(ValueError):
            Rectangle(0, 10)

    def test_create_instance_with_negative_width(self):
        """
        Test creating an instance of Rectangle with negative width.
        """
        with self.assertRaises(ValueError):
            Rectangle(-5, 10)

    def test_create_instance_with_zero_height(self):
        """
        Test creating an instance of Rectangle with zero height.
        """
        with self.assertRaises(ValueError):
            Rectangle(5, 0)

    def test_create_instance_with_negative_height(self):
        """
        Test creating an instance of Rectangle with negative height.
        """
        with self.assertRaises(ValueError):
            Rectangle(5, -10)

    def test_create_instance_with_negative_x_y(self):
        """
        Test creating an instance of Rectangle with negative x and y values.
        """
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -1, -2)

    def test_area(self):
        """
        Test calculating the area of a Rectangle instance.
        """
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_to_dictionary(self):
        """
        Test converting a Rectangle instance to a dictionary.
        """
        r = Rectangle(5, 10, 2, 3, 10)
        expected_dict = {'id': 10, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        self.assertEqual(r.to_dictionary(), expected_dict)

    def test_to_str(self):
        """
        Test obtaining a string representation of a Rectangle instance.
        """
        r = Rectangle(5, 10, 2, 3, 10)
        expected_str = "[Rectangle] (10) 2/3 - 5/10"
        self.assertEqual(str(r), expected_str)

    def test_update_with_args(self):
        """
        Test updating a Rectangle instance using *args.
        """
        r = Rectangle(5, 10, 2, 3, 10)
        r.update(20, 15, 8, 4)
        self.assertEqual(r.to_dictionary(), {'id': 20, 'width': 15,
                                             'height': 8, 'x': 4, 'y': 3})

    def test_update_with_kwargs(self):
        """
        Test updating a Rectangle instance using **kwargs.
        """
        r = Rectangle(5, 10, 2, 3, 10)
        r.update(width=15, height=8, x=4, y=1)
        self.assertEqual(r.to_dictionary(), {'id': 10, 'width': 15,
                                             'height': 8, 'x': 4, 'y': 1})

    def tearDown(self):
        """
        Clean up by removing the created JSON file after each test.
        """
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    unittest.main()
