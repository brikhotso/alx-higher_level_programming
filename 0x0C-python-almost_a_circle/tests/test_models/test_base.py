#!/usr/bin/python3
""" tests/test_models/test_base """
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstantiation(unittest.TestCase):

    def test_create_instance_with_id(self):
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_create_instance_without_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_create_instance_with_str_id(self):
        b = Base("string_id")
        self.assertEqual(b.id, "string_id")


class TestJsonAndSaveToFile(unittest.TestCase):

    def test_to_json_string_with_empty_list(self):
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_to_json_string_with_valid_list(self):
        json_str = Base.to_json_string([{"id": 1, "name": "example"}])
        expected_str = '[{"id": 1, "name": "example"}]'
        self.assertEqual(json_str, expected_str)

    def test_to_json_string_with_none(self):
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")

    def test_save_to_file_with_none_list(self):
        Base.save_to_file(None)
        with open("Base.json", "r") as file:
            content = file.read()
        self.assertEqual(content, "[]")

    def test_save_to_file_with_empty_list(self):
        Base.save_to_file([])
        with open("Base.json", "r") as file:
            content = file.read()
        self.assertEqual(content, "[]")

    def test_save_to_file_with_valid_list(self):
        b1 = Base(1)
        b2 = Base(2)
        Base.save_to_file([b1, b2])
        with open("Base.json", "r") as file:
            content = file.read()
        expected_content = '[{"id": 1}, {"id": 2}]'
        self.assertEqual(content, expected_content)


class TestJsonAndLoadFromFile(unittest.TestCase):

    def test_load_from_file_with_valid_file(self):
        b1 = Base(1)
        b2 = Base(2)
        Base.save_to_file([b1, b2])
        instances = Base.load_from_file()
        self.assertEqual(len(instances), 2)
        self.assertIsInstance(instances[0], Base)
        self.assertIsInstance(instances[1], Base)
        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[1].id, 2)

    def test_load_from_file_with_nonexistent_file(self):
        instances = Base.load_from_file()
        self.assertEqual(instances, [])

    def test_load_from_file_with_empty_file(self):
        with open("Base.json", "w") as file:
            file.write("")
        instances = Base.load_from_file()
        self.assertEqual(instances, [])


class TestCsvMethods(unittest.TestCase):

    def test_save_to_file_csv_with_none_list(self):
        Base.save_to_file_csv(None)
        with open("Base.csv", "r") as file:
            content = file.read()
        self.assertEqual(content, "")

    def test_save_to_file_csv_with_empty_list(self):
        Base.save_to_file_csv([])
        with open("Base.csv", "r") as file:
            content = file.read()
        self.assertEqual(content, "")

    def test_load_from_file_csv_with_nonexistent_file(self):
        instances = Base.load_from_file_csv()
        self.assertEqual(instances, [])

    def test_load_from_file_csv_with_empty_file(self):
        with open("Base.csv", "w") as file:
            file.write("")
        instances = Base.load_from_file_csv()
        self.assertEqual(instances, [])


if __name__ == "__main__":
    unittest.main()
