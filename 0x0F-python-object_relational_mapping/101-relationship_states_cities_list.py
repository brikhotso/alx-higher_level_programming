#!/usr/bin/python3

"""
Module Documentation for 101-relationship_states_cities_list.py:

This module contains a Python script that interacts with a MySQL database using
SQLAlchemy ORM. Lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa.
"""


from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City
import sys

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    session.close()
