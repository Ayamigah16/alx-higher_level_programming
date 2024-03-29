#!/usr/bin/python3
"""
tests/test_models/test_base.py
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_single_instance(self):
        """Test creating a single instance of Base class."""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_multiple_instances(self):
        """Test creating multiple instances of Base class."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_custom_id(self):
        """Test creating a Base instance with a custom id."""
        b1 = Base(10)
        self.assertEqual(b1.id, 10)

    def test_non_integer_id(self):
        """Test creating a Base instance with a non-integer id."""
        with self.assertRaises(TypeError):
            Base('invalid_id')

    def test_zero_id(self):
        """Test creating a Base instance with id = 0."""
        with self.assertRaises(ValueError):
            Base(0)


if __name__ == '__main__':
    unittest.main()
