#!/usr/bin/python3

"""
Module Documentation for 10-model_state_my_get.py:

This module contains a Python script that interacts with a MySQL database using
SQLAlchemy ORM. It retrieves a state with a specific name from the 'states'
table in the specified database using a custom get method.
"""


from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == sys.argv[4]).first()

    if state:
        print("{}".format(state.id,))
    else:
        print("Not found")
    session.close()
