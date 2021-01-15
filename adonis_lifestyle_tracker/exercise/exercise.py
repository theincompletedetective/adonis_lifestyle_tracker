'''
Contains the functions needed to add exercises and their equipment to the exercise database,
as well as their number of repetitions and resistance they require. It also allows new weeks
to be added, to track the exercise information for each week of the program.
'''
import os
import sqlite3
from sqlite3 import IntegrityError
import click


DB_PATH = os.path.join(os.path.dirname(__file__), 'exercise.db')


@click.command()
@click.option('-ex', '--exercise', required=True, help='Name of the exercise.')
@click.option('-eq', '--equipment', required=True, help='Equipment used to perform the exercise.')
def add_exercise(exercise, equipment):
    '''
    Adds the specified exercise and equipment to the exercise table
    in the exercise database.
    '''
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute(
            'INSERT INTO exercise (id, equipment) VALUES (?, ?)',
            (exercise, equipment)
        )
    except IntegrityError:
        print(f"The '{exercise}' exercise is already in the database.")
    else:
        conn.commit()
        print(
            f"The '{exercise}' exercise and '{equipment}' equipment have "
            "been successfully added to the database."
        )
    finally:
        conn.close()


@click.command()
@click.option('-w', '--week', required=True, type=int, help='Week number.')
@click.option('-e', '--exercise', required=True, help='Name of the exercise.')
@click.option('--reps', required=True, type=int, help='Number of repetitions of a given exercise.')
@click.option('-r', '--resistance', required=True, help='Amount of resistance for a given exercise.')
def add_week(week, exercise, reps, resistance):
    '''
    Adds the specified exercise, reps, and resistance to the provided week
    in the exercise database.
    '''
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # To make sure a duplicate row doesn't exist in the database
    row_in_db = cursor.execute(
        '''
        SELECT * from week_exercise_reps_resistance
        WHERE week_id = ?
        AND exercise_id = ?
        AND reps = ?
        AND resistance = ?
        ''',
        (week, exercise, reps, resistance)
    ).fetchone()

    if row_in_db:
        print(
            f"Week {week} with the '{exercise}' exercise, '{reps}' reps, "
            f"and '{resistance}' resistance has already been added to the database."
        )
    else:
        cursor.execute(
            '''
            INSERT INTO week_exercise_reps_resistance
                (id, exercise_id, reps, resistance)
            VALUES(?, ?, ?, ?)
            ''',
            (week, exercise, reps, resistance)
        )
        conn.commit()
        print(
            f"Week {week} with the '{exercise}' exercise, '{reps}' reps, "
            f"and '{resistance}' resistance has been successfully added to the database."
        )

    conn.close()


@click.command()
@click.argument('exercise')
def get_equipment(exercise):
    '''Gets the equipment for the specified exercise in the exercise table.'''
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute( 'SELECT equipment FROM exercise WHERE id = ?', (exercise,) )

    try:
        print(cursor.fetchone()[0])
    except TypeError:
        print(f"The '{exercise}' exercise is not in the database!")
    else:
        conn.close()


@click.command()
@click.option('-w', '--week', required=True, type=int, help='Week number.')
@click.option('-e', '--exercise', required=True, help='Name of the exercise.')
@click.option('-r', '--reps', required=True, type=int, help='Number of repetitions of a given exercise.')
def get_resistance(week, exercise, reps):
    '''Gets the equipment for the specified exercise in the exercise database.'''
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        '''
        SELECT resistance
        FROM week
        WHERE id = ?
        AND exercise_id = ?
        AND reps = ?
        ''',
        (week, exercise, reps,)
    )

    try:
        print(cursor.fetchone()[0])
    except TypeError:
        print(
            f"Week {week} with the '{exercise}' exercise and {reps} reps is not in the database!"
        )
    else:
        conn.close()


@click.command()
@click.option('-w', '--week', required=True, type=int, help='Week number.')
@click.option('-e', '--exercise', required=True, help='Name of the exercise.')
@click.option('-r', '--reps', required=True, type=int, help='Number of repetitions of a given exercise.')
@click.option('-n', '--new-resistance', required=True, help='Updated amount of resistance for a given exercise.')
def update_resistance(week, exercise, reps, new_resistance):
    '''
    Updates the resistance used for the specified exercise,
    at the given rep range, for the provided week.
    '''
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # To make sure the week, exercise, and reps are already in the database
    week_in_db = cursor.execute(
        '''
        SELECT * FROM week
        WHERE id = ?
        AND exercise_id = ?
        AND reps = ?
        ''',
        (week, exercise, reps,)
    ).fetchone()

    # To make sure an identical row is not already in the database
    row_in_db = cursor.execute(
        '''
        SELECT * FROM week
        WHERE id = ?
        AND exercise_id = ?
        AND reps = ?
        AND resistance = ?
        ''',
        (week, exercise, reps, new_resistance)
    ).fetchone()

    if not week_in_db:
        print(
            f"Week {week} with the '{exercise}' exercise and {reps} reps isn't in the database."
        )
    elif row_in_db:
        print(
            f"Week {week} with the '{exercise}' exercise, {reps} reps, "
            f"and '{new_resistance}' resistance is already in the database."
        )
    else:
        cursor.execute(
            '''
            UPDATE week
            SET resistance = ?
            WHERE id = ?
            AND exercise_id = ?
            AND reps = ?
            ''',
            (new_resistance, week, exercise, reps,)
        )
        conn.commit()
        conn.close()
