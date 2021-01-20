'''
Contains the absolute path to the database, as well as a tuple of equipment
and exercises for the exercise GUI.
'''
import os
import sqlite3
from pathlib import Path


DB_PATH = os.path.join(
    os.path.abspath(Path( os.path.dirname(__file__) ).parent), # the adonis_lifestyle_tracker directory
    'database',
    'tracker.db'
)


def handle_get_db_path(values):
    '''Handles the event to get the absolute path to the database, for the GUIs.'''
    db_path = values['-PATH-']

    if os.path.isfile(db_path) and db_path.endswith('.db'):
        return db_path

    return None


def get_sorted_tuple(db_path, column, table):
    '''Gets a sorted tuple of the specified elements from the database.'''
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

    cursor.execute(f'SELECT {column} FROM {table}')

    elems_list = [elem[0] for elem in cursor.fetchall()]
    elems_list.sort()

    elems_tuple = tuple(elems_list)

    db.commit()
    db.close()

    return elems_tuple
