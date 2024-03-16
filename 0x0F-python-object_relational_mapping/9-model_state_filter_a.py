#!/usr/bin/python3

"""
Module Documentation for 9-model_state_filter_a.py:

This module contains a Python script that interacts with a MySQL database using
SQLAlchemy ORM. It retrieves states with names containing 'a' from the 'states'
table in the specified database and prints their IDs and names.
"""


from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
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

    a_state = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()

    for state in a_state:
        print("{}: {}".format(state.id, state.name))

    session.close()
