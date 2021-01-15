'''
Contains the functions needed to add exercise information to the database.
'''
import sqlite3
from sqlite3 import IntegrityError
import click
from adonis_lifestyle_tracker.config import EXERCISE_DB_PATH


@click.command()
@click.argument('week')
def add_week(week):
    '''Adds the specified week to its table in the exercise database.'''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute( 'INSERT INTO week (id) VALUES (?)', (week,) )
    except IntegrityError:
        print(f"Week {week} is already in the database.")
    else:
        conn.commit()
        print(
            f"Week {week} has been successfully added to the database."
        )
    finally:
        conn.close()


@click.command()
@click.argument('equipment')
def add_equipment(equipment):
    '''Adds the specified equipment to its table in the exercise database.'''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute(
            'INSERT INTO equipment (id) VALUES (?)', (equipment,)
        )
    except IntegrityError:
        print(f"The '{equipment}' equipment is already in the database.")
    else:
        conn.commit()
        print(
            f"The '{equipment}' equipment has been successfully added to the database."
        )
    finally:
        conn.close()


@click.command()
@click.argument('exercise')
@click.argument('equipment')
def add_exercise(exercise, equipment):
    '''
    Adds the specified exercise and its equipment to its table in the exercise database.
    '''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    # To make sure that the equipment is already in the database
    equipment_in_db = cursor.execute(
      'SELECT * FROM equipment WHERE id =?', (equipment,)
    ).fetchone()

    if equipment_in_db:
        try:
            cursor.execute(
                'INSERT INTO exercise (id, equipment_id) VALUES (?, ?)',
                (exercise, equipment)
            )
        except IntegrityError:
            print(f"The '{exercise}' exercise is already in the database.")
        else:
            conn.commit()
            print(f"The '{exercise}' exercise has been successfully added to the database.")

    else:
        print(f"The '{equipment}' equipment needs to be added to the database.")

    conn.close()


@click.command()
@click.argument('reps', type=int)
def add_reps(reps):
    '''Adds the specified reps to its table in the exercise database.'''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute(
            'INSERT INTO reps (id) VALUES (?)', (reps,)
        )
    except IntegrityError:
        print(f"{reps} reps is already in the database.")
    else:
        conn.commit()
        print(
            f"{reps} reps has been successfully added to the database."
        )
    finally:
        conn.close()


@click.command()
@click.argument('resistance')
def add_resistance(resistance):
    '''Adds the specified resistance to its table in the exercise database.'''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute(
            'INSERT INTO resistance (id) VALUES (?)', (resistance,)
        )
    except IntegrityError:
        print(f"'{resistance}' resistance is already in the database.")
    else:
        conn.commit()
        print(
            f"'{resistance}' resistance has been successfully added to the database."
        )
    finally:
        conn.close()


@click.command()
@click.option('-w', '--week', required=True, type=int, help='Week number.')
@click.option('-e', '--exercise', required=True, help='Name of the exercise.')
@click.option('--reps', required=True, type=int, help='Number of repetitions of a given exercise.')
@click.option('-r', '--resistance', required=True, help='Amount of resistance for a given exercise.')
def add_exercise_reps_resistance_to_week(week, exercise, reps, resistance):
    '''
    Adds the specified exercise, reps, and resistance to the provided week
    in the exercise database.
    '''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    # To make sure the week is in the database
    week_in_db = cursor.execute(
      'SELECT * FROM week WHERE id = ?', (week,)
    ).fetchone()

    # To make sure the exercise is in the database
    exercise_in_db = cursor.execute(
      'SELECT * FROM exercise WHERE id = ?', (exercise,)
    ).fetchone()

    # To make sure the reps are in the database
    reps_in_db = cursor.execute(
      'SELECT * from reps WHERE id = ?', (reps,)
    ).fetchone()

    # To make sure the resistance is in the database
    resistance_in_db = cursor.execute(
      'SELECT * FROM resistance WHERE id = ?', (resistance,)
    ).fetchone()

    # To make sure a duplicate row doesn't exist in the database
    row_in_db = cursor.execute(
        '''
        SELECT *
        FROM week_exercise_reps_resistance
        WHERE week_id = ?
        AND exercise_id = ?
        AND reps_id = ?
        AND resistance_id = ?
        ''',
        (week, exercise, reps, resistance)
    ).fetchone()

    if not week_in_db:
      print(f"Week {week} needs to be added to the database.")
    elif not exercise_in_db:
      print(f"The '{exercise}' exercise needs to be added to the database.")
    elif not reps_in_db:
      print(f"{reps} reps needs to be added to the database.")
    elif not resistance_in_db:
      print(f"'{resistance}' resistance needs to be added to the database.")
    elif row_in_db:
        print(
            f"Week {week} with the '{exercise}' exercise, {reps} reps, "
            f"and '{resistance}' resistance has already been added to the database."
        )
    else:
        cursor.execute(
            '''
            INSERT INTO week_exercise_reps_resistance
                (week_id, exercise_id, reps_id, resistance_id)
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
