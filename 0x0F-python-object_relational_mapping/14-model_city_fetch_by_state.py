#!/usr/bin/python3
"""
Script documentation: Fetches all City objects from the 'cities' table
                        grouped by state from the database 'hbtn_0e_14_usa'.
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <db_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create the engine and bind it to the session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, db_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query and print all City objects grouped by state
    cities = session.query(
        State.name,
        City.id,
        City.name).join(City).order_by(City.id).all()
    for state_name, city_id, city_name in cities:
        print("{}: ({}) {}".format(state_name, city_id, city_name))

    # Close the session
    session.close()
