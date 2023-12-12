#!/usr/bin/python3
"""Connects to a MySQL database and excecute a select query then print the result. It uses arguments sent by the user on prompt"""
import MySQLdb
import sys
def main():
    
    db = MySQLdb.connect(host=localhost, port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    cur.execute("SELECT * from states ORDER BY id ASC")

    rows = cur.fetchall()

    for row in rows:
        for col in row:
            print("{}".format(col))

    cur.close()
    db.close()

if __name__ == "__main__":
    main()