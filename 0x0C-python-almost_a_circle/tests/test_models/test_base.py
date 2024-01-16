#!/usr/bin/python3
"""
Module: test_models.test_base

This module contains unit tests for the Base class and its related methods.
"""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstantiation(unittest.TestCase):
    """
    Test cases for the instantiation of the Base class.
    """

    def test_create_instance_with_id(self):
        """
        Test creating an instance of Base with a specified ID.
        """
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_create_instance_without_id(self):
        """
        Test creating instances of Base without specifying an ID.
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_create_instance_with_str_id(self):
        """
        Test creating an instance of Base with a string ID.
        """
        b = Base("string_id")
        self.assertEqual(b.id, "string_id")


class TestJsonAndSaveToFile(unittest.TestCase):
    """
    Test cases for JSON serialization and saving to file methods of Base class.
    """

    def test_to_json_string_with_empty_list(self):
        """
        Test converting an empty list to a JSON string.
        """
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_to_json_string_with_valid_list(self):
        """
        Test converting a valid list of dictionaries to a JSON string.
        """
        json_str = Base.to_json_string([{"id": 1, "name": "example"}])
        expected_str = '[{"id": 1, "name": "example"}]'
        self.assertEqual(json_str, expected_str)

    def test_to_json_string_with_none(self):
        """
        Test converting None to a JSON string.
        """
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")

    def test_save_to_file_with_empty_list(self):
        """
        Test saving to file with an empty list of instances.
        """
        Base.save_to_file([])
        with open("Base.json", "r") as file:
            content = file.read()
        self.assertEqual(content, "[]")


class TestJsonAndLoadFromFile(unittest.TestCase):
    """
    Test cases for loading instances from JSON file methods of Base class.
    """

    def test_load_from_file_with_nonexistent_file(self):
        """
        Test loading instances when the JSON file does not exist.
        """
        instances = Base.load_from_file()
        self.assertEqual(instances, [])

    def test_load_from_file_with_empty_file(self):
        """
        Test loading instances from an empty JSON file.
        """
        with open("Base.json", "w") as file:
            file.write("")
        instances = Base.load_from_file()
        self.assertEqual(instances, [])


class TestCsvMethods(unittest.TestCase):
    """
    Test cases for CSV serialization and loading from CSV file methods.
    """

    def test_save_to_file_csv_with_empty_list(self):
        """
        Test saving to CSV file with an empty list of instances.
        """
        Base.save_to_file_csv([])
        with open("Base.csv", "r") as file:
            content = file.read()
        self.assertEqual(content, "")

    def test_load_from_file_csv_with_nonexistent_file(self):
        """
        Test loading instances from CSV when the file does not exist.
        """
        instances = Base.load_from_file_csv()
        self.assertEqual(instances, [])

    def test_load_from_file_csv_with_empty_file(self):
        """
        Test loading instances from an empty CSV file.
        """
        with open("Base.csv", "w") as file:
            file.write("")
        instances = Base.load_from_file_csv()
        self.assertEqual(instances, [])


if __name__ == "__main__":
    unittest.main()
