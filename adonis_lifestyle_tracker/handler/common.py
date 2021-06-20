import os
import sqlite3
import PySimpleGUI as sg


def get_sorted_tuple(db_path, column, table):
    db = sqlite3.connect(db_path)
    cursor = db.cursor()
    cursor.execute(f'SELECT {column} FROM {table}')

    elements_tuple = tuple(sorted({elem[0] for elem in cursor.fetchall()}))

    db.close()
    return elements_tuple


def handle_load_database(window, values):
    db_path = values['-PATH-'].strip()

    if os.path.isfile(db_path) and db_path.endswith('.db'):
        window['-WEEK-'].update(values=get_sorted_tuple(db_path, 'id', 'week'))
        window['-FOOD-'].update(values=get_sorted_tuple(db_path, 'id', 'food'))
        window['-EQUIPMENT-'].update(values=get_sorted_tuple(db_path, 'id', 'equipment'))
        window['-EXERCISE-'].update(values=get_sorted_tuple(db_path, 'id', 'exercise'))
        sg.popup('The database has been successfully loaded!', title='Success')
        return db_path
    else:
        sg.popup_error('You must provide the absolute path to the database!', title='Error')
        window['-PATH-'].update('')
