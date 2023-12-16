#!/usr/bin/python3
"""
Module documentation: Prints the id of the State object with
the given name from the 'states' table in the database.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <db_name> <state_name>".format(
            sys.argv[0]))
        sys.exit(1)

    # Get arguments
    username, password, db_name, state_name = (sys.argv[1], sys.argv[2],
                                               sys.argv[3], sys.argv[4])

    # Create the engine and bind it to the session
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, db_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query State object by name and print the result
    state = session.query(State).filter(State.name == state_name).first()
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
