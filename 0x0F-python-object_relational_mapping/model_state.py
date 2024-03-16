#!/usr/bin/python3

"""
Module Documentation for model_state.py:

This module defines the State class using SQLAlchemy ORM for mapping to the
'states' table in the database.
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ Describe clase State Base"""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
