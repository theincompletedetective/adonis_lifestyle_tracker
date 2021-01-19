'''
Contains the absolute path to the database, as well as a tuple of equipment
and exercises for the exercise GUI.
'''
import os
import sqlite3


DB_PATH = os.path.join(os.path.dirname(__file__), 'database', 'tracker.db')


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
