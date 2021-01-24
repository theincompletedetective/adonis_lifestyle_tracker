'''
Contains the handler functions needed for both the exercise and nutrition GUIs.
'''
import os
from datetime import datetime
import sqlite3
import PySimpleGUI as sg


def get_date():
    '''Selects the date for the weekday.'''
    now = datetime.now()

    return sg.popup_get_date(
        start_mon = now.month,
        start_day = now.day,
        start_year = now.year,
        close_when_chosen = True,
    )


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


def handle_load_database(window, values):
    '''Handles the event to load the database.'''
    db_path = values['-PATH-'].strip()

    if os.path.isfile(db_path) and db_path.endswith('.db'):
        # To update the GUI with the nutrition data
        window['-WEEK-'].update(
            values=get_sorted_tuple(db_path, 'id', 'week')
        )
        window['-FOOD-'].update(
            values=get_sorted_tuple(db_path, 'id', 'food')
        )

        # To update the GUI with the exercise data
        window['-EQUIPMENT-'].update(
            values=get_sorted_tuple(db_path, 'id', 'equipment')
        )
        window['-EXERCISE-'].update(
            values=get_sorted_tuple(db_path, 'id', 'exercise')
        )

        sg.popup('The database has been successfully loaded!', title='Success')

        return db_path
    else:
        sg.popup_error(
            'You must provide the absolute path to the database!',
            title='Error'
        )
        window['-PATH-'].update('')
