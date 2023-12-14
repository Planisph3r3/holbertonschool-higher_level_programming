#!/usr/bin/python3
"""
Fetching/Getting all states using MySQLdb
"""


import MySQLdb
import sys


def main():
    """
    Connects to a MySQL database and excecute a select
    query then print the result.
    It uses arguments sent by the user on prompt
    """

    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        password=sys.argv[2],
        port=3306,
        database=sys.argv[3],
    )
    r = db.cursor()
    r.execute("SELECT * FROM states ORDER BY id ASC")
    rows = r.fetchall()

    for row in rows:
        print(row)

    r.close()
    db.close()


if __name__ == "__main__":
    """
    Execution Guardian
    """
    main()
