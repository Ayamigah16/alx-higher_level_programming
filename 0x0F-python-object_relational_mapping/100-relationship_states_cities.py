#!/usr/bin/python3
"""
Script documentation: Creates the State “California” with
the City “San Francisco" in the database 'hbtn_0e_100_usa'.
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <db_name>".format(
            sys.argv[0]))
        sys.exit(1)

    # Get arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create the engine and bind it to the session
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, db_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Create a new State and City
    california = State(name="California",
                       cities=[City(name="San Francisco")])

    # Add to the session and commit
    session.add(california)
    session.commit()

    # Close the session
    session.close()
