'''Contains the functions needed to CRUD exercise data in the database.'''
import sqlite3
from sqlite3 import IntegrityError
import click
from adonis_lifestyle_tracker.config import Config


@click.command()
@click.option('-e', '--equipment', required=True, help='Name of the equipment used for the exercise.')
def add_equipment(equipment):
    '''Adds the specified equipment to the table in the exercise database.'''
    conn = sqlite3.connect(Config.EXERCISE_DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute( 'INSERT INTO equipment (id) VALUES (?)', (equipment,) )
    except IntegrityError:
        print(f'The equipment "{equipment}" is already in the database.')
    else:
        conn.commit()
        print(f'The equipment "{equipment}" has been successfully added to the database!')
    finally:
        conn.close()


@click.command()
@click.option('--exercise', required=True, help='Name of the exercise.')
@click.option('--equipment', required=True, help='Name of the equipment used for the exercise.')
def add_exercise(exercise, equipment):
    '''
    Adds the specified exercise and equipment to the exercise and equipment
    tables in the database.
    '''
    conn = sqlite3.connect(Config.EXERCISE_DB_PATH)
    cursor = conn.cursor()

    # TODO: Make sure that the equipment already exists in the equipment table
    cursor.execute('SELECT id from equipment WHERE id == ?', (equipment,) )

    equipment_in_db = cursor.fetchone()

    if equipment_in_db:
        try:
            cursor.execute(
                'INSERT INTO exercise (id, equipment_id) VALUES (?, ?);',
                (exercise, equipment)
            )
        except IntegrityError:
            print(f"The exercise '{exercise}' is already in the database.")
        else:
            conn.commit()
            print(
                f'The exercise "{exercise}" has been successfully added to the database, '
                f'with the equipment "{equipment}"!'
            )
    else:
        print(f"The equipment '{equipment}' is not in the database.")

    conn.close()


def get_exercise_from_week(week, exercise):
    '''
    Get an exercise's information from the specified week in the database.
    '''
    conn = sqlite3.connect(Config.EXERCISE_DB_PATH)
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
