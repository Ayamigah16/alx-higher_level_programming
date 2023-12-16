#!/usr/bin/python3
"""
Module documentation: This script connects to a MySQL server and retrieves
states from the 'states' table in the specified database whose names start
with 'N'.
"""

import MySQLdb
import sys


def filter_states_by_name(username, password, db_name):
    """
    Function documentation: Retrieves and prints states whose names start
    with 'N'.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Database name.
    """
    # Connect to the database
    conn = MySQLdb.connect(
        host="localhost", port=3306,
        user=username, passwd=password,
        db=db_name, charset="utf8")
    cur = conn.cursor()

    # Execute the SQL query
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    query_rows = cur.fetchall()

    # Print the results
    for row in query_rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    conn.close()


if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <db_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the function to filter states by name
    filter_states_by_name(username, password, db_name)
