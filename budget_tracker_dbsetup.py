"""
Write an application that keeps track of a household’s budget.
The user can add expenses, income, and recurring costs to find out
how much they are saving or losing over a period of time.

Optional: Allow the user to specify a date range and
see the net flow of money in and out of the house budget for that time period.

TEXT as ISO8601 strings ("YYYY-MM-DD HH:MM:SS.SSS").
"""

import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
        
create_expenses_table = """
CREATE TABLE IF NOT EXISTS expenses (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  day TEXT NOT NULL,
  name TEXT NOT NULL,
  amount REAL NOT NULL,
  notes TEXT
);
"""

create_income_table = """
CREATE TABLE IF NOT EXISTS income (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  day TEXT NOT NULL,
  name TEXT NOT NULL,
  amount REAL NOT NULL,
  notes TEXT
);
"""

create_recurring_costs_table = """
CREATE TABLE IF NOT EXISTS recurring_costs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  day TEXT NOT NULL,
  name TEXT NOT NULL,
  amount REAL NOT NULL,
  period TEXT NOT NULL,
  notes TEXT
);
"""

connection = create_connection("budget.sqlite")

execute_query(connection, create_expenses_table)
execute_query(connection, create_income_table)  
execute_query(connection, create_recurring_costs_table)  
