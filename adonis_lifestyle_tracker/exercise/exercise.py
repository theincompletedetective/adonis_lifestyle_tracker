'''Contains the functions needed to CRUD exercise data in the database.'''
import sqlite3
from sqlite3 import IntegrityError
import click
from adonis_lifestyle_tracker.config import Config


@click.command()
@click.argument('week')
def add_week(week):
    '''Adds the specified week number to the week table in the exercise database.'''
    conn = sqlite3.connect(Config.EXERCISE_DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute( 'INSERT INTO week (id) VALUES (?)', (week,), )
    except IntegrityError:
        print(f'Week number {week} is already in the database.')
    else:
        conn.commit()
        print(f'Week number {week} has been successfully added to the database!')
    finally:
        conn.close()


@click.command()
@click.option('-e', '--exercise', required=True, help='Name of the exercise.')
@click.option('-t', '--tool', required=True, help='Name of the equipment used for the exercise.')
def add_exercise(exercise, tool):
    '''Adds an exercise and its equipment to the exercise table of the exercise database.'''
    conn = sqlite3.connect(Config.EXERCISE_DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute( 'INSERT INTO exercise (id, tool_id) VALUES (?, ?)', (exercise, tool), )
    except IntegrityError:
        print(f'The "{exercise}" exercise and "{tool}" equipment are already in the database.')
    else:
        conn.commit()
        print(
            f'The "{exercise}" exercise and "{tool}" equipment '
            'have been successfully added to the database!'
        )
    finally:
        conn.close()


@click.command()
@click.argument('reps')
def add_reps(reps):
    '''Adds the specified reps to the reps table in the exercise database.'''
    conn = sqlite3.connect(Config.EXERCISE_DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute( 'INSERT INTO reps (id) VALUES (?)', (reps,), )
    except IntegrityError:
        print(f'{reps} reps is already in the database.')
    else:
        conn.commit()
        print(f'{reps} reps has been successfully added to the database!')
    finally:
        conn.close()


@click.command()
@click.argument('resistance')
def add_resistance(resistance):
    '''Adds the specified resistance to the resistance table in the exercise database.'''
    conn = sqlite3.connect(Config.EXERCISE_DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute( 'INSERT INTO resistance (id) VALUES (?)', (resistance,), )
    except IntegrityError:
        print(f'"{resistance}" resistance is already in the database.')
    else:
        conn.commit()
        print(f'"{resistance}" resistance has been successfully added to the database!')
    finally:
        conn.close()


@click.command()
@click.option('-e', '--exercise', required=True, help='Name of the exercise.')
@click.option('-w', '--week', required=True, type=int, help='Week number.')
def add_week_to_exercise(exercise, week):
    '''
    Adds the specified exercise and week to the exercise_week table
    in the exercise database.
    '''
    conn = sqlite3.connect(Config.EXERCISE_DB_PATH)
    cursor = conn.cursor()

    # To make sure that the exercise is already in the exercise database
    cursor.execute( 'SELECT * from exercise WHERE id = ?', (exercise,) )
    exercise_in_db = cursor.fetchone()

    # To make sure the week is already in the exercise database
    cursor.execute( 'SELECT * from week WHERE id = ?', (week,) )
    week_in_db = cursor.fetchone()

    # To make sure the same exercise was not already added to the same week
    cursor.execute(
        'SELECT * from exercise_week WHERE exercise_id = ? AND week_id = ?',
        (exercise, week)
    )
    exercise_week_in_db = cursor.fetchone()

    if not exercise_in_db:
        print(f"The '{exercise}' exercise is not in the database.")
    elif not week_in_db:
        print(f"Week number {week} is not in the database.")
    elif exercise_week_in_db:
        print(f"Week number {week} has already been added to the '{exercise}' exercise in the database.")
    else:
        cursor.execute(
            'INSERT INTO exercise_week (exercise_id, week_id) VALUES (?, ?)',
            (exercise, week),
        )
        conn.commit()
        print(f"Week number {week} has been successfully added to the '{exercise}' exercise in the database!")

    conn.close()


@click.command()
@click.option('-e', '--exercise', required=True, help='Name of the exercise.')
@click.option('--reps', required=True, type=int, help='Number of repetitions to use for the exercise.')
@click.option('-r', '--resistance', required=True, help='Amount of resistance to use for the exercise.')
def add_reps_and_resistance(exercise, reps, resistance):
    '''
    Adds the specified resistance and reps to the exercise_reps_resistance table
    in the exercise database.
    '''
    conn = sqlite3.connect(Config.EXERCISE_DB_PATH)
    cursor = conn.cursor()

    # To make sure that the exercise is already in the exercise database
    cursor.execute( 'SELECT * from exercise WHERE id = ?', (exercise,) )
    exercise_in_db = cursor.fetchone()

    # To make sure the reps is already in the exercise database
    cursor.execute( 'SELECT * from reps WHERE id = ?', (reps,) )
    reps_in_db = cursor.fetchone()

    # To make sure the resistance is already in the exercise database
    cursor.execute( 'SELECT * from resistance WHERE id = ?', (resistance,) )
    resistance_in_db = cursor.fetchone()

    # To make sure that the same exercise, reps, and resistance are not already in the database
    cursor.execute(
        '''
        SELECT * from exercise_reps_resistance
        WHERE exercise_id = ?
        AND reps_id = ?
        AND resistance_id = ?
        ''',
        (exercise, reps, resistance)
    )
    exercise_reps_resistance_in_db = cursor.fetchone()

    if not exercise_in_db:
        print(f"The '{exercise}' exercise is not in the database.")
    elif not reps_in_db:
        print(f"{reps} reps is not in the database.")
    elif not resistance_in_db:
        print(f"'{resistance}' resistance is not in the database.")
    elif exercise_reps_resistance_in_db:
        print(
            f"{reps} reps and '{resistance}' resistance have already been added "
            f"to the '{exercise}' exercise in the database."
        )
    else:
        cursor.execute(
            'INSERT INTO exercise_reps_resistance (exercise_id, reps_id, resistance_id) VALUES (?, ?, ?)',
            (exercise, reps, resistance),
        )
        conn.commit()
        print(
            f"{reps} reps and '{resistance}' resistance have been successfully added "
            f"to the '{exercise}' exercise in the database!"
        )

    conn.close()
