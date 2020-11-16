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
import datetime

DATE_FORMAT = '%Y-%m-%d'

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

def input_expense():
    """
    Here we ask the user for his expense data,
    running simple validation checks.
    We'll leave notes as optional.
    """
    notes_input = ''
    amount_input = 0
    print("Ok, let's add an expense.")

    while True: 
        date_input = input("Please add a date for your expense (YYYY-MM-DD): ")
        try:
            date_obj = datetime.datetime.strptime(date_input, date_format)
            print(f"Date recorded as {date_obj.date()}")
            break
        except ValueError:
            print("Incorrect data format, should be YYYY-MM-DD")
            continue

    while True:
        name_input = str(input("Please add a name for your expense: "))
        if len(name_input) > 0:
            print(f"Name recorded as {name_input}")
            break
        print("Name can't be empty")

    notes_input = str(input("Please add an optional description for your expense: "))
    print(f"Description recorded as {notes_input}")

    while True:
        try:
            amount_input = float(input("Please add the amount now: "))
            print(f"Amount recorded as {amount_input}")
            break
        except ValueError:
            print("Incorrect format, it must be a number, try again.")
            continue

    return date_input, name_input, amount_input, notes_input

def input_income():
    pass

def add_income():
    pass

def input_recurring_cost():
    pass

def add_recurring_cost():
    pass

#pdb.set_trace()

connection = create_connection("budget.sqlite")
add_expense(connection, input_expense())
