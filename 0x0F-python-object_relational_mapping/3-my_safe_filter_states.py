#!/usr/bin/python3

"""
Module Documentation for 3-my_safe_filter_states.py:

This module contains a Python script that interacts with a MySQL database using
MySQLdb. It fetches a state with a specific name from the 'states' table in the
specified database using a parameterized query.
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
    cur.execute("SELECT * FROM states WHERE name = %s \
                 ORDER BY states.id", (sys.argv[4],))

    for row in cur:
        print(row)

    cur.close()
    db.close()
