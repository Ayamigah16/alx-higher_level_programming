#!/usr/bin/python3
"""
Module documentation: This script connects to a MySQL server
and retrieves all cities from the 'cities' table in the specified
database, including the corresponding state name.
"""

import MySQLdb
import sys


def get_cities_by_state(username, password, db_name):
    """
    Function documentation: Retrieves and prints all cities from the
    'cities' table with the corresponding state name.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Database name.
    """
    # Connect to the database
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, passwd=password,
                           db=db_name, charset="utf8")
    cur = conn.cursor()

    # Execute the SQL query
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
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
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <db_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the function to get all cities with corresponding state names
    get_cities_by_state(username, password, db_name)
