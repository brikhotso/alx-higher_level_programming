#!/usr/bin/python3

"""
Module Documentation for 1-filter_states.py:

This module contains a Python script that interacts with a MySQL database using
SQLAlchemy ORM. It fetches states with names starting with 'N' from the
'states' table in the specified database.
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
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()

    for row in rows:
        if row[1][0] == "N":
            print(row)

    cur.close()
    db.close()
