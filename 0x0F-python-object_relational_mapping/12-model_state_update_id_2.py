#!/usr/bin/python3
"""
Module documentation: Changes the name of a State object with id=2
                        in the 'states' table to "New Mexico".
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print(
            "Usage: {} <username> <password> <db_name>".format(
                sys.argv[0]))
        sys.exit(1)

    # Get arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create the engine and bind it to the session
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, db_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query and update the State object with id=2
    state_to_update = session.query(State).filter_by(id=2).first()
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
