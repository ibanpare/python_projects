"""
Setup for budget_tracker.py, creating tables and defining db functions
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

if __name__ == '__main__':
    connection = create_connection("budget.sqlite")
    execute_query(connection, create_expenses_table)
    execute_query(connection, create_income_table)
    execute_query(connection, create_recurring_costs_table)
