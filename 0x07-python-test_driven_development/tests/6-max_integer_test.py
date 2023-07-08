import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Test case class for the max_integer function.
    """

    def test_max_integer_positive(self):
        """
        Test the max_integer function with a list of positive integers.
        """
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_max_integer_unsorted(self):
        """
        Test the max_integer function with an unsorted list of integers.
        """
        result = max_integer([1, 3, 4, 2])
        self.assertEqual(result, 4)
