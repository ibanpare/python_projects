"""
Write an application that keeps track of a household’s budget.
The user can add expenses, income, and recurring costs to find out
how much they are saving or losing over a period of time.

Optional: Allow the user to specify a date range and
see the net flow of money in and out of the house budget for that time period.

TODO:
generalizzare di brutto
recurring costs nel report
probabilmente spostare le funzioni in altro file e qui mettere runtime

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

def input_record():
    """
    Here we ask the user for his record data,
    running simple validation checks.
    Notes are optional.
    We can accept income data, expense data or recurring cost data.
    """
    notes_input = ''
    amount_input = 0
    print("Ok, let's add a record")

    #Recurring cost check
    recurring = input("Is your record a recurring cost (Y or N)? ")
    if recurring == "Y":
        period = int(input("How long for will that expense happen (indicate monts)? "))

    #date input
    while True: 
        date_input = input("Please add a date for your record (YYYY-MM-DD): ")
        try:
            date_obj = datetime.datetime.strptime(date_input, DATE_FORMAT)
            print(f"Date recorded as {date_obj.date()}")
            break
        except ValueError:
            print("Incorrect data format, should be YYYY-MM-DD")
            continue

    #name input
    while True:
        name_input = str(input("Please add a name for your record: "))
        if len(name_input) > 0:
            print(f"Name recorded as {name_input}")
            break
        print("Name can't be empty")

    #optional notes input
    notes_input = str(input("Please add an optional description for your record: "))
    print(f"Description recorded as {notes_input}")

    #amount input
    while True:
        try:
            amount_input = float(input("Please add the amount now: "))
            print(f"Amount recorded as {amount_input}")
            break
        except ValueError:
            print("Incorrect format, it must be a number, try again.")
            continue

    if recurring == "Y": 
        return date_input, name_input, amount_input, period, notes_input

    return date_input, name_input, amount_input, notes_input

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

def add_income(connection, income):
    """ adds an income with parameterized query
    :param connection: database connection
    :param expense: expense data
    """
    query = '''
    INSERT INTO
      income (day, name, amount, notes)
    VALUES
      (?, ?, ?, ?)
    '''
    cur = connection.cursor()
    cur.execute(query, income)
    connection.commit()
    print("New income added!")

def add_recurring_cost(connection, reccost):
    """ 
    adds a recurring cost
    """

    query = '''
    INSERT INTO
      recurring_costs (day, name, amount, period, notes)
    VALUES
      (?, ?, ?, ?, ?)
    '''
    cur = connection.cursor()
    cur.execute(query, reccost)
    connection.commit()
    print("New recurring cost added!")

def get_report(connection):
    """ 
    gets net flow of money in and out of the house
    for specified time perido
    """

    while True: 
        start_date = input("Please add a start date for your report (YYYY-MM-DD): ")
        end_date = input("Please add an end date for your report (YYYY-MM-DD): ")
        try:
            start_date_obj = datetime.datetime.strptime(start_date, DATE_FORMAT)
            end_date_obj = datetime.datetime.strptime(end_date, DATE_FORMAT)
            print(f"Start date recorded as {start_date_obj.date()}")
            print(f"Start date recorded as {end_date_obj.date()}")
            break
        except ValueError:
            print("Incorrect data format, should be YYYY-MM-DD")
            continue

    expense_query = '''
    SELECT amount 
    FROM expenses
    WHERE day > ? AND day < ?
    '''
    cur = connection.cursor()
    cur.execute(expense_query, (start_date, end_date))
    result = cur.fetchall()
    total_expenses = 0
    for expense in result:
        total_expenses += expense[0]
    connection.commit()

    income_query = '''
    SELECT amount 
    FROM income
    WHERE day > ? AND day < ?
    '''
    cur = connection.cursor()
    cur.execute(income_query, (start_date, end_date))
    result = cur.fetchall()
    total_income = 0
    for income in result:
        total_income += income[0]
    connection.commit()

    print(f"Total expenses for the time period were {total_expenses}")
    print(f"Total income for the time period was {total_income}")
    print(f"Net income for the time period is {total_income - total_expenses}")

#pdb.set_trace()

connection = create_connection("budget.sqlite")
#add_recurring_cost(connection, input_record())
#add_expense(connection, input_record())
get_report(connection)