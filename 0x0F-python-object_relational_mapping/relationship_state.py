#!/usr/bin/python3

"""
Module Documentation for relationship_state.py:

This module defines the State class using SQLAlchemy ORM for mapping to the
'states' table in the database.
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import City, Base


class State(Base):
    """ Describe clase State Base"""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
