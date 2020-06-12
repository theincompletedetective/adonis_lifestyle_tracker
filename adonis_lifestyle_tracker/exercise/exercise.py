'''Contains the functions needed to CRUD exercise data in the database.'''

import sqlite3


def get_exercise(name):
    '''Get an exercise's information from the database.'''
    conn = sqlite3.connect('exercise.db')
    cursor = conn.cursor()

    cursor.execute(
        '''
        SELECT id, equipment, reps_5, reps_8, reps_13, reps_21 FROM exercise
            WHERE exercise_name == ?
        ''',
        (name,)
    )

    exercise_tuple = cursor.fetchone()

    conn.commit()
    conn.close()

    return exercise_tuple


def add_exercise(name, equipment):
    '''Adds an exercise to the database.'''
    conn = sqlite3.connect('exercise.db')
    cursor = conn.cursor()

    cursor.execute(
        '''
        INSERT INTO exercise (exercise_name, equipment)
            VALUES (?, ?);
        ''',
        (name, equipment)
    )

    conn.commit()
    conn.close()


def add_5_reps_resistance(exercise, resistance):
    '''Adds the resistance used for five reps of the given exercise.'''


def add_8_reps_resistance(exercise, resistance):
    '''Adds the resistance used for eight reps of the given exercise.'''


def add_13_reps_resistance(exercise, resistance):
    '''Adds the resistance used for 13 reps of the given exercise.'''


def add_21_reps_resistance(exercise, resistance):
    '''Adds the resistance used for 21 reps of the given exercise.'''


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
    conn = sqlite3.connect('nutrition.db')
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