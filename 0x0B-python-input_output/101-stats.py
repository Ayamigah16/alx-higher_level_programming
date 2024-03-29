#!/usr/bin/python3
"""101-stats.py is a program that reads IP logs from stdin and
prints metrics every ten lines or until EOF or Ctrl-C.
"""

import sys


def print_stats(status_codes, total_size):
    """
    Print the computed statistics.

    Args:
        status_codes (dict): Dictionary containing status codes
    and their counts.
        total_size (int): Total file size.
    """
    print("File size: {}".format(total_size))
    for status_code in sorted(status_codes.keys()):
        if status_codes[status_code] > 0:
            print("{}: {}".format(
                status_code, status_codes[status_code]))


def parse_line(line):
    """
    Parse a single line of log and extract status code and file size.

    Args:
        line (str): A line of log.

    Returns:
        tuple: A tuple containing the status code (int)
    and file size (int).
    """
    split_line = line.split()
    status_code = split_line[-2]
    file_size = split_line[-1]
    return int(status_code), int(file_size)


def main():
    """
    Main function to compute and print the statistics.
    """
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}
    total_size = 0
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            status_code, file_size = parse_line(line)

            if status_code in status_codes:
                status_codes[status_code] += 1

            total_size += file_size
            line_count += 1

            if line_count % 10 == 0:
                print_stats(status_codes, total_size)

    except KeyboardInterrupt:
        print_stats(status_codes, total_size)
        raise


if __name__ == "__main__":
    if not sys.stdin.isatty():
        main()
