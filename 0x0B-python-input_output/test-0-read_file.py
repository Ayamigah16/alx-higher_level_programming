#!/usr/bin/python3

import os
import unittest

from io import StringIO
from unittest.mock import patch

from read_file import read_file


class ReadFileTestCase(unittest.TestCase):
    def test_read_file(self):
        expected_output = "We offer a truly innovative approach to education:\n" \
                          "focus on building reliable applications and scalable systems," \
                          " take on real-world challenges, collaborate with your peers.\n" \
                          "\n" \
                          "A school every software engineer would have dreamt of!\n"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            read_file("my_file_0.txt")
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_read_file_nonexistent(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            read_file("nonexistent_file.txt")
            self.assertEqual(fake_out.getvalue(), '')

    def test_read_file_empty(self):
        with open("empty_file.txt", "w"):
            pass

        with patch('sys.stdout', new=StringIO()) as fake_out:
            read_file("empty_file.txt")
            self.assertEqual(fake_out.getvalue(), '')

        os.remove("empty_file.txt")


if __name__ == '__main__':
    unittest.main()
