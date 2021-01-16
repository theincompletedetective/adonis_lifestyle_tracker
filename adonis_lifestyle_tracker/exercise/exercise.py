'''
Contains the functions needed to add exercise information to the database.
'''
import sqlite3
from sqlite3 import IntegrityError
import click
from adonis_lifestyle_tracker.config import EXERCISE_DB_PATH


@click.command()
@click.argument('exercise')
@click.argument('equipment')
def add_exercise(exercise, equipment):
    '''
    Adds the specified exercise and its equipment to the exercise database.
    '''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
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
            f"The '{exercise}' exercise with the '{equipment}' equipment "
            "has been successfully added to the database."
        )
    finally:
        conn.close()


@click.command()
@click.option('-w', '--week', required=True, type=int, help='Week number.')
@click.option('-e', '--exercise', required=True, help='Name of the exercise.')
@click.option('--reps', required=True, type=int, help='Number of repetitions of a given exercise.')
@click.option('-r', '--resistance', required=True, help='Amount of resistance for a given exercise.')
def add_exercise_to_week(week, exercise, reps, resistance):
    '''
    Adds the specified exercise, reps, and resistance to the provided week in the exercise database.
    '''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute(
            '''
            INSERT INTO week_exercise
                (week, exercise_id, reps, resistance)
            VALUES(?, ?, ?, ?)
            ''',
            (week, exercise, reps, resistance)
        )
    except IntegrityError:
        print(
            f"Week {week} with the '{exercise}' exercise, '{reps}' reps, "
            f"and '{resistance}' resistance is already in the the database."
        )
    else:
        conn.commit()
        print(
            f"Week {week} with the '{exercise}' exercise, '{reps}' reps, "
            f"and '{resistance}' resistance has been successfully added to the database."
        )
    finally:
        conn.close()


@click.command()
@click.argument('exercise')
def get_equipment(exercise):
    '''Gets the equipment for the specified exercise in the database.'''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    cursor.execute( 'SELECT equipment FROM exercise WHERE id = ?', (exercise,) )

    try:
        print(cursor.fetchone()[0])
    except TypeError:
        print(f"The '{exercise}' exercise is not in the database.")
    finally:
        conn.close()


@click.command()
@click.option('-w', '--week', required=True, type=int, help='Week number.')
@click.option('-e', '--exercise', required=True, help='Name of the exercise.')
@click.option('-r', '--reps', required=True, type=int, help='Number of repetitions of a given exercise.')
def get_resistance(week, exercise, reps):
    '''Gets the resistance for the specified week, exercise, and reps, in the exercise database.'''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        '''
        SELECT resistance
        FROM week_exercise
        WHERE week = ?
        AND exercise_id = ?
        AND reps = ?
        ''',
        (week, exercise, reps)
    )

    try:
        print(cursor.fetchone()[0])
    except TypeError:
        print(
            f"Week {week} with the '{exercise}' exercise and {reps} reps is not in the database."
        )
    finally:
        conn.close()


@click.command()
@click.option('-w', '--week', required=True, type=int, help='Week number.')
@click.option('-e', '--exercise', required=True, help='Name of the exercise.')
@click.option('-r', '--reps', required=True, type=int, help='Number of repetitions of a given exercise.')
@click.option('-n', '--new-resistance', required=True, help='Updated amount of resistance for a given exercise.')
def change_resistance(week, exercise, reps, new_resistance):
    '''
    Changes the resistance used for the specified exercise, at the given rep range, for the provided week.
    '''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute(
            '''
            UPDATE week_exercise
            SET resistance = ?
            WHERE week = ?
            AND exercise_id = ?
            AND reps = ?
            ''',
            (new_resistance, week, exercise, reps)
        )
    except IntegrityError:
        print(
            f"Week {week}, the '{exercise}' exercise, and {reps} reps are not in the database."
        )
    else:
        conn.commit()
        print(
            f"The resistance for week {week}, the '{exercise}' exercise, "
            f"and {reps} reps has been successfully updated to {new_resistance}."
        )
    finally:
        conn.close()
