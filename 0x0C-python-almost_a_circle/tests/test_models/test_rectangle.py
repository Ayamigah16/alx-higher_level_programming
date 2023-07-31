#!/usr/bin/python3
"""
tests/test_models/test_rectangle.py
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_default_values(self):
        """Test creating a Rectangle instance with default values."""
        r1 = Rectangle(10, 5)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_custom_values(self):
        """Test creating a Rectangle instance with custom values."""
        r1 = Rectangle(10, 5, 2, 3, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.id, 1)

    def test_non_integer_width(self):
        """Test creating a Rectangle instance with a non-integer width."""
        with self.assertRaises(TypeError):
            Rectangle('invalid_width', 5)

    def test_negative_width(self):
        """Test creating a Rectangle instance with a negative width."""
        with self.assertRaises(ValueError):
            Rectangle(-10, 5)

    def test_non_integer_height(self):
        """Test creating a Rectangle instance with a non-integer height."""
        with self.assertRaises(TypeError):
            Rectangle(10, 'invalid_height')

    def test_negative_height(self):
        """Test creating a Rectangle instance with a negative height."""
        with self.assertRaises(ValueError):
            Rectangle(10, -5)

    def test_non_integer_x(self):
        """Test creating a Rectangle instance with a non-integer x-coordinate."""
        with self.assertRaises(TypeError):
            Rectangle(10, 5, 'invalid_x', 3)

    def test_negative_x(self):
        """Test creating a Rectangle instance with a negative x-coordinate."""
        with self.assertRaises(ValueError):
            Rectangle(10, 5, -2, 3)

    def test_non_integer_y(self):
        """Test creating a Rectangle instance with a non-integer y-coordinate."""
        with self.assertRaises(TypeError):
            Rectangle(10, 5, 2, 'invalid_y')

    def test_negative_y(self):
        """Test creating a Rectangle instance with a negative y-coordinate."""
        with self.assertRaises(ValueError):
            Rectangle(10, 5, 2, -3)


if __name__ == '__main__':
    unittest.main()
