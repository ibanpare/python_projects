"""
Write an application that keeps track of a household’s budget.
The user can add expenses, income, and recurring costs to find out
how much they are saving or losing over a period of time.

Optional: Allow the user to specify a date range and
see the net flow of money in and out of the house budget for that time period.

TEXT as ISO8601 strings ("YYYY-MM-DD HH:MM:SS.SSS").

fields = "field1, field2, field3, field4"
table = "table"
conditions = "condition1=1 AND condition2=2"

sql = (f"SELECT {fields} "
       f"FROM {table} "
       f"WHERE {conditions};")
"""

import sqlite3
from sqlite3 import Error
import pdb

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def add_expense(connection, expense):
    """ adds an expense with parameterized query
    :param connection: database connection
    :param expense: expense data
    """
    query = '''
    INSERT INTO
      expenses (day, name, amount, notes)
    VALUES
      (?, ?, ?, ?)
    '''
    cur = connection.cursor()
    cur.execute(query, expense)
    connection.commit()
    print("New expense added!")

#pdb.set_trace()

connection = create_connection("budget.sqlite")
add_expense(connection, ("2020-10-10", "Test", 100, "DEFAULT"))
