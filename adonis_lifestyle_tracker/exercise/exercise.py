'''Contains the functions needed to CRUD exercise data in the database.'''
import sqlite3
import PySimpleGUI as sg
from adonis_lifestyle_tracker.config import Config


def get_exercise_database():
    '''
    Allows the user to select the exercise database to use for
    all CRUD operations.
    '''
    sg.theme('Reddit')

    layout = [
        [sg.Text('Please select the exercise database:')],
        [sg.Input(key='-EXERCISE-'), sg.FileBrowse()],
        [
            sg.Submit(button_color=Config.SUBMIT_BUTTON_COLOR),
            sg.Cancel(button_color=Config.CANCEL_BUTTON_COLOR)
        ]
    ]

    window = sg.Window('Exercise Database Selector', layout)
    event, values = window.read()
    window.close()
    return values['-EXERCISE-']


def get_cursor(db):
    '''Gets the cursor which allows changes to be made to the database.'''
    conn = sqlite3.connect(db)
    return conn.cursor()


def add_exercise(exercise, equipment, database_path=None):
    '''
    Adds the specified exercise and equipment to the exercise and equipment
    tables in the database.
    '''
    if database_path:
        conn = sqlite3.connect(database_path)
    else:
        conn = sqlite3.connect( get_exercise_database() )

    cursor = conn.cursor()

    # To make sure equipment isn't already in database
    try:
        equipment_id = cursor.execute(
            'SELECT id from equipment where id = ?', (equipment,)
        ).fetchone()[0]
    except TypeError:
        cursor.execute( 'INSERT INTO equipment (id) VALUES (?)', (equipment,) )
        equipment_id = equipment

    cursor.execute(
        '''
        INSERT INTO exercise (id, equipment_id) VALUES (?, ?);
        ''',
        (exercise, equipment_id,)
    )

    conn.commit()
    conn.close()


def get_exercise_from_week(week, exercise):
    '''
    Get an exercise's information from the specified week in the database.
    '''
    conn = sqlite3.connect( get_exercise_database() )
    cursor = conn.cursor()

    cursor.execute(
        'SELECT * FROM week WHERE id == ? AND exercise_id == ?',
        (week, exercise,)
    )

    week_tuple = cursor.fetchone()

    cursor.execute( 'SELECT equipment FROM exercise WHERE id = ?', (exercise,) )

    equipment_tuple = cursor.fetchone()

    conn.commit()
    conn.close()

    return (*week_tuple, *equipment_tuple,)


def add_exercise_to_week(
        week, exercise, reps_5=None,
        reps_8=None, reps_13=None, reps_21=None):
    '''
    Adds an exercise's id to the specified week in the database.
    '''
    conn = sqlite3.connect( get_exercise_database() )
    cursor = conn.cursor()

    cursor.execute(
        '''
        INSERT INTO week (
            id, exercise_id, reps_5, reps_8, reps_13, reps_21
        )
            VALUES (?, ?, ?, ?, ?, ?);
        ''',
        (week, exercise, reps_5, reps_8, reps_13, reps_21,)
    )

    conn.commit()
    conn.close()


def add_resistance_to_week(rep_range, resistance, week, exercise):
    '''
    Adds the resistance used for the specified reps of the given exercise
    to the provided week.
    '''
    conn = sqlite3.connect( get_exercise_database() )
    cursor = conn.cursor()

    cursor.execute(
        '''
        UPDATE week SET ? = ? WHERE id = ? AND exercise_id = ?;
        ''',
        (rep_range, resistance, week, exercise,)
    )

    conn.commit()
    conn.close()
