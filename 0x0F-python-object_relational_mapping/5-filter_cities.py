#!/usr/bin/python3

"""
Module Documentation for 5-filter_cities.py:

This module contains a Python script that interacts with a MySQL database using
SQLAlchemy ORM. It deletes states with names containing 'a' from the 'states'
table in the specified database.
"""


import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
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
    cur.execute(
        "SELECT GROUP_CONCAT(cities.name SEPARATOR ', ') \
         FROM cities \
         JOIN states ON cities.state_id = states.id \
         WHERE states.name = %s \
         ORDER BY cities.id", (sys.argv[4],))

    row = cur.fetchone()

    if row and row[0]:
        print(row[0])
    else:
        print("")

    cur.close()
    db.close()
