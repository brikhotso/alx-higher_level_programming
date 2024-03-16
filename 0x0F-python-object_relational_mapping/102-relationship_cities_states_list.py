#!/usr/bin/python3

"""
Module Documentation for 102-relationship_cities_states_list.py:

This module contains a Python script that interacts with a MySQL database using
SQLAlchemy ORM. Lists all City objects from the database hbtn_0e_101_usa.
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

    for city in session.query(City).order_by(City.id):
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
