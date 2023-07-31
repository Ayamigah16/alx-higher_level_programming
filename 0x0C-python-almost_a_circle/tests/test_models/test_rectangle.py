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

    def test_area(self):
        """Test the area method of Rectangle."""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        """Test the display method of Rectangle."""
        r1 = Rectangle(2, 3, 2, 2)
        r1_expected_output = "\n\n  ##\n  ##\n  ##\n"
        self.assertOutput(r1.display, r1_expected_output)

        r2 = Rectangle(3, 2, 1, 0)
        r2_expected_output = " ###\n ###\n"
        self.assertOutput(r2.display, r2_expected_output)

    # Helper method to capture stdout output for testing
    def assertOutput(self, func, expected_output):
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output
        func()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
