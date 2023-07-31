#!/usr/bin/python3
"""Defines unittests for Square class."""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class."""

    def test_square_creation(self):
        """Test Square instance creation."""
        s1 = Square(5)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

    def test_square_area(self):
        """Test Square area calculation."""
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

        s2 = Square(10)
        self.assertEqual(s2.area(), 100)

    def test_square_str(self):
        """Test Square __str__ representation."""
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")

        s2 = Square(10, 2, 3)
        self.assertEqual(str(s2), "[Square] (2) 2/3 - 10")

    def test_square_update(self):
        """Test Square update method."""
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")

        s1.update(1, 20)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 20")

        s1.update(2, 10, 2)
        self.assertEqual(str(s1), "[Square] (2) 2/0 - 10")

        s1.update(3, 10, 2, 3)
        self.assertEqual(str(s1), "[Square] (3) 3/0 - 10")

    def test_square_size_getter_setter(self):
        """Test Square size getter and setter."""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

        s1.size = 10
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)

        with self.assertRaises(TypeError) as context:
            s1.size = "9"
        self.assertEqual(str(context.exception), "width must be an integer")

        with self.assertRaises(ValueError) as context:
            s1.size = 0
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_update_method(self):
        """Test the update method of the Square class."""
        s1 = Square(4, 2, 3, 5)
        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 2/3 - 4")

        s1.update(10, 5)
        self.assertEqual(str(s1), "[Square] (10) 2/3 - 5")

        s1.update(10, 5, 1)
        self.assertEqual(str(s1), "[Square] (10) 1/3 - 5")

        s1.update(10, 5, 1, 7)
        self.assertEqual(str(s1), "[Square] (10) 1/7 - 5")

        s1.update(y=10)
        self.assertEqual(str(s1), "[Square] (10) 1/10 - 5")

    def test_to_dictionary_method(self):
        """Test the to_dictionary method of the Square class."""
        s1 = Square(4, 2, 3, 5)
        s1_dict = s1.to_dictionary()
        expected_dict = {'id': 5, 'size': 4, 'x': 2, 'y': 3}
        self.assertEqual(s1_dict, expected_dict)

    def setUp(self):
        # Create an instance of Square with id=1, size=5, x=0, and y=0
        self.s1 = Square(5, 0, 0, 1)

    def test_to_csv_row(self):
        """
        Test the to_csv_row method of Square.

        This test case checks whether the to_csv_row method
        correctly returns the CSV representation
        of the Square instance. It creates a Square with id=1,
        size=5, x=0, and y=0. The expected CSV row
        string should be "1,5,0,0".
        """
        csv_row = self.s1.to_csv_row()
        expected_row = "1,5,0,0"
        self.assertEqual(csv_row, expected_row)

    def test_from_csv_row(self):
        """
        Test the from_csv_row method of Square.

        This test case checks whether the from_csv_row method
        correctly creates a new Square instance
        from the given CSV row string. It provides the CSV row
        string "1,5,0,0" which should be parsed into
        a new Square instance with id=1, size=5, x=0, and y=0.
        The new instance should be equal to the original
        instance created in setUp.
        """
        csv_row = "1,5,0,0"
        new_s1 = Square.from_csv_row(csv_row)
        self.assertEqual(self.s1.id, new_s1.id)
        self.assertEqual(self.s1.size, new_s1.size)
        self.assertEqual(self.s1.x, new_s1.x)
        self.assertEqual(self.s1.y, new_s1.y)

if __name__ == "__main__":
    unittest.main()
