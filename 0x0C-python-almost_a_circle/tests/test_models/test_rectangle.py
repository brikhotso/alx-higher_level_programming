#!/usr/bin/python3
""" tests/test_models/test_rectangle """
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_create_instance_with_id(self):
        r = Rectangle(5, 10, id=10)
        self.assertEqual(r.id, 10)

    def test_create_instance_with_zero_width(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 10)

    def test_create_instance_with_negative_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-5, 10)

    def test_create_instance_with_zero_height(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 0)

    def test_create_instance_with_negative_height(self):
        with self.assertRaises(ValueError):
            Rectangle(5, -10)

    def test_create_instance_with_negative_x_y(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -1, -2)

    def test_area(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_to_dictionary(self):
        r = Rectangle(5, 10, 2, 3, 10)
        expected_dict = {'id': 10, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        self.assertEqual(r.to_dictionary(), expected_dict)

    def test_to_str(self):
        r = Rectangle(5, 10, 2, 3, 10)
        expected_str = "[Rectangle] (10) 2/3 - 5/10"
        self.assertEqual(str(r), expected_str)

    def test_update_with_args(self):
        r = Rectangle(5, 10, 2, 3, 10)
        r.update(20, 15, 8, 4)
        self.assertEqual(r.to_dictionary(), {'id': 20, 'width': 15,
                                             'height': 8, 'x': 4, 'y': 3})

    def test_update_with_kwargs(self):
        r = Rectangle(5, 10, 2, 3, 10)
        r.update(width=15, height=8, x=4, y=1)
        self.assertEqual(r.to_dictionary(), {'id': 10, 'width': 15,
                                             'height': 8, 'x': 4, 'y': 1})

    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    unittest.main()
