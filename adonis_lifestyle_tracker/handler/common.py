'''Contains the handler function used for both the exercise and nutrition GUIs.'''
import sqlite3
from os.path import isfile as os_path_isfile


def get_sorted_tuple(db_path, column, table):
    '''Gets a sorted tuple of the specified elements from the database.'''
    if os_path_isfile(db_path) and db_path.endswith('.db'):
        db = sqlite3.connect(db_path)
        cursor = db.cursor()

        cursor.execute(f'SELECT {column} FROM {table}')

        elems_list = [elem[0] for elem in cursor.fetchall()]
        elems_list.sort()

        elems_set = set(elems_list)

        elems_tuple = tuple(elems_set)

        db.commit()
        db.close()

        return elems_tuple
    else:
        return tuple()
