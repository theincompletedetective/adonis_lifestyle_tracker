'''Contains the handler function used for both the exercise and nutrition GUIs.'''
import sqlite3
from os.path import isfile as os_path_isfile


def get_sorted_tuple(db_path, column, table):
    '''Gets a sorted tuple of the specified elements from the database.'''
    elems_tuple = tuple()

    db = sqlite3.connect(db_path)
    cursor = db.cursor()
    cursor.execute(f'SELECT {column} FROM {table}')

    elems_tuple = tuple( sorted({elem[0] for elem in cursor.fetchall()}) )
    
    db.close()
    return elems_tuple

