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

    def test_update_no_keyword(self):
        """Test the update method with no-keyword arguments."""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")

        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")

        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_with_keyword(self):
        """Test the update method with key-worded arguments."""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(width=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 1/10")

        r1.update(x=2, width=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/10 - 1/10")

        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/10")

        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")

    def test_update_with_both_args_and_kwargs(self):
        """Test the update method with both no-keyword and key-worded arguments."""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

        r1.update(89, width=1)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 1/3")

        r1.update(y=1, width=2, x=3)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/3")

        r1.update(x=1, height=2, y=3)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 2/3")

    def test_to_dictionary(self):
        """Test the to_dictionary method of the Rectangle class."""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dict = r1.to_dictionary()
        expected_dict = {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(r1_dict, expected_dict)

        r2 = Rectangle(1, 1)
        r2.update(**r1_dict)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/9 - 10")

    def setUp(self):
        """ Create an instance of Rectangle with id=1,
        width=10, height=5, x=0, and y=0"""
        self.r1 = Rectangle(10, 5, 0, 0, 1)

    def test_to_csv_row(self):
        """
        Test the to_csv_row method of Rectangle.

        This test case checks whether the to_csv_row method
        correctly returns the CSV representation
        of the Rectangle instance. It creates a Rectangle with id=1,
        width=10, height=5, x=0, and y=0.
        The expected CSV row string should be "1,10,0,0".
        """
        csv_row = self.r1.to_csv_row()
        expected_row = "1,10,0,0"
        self.assertEqual(csv_row, expected_row)

    def test_from_csv_row(self):
        """
        Test the from_csv_row method of Rectangle.

        This test case checks whether the from_csv_row method
        correctly creates a new Rectangle instance
        from the given CSV row string. It provides the CSV row
        string "1,10,0,0" which should be parsed into
        a new Rectangle instance with id=1, width=10, height=5,
        x=0, and y=0. The new instance should be equal
        to the original instance created in setUp.
        """
        csv_row = "1,10,0,0"
        new_r1 = Rectangle.from_csv_row(csv_row)
        self.assertEqual(self.r1.id, new_r1.id)
        self.assertEqual(self.r1.width, new_r1.width)
        self.assertEqual(self.r1.height, new_r1.height)
        self.assertEqual(self.r1.x, new_r1.x)
        self.assertEqual(self.r1.y, new_r1.y)

if __name__ == '__main__':
    unittest.main()
