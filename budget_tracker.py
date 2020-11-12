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
import budget_tracker_dbsetup
import pdb

connection = budget_tracker_dbsetup.create_connection("budget.sqlite")

def add_expense(day, name, amount, notes = ''):

    query = f'''
    INSERT INTO
      expenses (day, name, amount, notes)
    VALUES
      ("{day}", "{name}", {amount}, "{notes}")
    '''
    budget_tracker_dbsetup.execute_query(connection, query)

#pdb.set_trace()

add_expense("2020-10-10", "Test", 100)
