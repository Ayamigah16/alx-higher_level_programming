#!/usr/bin/python3
"""
Module documentation: This script connects to a MySQL server and retrieves
all cities from the 'cities' table in the specified database for a given state.
"""

import MySQLdb
import sys


def filter_cities_by_state(username, password, db_name, state_name):
    """
    Function documentation: Retrieves and prints all cities of a
    given state from the 'cities' table.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Database name.
        state_name (str): Name of the state to filter cities.
    """
    # Connect to the database
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, passwd=password,
                           db=db_name, charset="utf8")
    cur = conn.cursor()

    # Execute the SQL query with user input using parameterized query
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cur.execute(query, (state_name,))
    # The second argument is a tuple of values

    query_rows = cur.fetchall()

    # Print the results
    if query_rows:
        result = ", ".join(row[0] for row in query_rows)
        print(result)

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

    # Call the function to filter cities by state
    filter_cities_by_state(username, password, db_name, state_name)
