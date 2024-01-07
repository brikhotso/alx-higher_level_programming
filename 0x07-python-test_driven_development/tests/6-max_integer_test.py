#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittests for the max_integer function."""

    def test_empty_list(self):
        """Test when the input list is empty."""
        result = max_integer([])
        self.assertIsNone(result)

    def test_single_element_list(self):
        """Test when the input list has a single element."""
        result = max_integer([42])
        self.assertEqual(result, 42)

    def test_positive_numbers(self):
        """Test when the input list has positive numbers."""
        result = max_integer([1, 3, 5, 2, 4])
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        """Test when the input list has negative numbers."""
        result = max_integer([-1, -3, -5, -2, -4])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        """Test when the input list has mixed positive and negative numbers."""
        result = max_integer([-1, 3, 0, -2, 4])
        self.assertEqual(result, 4)

    def test_duplicate_max_value(self):
        """Test when the input list has duplicate maximum values."""
        result = max_integer([5, 5, 5, 5])
        self.assertEqual(result, 5)

    def test_float_numbers(self):
        """Test when the input list has floating-point numbers."""
        result = max_integer([1.5, 2.5, 1.0, 2.0])
        self.assertEqual(result, 2.5)

    def test_max_at_end_of_list(self):
        """Test when the maximum value is at the end of the list."""
        result = max_integer([1, 3, 5, 2, 4, 7])
        self.assertEqual(result, 7)


if __name__ == '__main__':
    unittest.main()
