'''
Contains the handler functions needed for both the exercise and nutrition GUIs.
'''
import os
import sqlite3
from datetime import datetime
import PySimpleGUI as sg


def get_date():
    '''Gets the specified day, using the PySimpleGUI date-picker.'''
    now = datetime.now()

    month, day, year = sg.popup_get_date(
        start_mon = now.month,
        start_day = now.day,
        start_year = now.year,
        close_when_chosen = True,
    )

    return f'{month}-{day}-{year}'


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
        window['-NUTRITION_WEEK-'].update(
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
        window['-EXERCISE_WEEK-'].update(
            values=get_sorted_tuple(db_path, 'week', 'week_exercise')
        )
        window['-REPS-'].update(
            values=get_sorted_tuple(db_path, 'reps', 'week_exercise')
        )
        window['-RESISTANCE-'].update(
            values=get_sorted_tuple(db_path, 'resistance', 'week_exercise')
        )

        sg.popup('The database has been successfully loaded!', title='Success')

        return db_path
    else:
        sg.popup_error(
            'You must provide the absolute path to the database!',
            title='Error'
        )
        window['-PATH-'].update('')
