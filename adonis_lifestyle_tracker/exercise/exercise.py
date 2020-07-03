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


def get_exercise_from_week(exercise, week):
    '''
    Get an exercise's information from the specified week in the database.
    '''
    conn = sqlite3.connect( get_exercise_database() )
    cursor = conn.cursor()

    cursor.execute(
        '''
        SELECT exercise_name, equipment, reps_5, reps_8, reps_13, reps_21
            FROM week
            WHERE exercise_name == ? and id == ?
        ''',
        (exercise, week,)
    )

    exercise_tuple = cursor.fetchone()

    conn.commit()
    conn.close()

    return exercise_tuple


def add_exercise_to_week(week, exercise, equipment):
    '''
    Adds an exercise's name and equipment to the specified week in the database.
    '''
    conn = sqlite3.connect( get_exercise_database() )
    cursor = conn.cursor()

    cursor.execute(
        '''
        INSERT INTO week (
            id, exercise_name, equipment
        )
            VALUES (?, ?, ?);
        ''',
        (week, exercise, equipment)
    )

    conn.commit()
    conn.close()


def add_5_reps_resistance(week, exercise, resistance):
    '''
    Adds the resistance used for five reps of the given exercise
    to the specified week.
    '''


def add_8_reps_resistance(week, exercise, resistance):
    '''
    Adds the resistance used for eight reps of the given exercise
    to the specified week.
    '''


def add_13_reps_resistance(week, exercise, resistance):
   '''
    Adds the resistance used for 13 reps of the given exercise
    to the specified week.
    '''


def add_21_reps_resistance(week, exercise, resistance):
    '''
    Adds the resistance used for 13 reps of the given exercise
    to the specified week.
    '''


def add_week(week_num):
    '''Adds a week to the week database table.'''
    conn = sqlite3.connect('exercise.db')
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO week (id) VALUES (?);", (week_num,)
    )

    conn.commit()
    conn.close()


def add_exercise_to_week(exercise, week):
    '''Adds an exercise to a given week.'''
    conn = sqlite3.connect('exercise.db')
    cursor = conn.cursor()

    # To get the ID for the provided exercise
    cursor.execute(
        "SELECT id FROM exercise WHERE exercise_name == ?;", (exercise,)
    )

    # To add the exercise's ID to the exercise_week relation table
    cursor.execute(
        '''
        INSERT INTO exercise_week (exercise_id, week_id)
            VALUES (?, ?);
        ''',
        (cursor.fetchone()[0], week)
    )

    conn.commit()
    conn.close()
