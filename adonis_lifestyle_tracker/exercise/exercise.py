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


def get_exercise_from_week(week, exercise):
    '''
    Get an exercise's information from the specified week in the database.
    '''
    conn = sqlite3.connect( get_exercise_database() )
    cursor = conn.cursor()

    cursor.execute(
        '''
        SELECT week, exercise, equipment, reps_5, reps_8, reps_13, reps_21
            FROM exercise
            WHERE week == ? and exercise == ?
        ''',
        (week, exercise,)
    )

    exercise_tuple = cursor.fetchone()

    conn.commit()
    conn.close()

    return exercise_tuple


def add_exercise_to_week(
        week, exercise, equipment, reps_5=None,
        reps_8=None, reps_13=None, reps_21=None):
    '''
    Adds an exercise's name and equipment to the specified week in the database.
    '''
    conn = sqlite3.connect( get_exercise_database() )
    cursor = conn.cursor()

    cursor.execute(
        '''
        INSERT INTO exercise (
            week, exercise, equipment, reps_5, reps_8, reps_13, reps_21
        )
            VALUES (?, ?, ?, ?, ?, ?, ?);
        ''',
        (week, exercise, equipment, reps_5, reps_8, reps_13, reps_21)
    )

    conn.commit()
    conn.close()


def add_resistance(rep_range, resistance, week, exercise):
    '''
    Adds the resistance used for the specified reps of the given exercise
    to the provided week.
    '''
    conn = sqlite3.connect( get_exercise_database() )
    cursor = conn.cursor()

    cursor.execute(
        '''
        UPDATE exercise SET ? = ?
            WHERE week = ? AND exercise = ?;
        ''',
        (rep_range, resistance, week, exercise)
    )

    conn.commit()
    conn.close()
