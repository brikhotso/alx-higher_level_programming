#!/usr/bin/python3

"""
Module Documentation for relationship_city.py:

This module defines the City class using SQLAlchemy ORM for mapping to the
'cities' table in the database.
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Define class City Base"""

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
