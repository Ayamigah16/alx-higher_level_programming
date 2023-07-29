#!/usr/bin/python3
"""101-stats.py is a program that reads IP logs from stdin and
prints metrics every ten lines or until EOF or Ctrl-C.
"""
import sys


def print_stats(total_size, status_counts):
    """
    Prints the statistics based on the total file size and status code counts.

    Args:
        total_size (int): The total file size.
        status_counts (dict): Dictionary containing status code counts.

    Returns:
        None
    """
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts):
        count = status_counts[status_code]
        print("{}: {}".format(status_code, count))


def parse_line(line):
    """
    Parses a log line and extracts the file size and status code.

    Args:
        line (str): The log line to parse.

    Returns:
        tuple: A tuple containing the file size and status code.
    """
    parts = line.split()
    file_size = int(parts[-1])
    status_code = int(parts[-2])
    return file_size, status_code


def calculate_stats():
    """
    Reads the standard input line by line, calculates the statistics, and prints them.

    Returns:
        None
    """
    total_size = 0
    status_counts = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            file_size, status_code = parse_line(line)
            total_size += file_size
            status_counts[status_code] = status_counts.get(status_code, 0) + 1

            if i % 10 == 0:
                print_stats(total_size, status_counts)
    except KeyboardInterrupt:
        print_stats(total_size, status_counts)


if __name__ == '__main__':
    calculate_stats()
