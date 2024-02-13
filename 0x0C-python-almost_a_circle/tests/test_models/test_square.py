#!/usr/bin/python3
"""
Module: test_models.test_square

This module contains unit tests for the Square class and its related methods.
"""

import unittest
import os
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Test cases for the Square class and its methods.
    """

    def test_create_instance_with_id(self):
        """
        Test creating an instance of Square with a specified ID.
        """
        s = Square(5, id=10)
        self.assertEqual(s.id, 10)

    def test_create_instance_with_zero_size(self):
        """
        Test creating an instance of Square with zero size.
        """
        with self.assertRaises(ValueError):
            Square(0)

    def test_create_instance_with_negative_size(self):
        """
        Test creating an instance of Square with negative size.
        """
        with self.assertRaises(ValueError):
            Square(-5)

    def test_create_instance_with_negative_x_y(self):
        """
        Test creating an instance of Square with negative x and y values.
        """
        with self.assertRaises(ValueError):
            Square(5, -1, -2)

    def test_to_dictionary(self):
        """
        Test converting a Square instance to a dictionary.
        """
        s = Square(5, 2, 3, 10)
        expected_dict = {'id': 10, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(s.to_dictionary(), expected_dict)

    def test_to_str(self):
        """
        Test obtaining a string representation of a Square instance.
        """
        s = Square(5, 2, 3, 10)
        expected_str = "[Square] (10) 2/3 - 5"
        self.assertEqual(str(s), expected_str)

    def test_update_with_args(self):
        """
        Test updating a Square instance using *args.
        """
        s = Square(5, 2, 3, 10)
        s.update(20, 10, 5, 1)
        self.assertEqual(s.to_dictionary(), {'id': 20, 'size': 10,
                                             'x': 5, 'y': 1})

    def test_update_with_kwargs(self):
        """
        Test updating a Square instance using **kwargs.
        """
        s = Square(5, 2, 3, 10)
        s.update(size=10, x=5, y=1)
        self.assertEqual(s.to_dictionary(), {'id': 10, 'size': 10,
                                             'x': 5, 'y': 1})

    def test_create_instance_with_missing_arguments(self):
        """
        Test creating an instance of Square with missing arguments.
        """
        with self.assertRaises(TypeError):
            Square()

    def test_create_instance_with_extra_argument(self):
        """
        Test creating an instance of Square with an extra argument.
        """
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_create_instance_with_invalid_argument_types(self):
        """
        Test creating an instance of Square with invalid argument types.
        """
        with self.assertRaises(TypeError):
            Square("1")

        with self.assertRaises(TypeError):
            Square(1, "2")

        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_create_instance_with_negative_size(self):
        """
        Test creating an instance of Square with negative size.
        """
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_create_instance_with_negative_x_y(self):
        """
        Test creating an instance of Square with negative x and y values.
        """
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_create_method_in_square(self):
        """
        Test create method in Square class.
        """
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.to_dictionary(), {'id': 89, 'size': 1,
                                             'x': 2, 'y': 3})

    def test_save_to_file_with_none(self):
        """
        Test saving to file with None in Square.
        """
        with self.assertRaises(TypeError):
            Square(None)

    def test_save_to_file_with_empty_list(self):
        """
        Test saving to file with an empty list in Square.
        """
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            content = file.read()
        self.assertEqual(content, "[]")

    def test_load_from_file_with_nonexistent_file(self):
        """
        Test loading instances from file when the file does not exist in Square.
        """
        instances = Square.load_from_file()
        self.assertEqual(instances, [])

    def test_load_from_file_with_existing_file(self):
        """
        Test loading instances from an existing file in Square.
        """
        with open("Square.json", "w") as file:
            file.write('[{"id": 1, "size": 5, "x": 2, "y": 3}]')
        instances = Square.load_from_file()
        expected_instance = Square(5, 2, 3, 1)
        self.assertEqual(instances[0].to_dictionary(),
                         expected_instance.to_dictionary())

    def tearDown(self):
        """
        Clean up by removing the created JSON file after each test.
        """
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    unittest.main()
