'''
Contains the functions needed to get exercise information from the database.
'''
import sqlite3
import click
from adonis_lifestyle_tracker.config import EXERCISE_DB_PATH


@click.command()
@click.argument('exercise')
def get_equipment(exercise):
    '''Gets the equipment for the specified exercise in the database.'''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    cursor.execute( 'SELECT equipment_id FROM exercise WHERE id = ?', (exercise,) )

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
    '''Gets the resistance for the specified week, exercise, and reps, in the exercise database.'''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        '''
        SELECT resistance_id
        FROM week_exercise
        WHERE week_id = ?
        AND exercise_id = ?
        AND reps_id = ?
        ''',
        (week, exercise, reps)
    )

    try:
        print(cursor.fetchone()[0])
    except TypeError:
        print(
            f"Week {week} with the '{exercise}' exercise and {reps} reps is not in the database."
        )
    else:
        conn.close()
