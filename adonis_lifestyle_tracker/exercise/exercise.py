'''Contains the functions needed to CRUD exercise data in the database.'''
import sqlite3
from sqlite3 import IntegrityError
import click
from adonis_lifestyle_tracker.config import Config


@click.command()
@click.option('-e', '--exercise', required=True, help='Name of the exercise.')
@click.option('-t', '--tool', required=True, help='Equipment used to perform the exercise.')
def add_exercise(exercise, tool):
    '''Adds the specified exercise and equipment to the exercise table in the exercise database.'''
    conn = sqlite3.connect(Config.EXERCISE_DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute(
            'INSERT INTO exercise (id, tool) VALUES (?, ?)',
            (exercise, tool)
        )
    except IntegrityError:
        print(f"'{exercise}' exercise is already in the database!")
    else:
        conn.commit()
        print(
            f"'{exercise}' exercise with '{tool}' equipment has "
            "been successfully added to the database!"
        )
    finally:
        conn.close()


@click.command()
@click.argument('reps')
def add_reps(reps):
    '''Adds the specified number of reps to the exercise database.'''
    conn = sqlite3.connect(Config.EXERCISE_DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute( 'INSERT INTO reps (id) VALUES (?)', (reps,) )
    except IntegrityError:
        print(f'{reps} reps is already in the database.')
    else:
        conn.commit()
        print(f'{reps} reps has been successfully added to the database.')
    finally:
        conn.close()


@click.command()
@click.argument('resistance')
def add_resistance(resistance):
    '''Adds the specified amount of resistance to the exercise database.'''
    conn = sqlite3.connect(Config.EXERCISE_DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute( 'INSERT INTO resistance (id) VALUES (?)', (resistance,) )
    except IntegrityError:
        print(f'"{resistance}" resistance is already in the database.')
    else:
        conn.commit()
        print(f'"{resistance}" resistance has been successfully added to the database.')
    finally:
        conn.close()


@click.command()
@click.option('-w', '--week', required=True, type=int, help='Week number.')
@click.option('-e', '--exercise', required=True, help='Name of the exercise.')
@click.option('--reps', required=True, type=int, help='Number of repetitions of a given exercise.')
@click.option('-r', '--resistance', required=True, help='Amount of resistance for a given exercise.')
def add_week(week, exercise, reps, resistance):
    '''Adds the specified exercise, reps, and resistance to the provided week.'''
    conn = sqlite3.connect(Config.EXERCISE_DB_PATH)
    cursor = conn.cursor()

    # To make sure the exercise, reps, and resistance are in the database
    exercise_in_db = cursor.execute( 'SELECT * from exercise where id = ?', (exercise,) ).fetchone()
    reps_in_db = cursor.execute( 'SELECT * from reps where id = ?', (reps,) ).fetchone()
    resistance_in_db = cursor.execute( 'SELECT * from resistance where id = ?', (resistance,) ).fetchone()

    # To make sure a duplicate row doesn't exist in the database
    duplicate_row_in_db = cursor.execute(
        '''
        SELECT * from week
        WHERE week_id = ?
        AND exercise_id = ?
        AND reps_id = ?
        AND resistance_id = ?
        ''',
        (week, exercise, reps, resistance)
    ).fetchone()

    if not exercise_in_db:
        print(f"'{exercise}' exercise is not in the database.")
    elif not reps_in_db:
        print(f"{reps} reps is not in the database.")
    elif not resistance_in_db:
        print(f"'{resistance}' resistance is not in the database.")
    if duplicate_row_in_db:
        print(
            f"Week number {week} with '{exercise}' exercise, '{reps}' reps, "
            f"and '{resistance}' resistance has already been added to the database."
        )
    else:
        cursor.execute(
            '''
            INSERT INTO week (week_id, exercise_id, reps_id, resistance_id)
            VALUES(?, ?, ?, ?)
            ''',
            (week, exercise, reps, resistance)
        )
        conn.commit()
        print(
            f"Week number {week} with '{exercise}' exercise, '{reps}' reps, "
            f"and '{resistance}' resistance has been successfully added to the database."
        )

    conn.close()


@click.command()
@click.argument('exercise')
def get_equipment(exercise):
    '''Gets the equipment for the specified exercise in the exercise database.'''
    conn = sqlite3.connect(Config.EXERCISE_DB_PATH)
    cursor = conn.cursor()

    cursor.execute( 'SELECT tool FROM exercise WHERE id = ?', (exercise,) )

    try:
        print(cursor.fetchone()[0])
    except TypeError:
        print(f"'{exercise}' exercise is not in the database!")
    else:
        conn.close()


@click.command()
@click.option('-w', '--week', required=True, type=int, help='Week number.')
@click.option('-e', '--exercise', required=True, help='Name of the exercise.')
@click.option('-r', '--reps', required=True, type=int, help='Number of repetitions of a given exercise.')
def get_resistance(week, exercise, reps):
    '''Gets the equipment for the specified exercise in the exercise database.'''
    conn = sqlite3.connect(Config.EXERCISE_DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        '''
        SELECT resistance_id FROM week
        WHERE week_id = ?
        AND exercise_id = ?
        AND reps_id = ?
        ''',
        (week, exercise, reps,)
    )

    try:
        print(cursor.fetchone()[0])
    except TypeError:
        print(
            f"Week number {week} with the '{exercise}' exercise "
            f"and {reps} reps is not in the database!"
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
    Updates the resistance for the specified exercise and rep range,
    for the given week.
    '''
    conn = sqlite3.connect(Config.EXERCISE_DB_PATH)
    cursor = conn.cursor()

    # To make sure the row exists in the database
    row_in_db = cursor.execute(
        '''
        SELECT * from week
        WHERE week_id = ?
        AND exercise_id = ?
        AND reps_id = ?
        ''',
        (week, exercise, reps)
    ).fetchone()

    if not row_in_db:
        print(
            f"Week number {week} with '{exercise}' exercise, "
            f"and {reps} reps isn't in the database."
        )
    else:
        cursor.execute(
            '''
            UPDATE week SET resistance_id = ?
            WHERE week_id = ?
            AND exercise_id = ?
            AND reps_id = ?
            ''',
            (new_resistance, week, exercise, reps)
        )
        conn.commit()
        print(
            f"Week number {week} with '{exercise}' exercise, and {reps} reps had its "
            f"resistance successfully updated to '{new_resistance}' resistance in the database."
        )

    conn.close()
