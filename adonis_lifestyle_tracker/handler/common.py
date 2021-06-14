'''
Contains the handler functions needed for both the exercise and nutrition GUIs.
'''
import sqlite3


def get_sorted_tuple(db_path, column, table):
    '''
    Gets an alphabetically or numerically sorted tuple of the
    specified elements from the database.
    '''
    elems_tuple = tuple()

    db = sqlite3.connect(db_path)
    cursor = db.cursor()
    cursor.execute(f'SELECT {column} FROM {table}')

    elems_tuple = tuple( sorted({elem[0] for elem in cursor.fetchall()}) )

    db.close()
    return elems_tuple
