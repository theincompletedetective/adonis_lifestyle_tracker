'''Contains the handler function used for both the exercise and nutrition GUIs.'''
import sqlite3
from os.path import isfile as os_path_isfile
import PySimpleGUI as sg


def get_sorted_tuple(db_path, column, table):
    '''Gets a sorted tuple of the specified elements from the database.'''
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


def handle_load_database(window, values):
    '''Handles the event to load the database from the specified file.'''
    if os_path_isfile(values['-PATH-']) and values['-PATH-'].endswith('.db'):
        db_path = values['-PATH-']

        # Nutrition info
        window['-FOOD-'].update( values=get_sorted_tuple(db_path, 'id', 'food') )
        window['-NUTRITION_WEEK-'].update( values=get_sorted_tuple(db_path, 'id', 'week') )

        # Exercise info
        window['-EQUIPMENT-'].update( values=get_sorted_tuple(db_path, 'id', 'equipment') )
        window['-EXERCISE-'].update( values=get_sorted_tuple(db_path, 'id', 'exercise') )
        window['-EXERCISE_WEEK-'].update( values=get_sorted_tuple(db_path, 'week', 'week_exercise') )
        window['-REPS-'].update( values=get_sorted_tuple(db_path, 'reps', 'week_exercise') )
        window['-RESISTANCE-'].update( values=get_sorted_tuple(db_path, 'resistance', 'week_exercise') )

        sg.popup('The database information has been successfully loaded!', title='Success')

        return db_path
    else:
        sg.popup_error(
            'You must enter the absolute path to the database file!',
            title='Error'
        )
        window['-PATH-'].update('')
