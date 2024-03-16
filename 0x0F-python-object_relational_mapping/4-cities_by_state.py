#!/usr/bin/python3

"""
Module Documentation for 4-cities_by_state.py:

This module contains a Python script that interacts with a MySQL database using
SQLAlchemy ORM. It retrieves city names from cities in a state specified by
name from the 'cities' and 'states' tables in the specified database.
"""


import MySQLdb
import sys

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
        charset="utf8",
    )

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                 FROM cities JOIN states \
                 ON cities.state_id = states.id  ORDER BY cities.id")
    rows = cur.fetchall()
    for row in rows:
        city_id, city_name, state_name = row
        print(row)

    cur.close()
    db.close()
