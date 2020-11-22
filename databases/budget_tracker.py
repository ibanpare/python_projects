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

def input_expinc():
    """
    Here we ask the user for his expense or income data,
    running simple validation checks.
    We'll leave notes as optional.
    """
    notes_input = ''
    amount_input = 0
    print("Ok, let's add an expense/income.")

    while True: 
        date_input = input("Please add a date for your expense/income (YYYY-MM-DD): ")
        try:
            date_obj = datetime.datetime.strptime(date_input, DATE_FORMAT)
            print(f"Date recorded as {date_obj.date()}")
            break
        except ValueError:
            print("Incorrect data format, should be YYYY-MM-DD")
            continue

    while True:
        name_input = str(input("Please add a name for your expense/income: "))
        if len(name_input) > 0:
            print(f"Name recorded as {name_input}")
            break
        print("Name can't be empty")

    notes_input = str(input("Please add an optional description for your expense/income: "))
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

def input_recurring_cost():
	"""
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  day TEXT NOT NULL,
  name TEXT NOT NULL,
  amount REAL NOT NULL,
  period TEXT NOT NULL,
  notes TEXT

  FAREI REFACTOR DELL'INPUT CON SCELTA INIZIALE DI COST/RECURRING O EXPENSE
  E RETURN DI CONSEGUENZA

  Il recurring ha tutti i campi più un periodo.
  Questo periodo potremmo farlo fisso in mesi con l'utente che setta un numero di mesi e bona.
  tra l'altro questo mi fa pensare che potrei gestire il tutto diversamente, come
  se fosse un cost normale ma facendo più insert con varie date, anche nel futuro,
  ha molto senso secondo me.
  quindi sarebbe ciclo for con incremento al mese.
  forse month iter serve qua.
	"""
    pass

def add_recurring_cost():
    """
	anche questa va un attimo ripensata visto sopra, e direi che si apre la possibilità per
	fare un'add generica, almeno per expense e income dato che cambian due cose
    """
    pass

#pdb.set_trace()

connection = create_connection("budget.sqlite")
add_expense(connection, input_expinc())
add_income(connection, input_expinc())
