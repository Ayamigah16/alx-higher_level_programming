#!/usr/bin/python3
"""
Module documentation: This script connects to a MySQL server and retrieves
states from the 'states' table in the specified database based on user input.
"""

import MySQLdb
import sys


def filter_states_by_user_input(username, password, db_name, state_name):
    """
    Function documentation: Retrieves and prints states based on user input.
    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Database name.
        state_name (str): State name to search for.
    """
    # Connect to the database
    conn = MySQLdb.connect(
        host="localhost", port=3306,
        user=username, passwd=password,
        db=db_name, charset="utf8")
    cur = conn.cursor()

    # Execute the SQL query with user input
    query = "SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC".format(
        state_name)
    cur.execute(query)
    query_rows = cur.fetchall()

    # Print the results
    for row in query_rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    conn.close()


if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <db_name> <state_name>".format(
            sys.argv[0]))
        sys.exit(1)

    # Get arguments
    username, password, db_name, state_name = (sys.argv[1], sys.argv[2],
                                               sys.argv[3], sys.argv[4])

    # Call the function to filter states by user input
    filter_states_by_user_input(username, password, db_name, state_name)
