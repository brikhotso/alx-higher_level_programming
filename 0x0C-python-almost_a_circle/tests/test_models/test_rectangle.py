#!/usr/bin/python3
"""
Module: test_models.test_rectangle

Contains unit tests for the Rectangle class and its related methods.
"""

import unittest
import os
import contextlib
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class and its methods.
    """

    def test_display_one_arg(self):
        r = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            r.display(1)

    def test_display_width_height(self):
        r = Rectangle(2, 3, 0, 0, 0)
        with contextlib.redirect_stdout(StringIO()) as capture:
            r.display()
        self.assertEqual(capture.getvalue(), "##\n##\n##\n")

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

    def test_create_instance_with_negative_x_y(self):
        """
        Test creating an instance of Rectangle with negative x and y values.
        """
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -1, -2)

    def test_create_instance_with_missing_arguments(self):
        """
        Test creating an instance of Rectangle with missing arguments.
        """
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_create_instance_with_extra_argument(self):
        """
        Test creating an instance of Rectangle with an extra argument.
        """
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_create_instance_with_invalid_argument_types(self):
        """
        Test creating an instance of Rectangle with invalid argument types.
        """
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_create_instance_with_negative_width_height(self):
        """
        Test creating an instance of Rectangle with negative width and height.
        """
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_create_method_in_rectangle(self):
        """
        Test create method in Rectangle class.
        """
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3,
                                'y': 4})
        self.assertEqual(r.to_dictionary(), {'id': 89, 'width': 1, 'height': 2,
                                             'x': 3, 'y': 4})

    def test_save_to_file_with_none(self):
        """
        Test saving to file with None in Rectangle.
        """
        with self.assertRaises(TypeError):
            Rectangle(None)

    def test_save_to_file_with_empty_list(self):
        """
        Test saving to file with an empty list in Rectangle.
        """
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            content = file.read()
        self.assertEqual(content, "[]")

    def test_load_from_file_with_nonexistent_file(self):
        """
        Test loading instances from file when file does not exist in Rectangle.
        """
        instances = Rectangle.load_from_file()
        self.assertEqual(instances, [])

    def test_load_from_file_with_existing_file(self):
        """
        Test loading instances from an existing file in Rectangle.
        """
        with open("Rectangle.json", "w") as file:
            file.write('[{"id": 1, "width": 5, "height": 10, "x": 2, "y": 3}]')
        instances = Rectangle.load_from_file()
        expected_instance = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(instances[0].to_dictionary(),
                         expected_instance.to_dictionary())

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
