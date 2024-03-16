#!/usr/bin/python3

"""
Module Documentation for 0-select_states.py:

This module contains a Python script that interacts with a MySQL database using
MySQLdb. It fetches all rows from the 'states' table in the specified database
and prints them.
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
    cur.execute("SELECT * FROM states ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
