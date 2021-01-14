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
@click.argument('week', type=int)
def add_week(week):
    '''Adds the specified week number to its table in the exercise database.'''
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute( 'INSERT INTO week (id) VALUES (?)', (week,) )
    except IntegrityError:
        print(f'Week number {week} is already in the database.')
    else:
        conn.commit()
        print(f'Week number {week} has been successfully added to the database.')
    finally:
        conn.close()


@click.command()
@click.argument('equipment')
def add_equipment(equipment):
    '''Adds the specified equipment to its table in the exercise database.'''
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute( 'INSERT INTO equipment (id) VALUES (?)', (equipment,) )
    except IntegrityError:
        print(f"The '{equipment}' equipment is already in the database!")
    else:
        conn.commit()
        print(
            f"The '{equipment}' equipment has been successfully added to the database."
        )
    finally:
        conn.close()


@click.command()
@click.option('-ex', '--exercise', required=True, help='Name of the exercise.')
@click.option('-eq', '--equipment', required=True, help='Equipment used to perform the exercise.')
def add_exercise(exercise, equipment):
    '''Adds the specified exercise and equipment to the exercise table in the database.'''
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # TODO: Make sure that the equipment already exists in the database
    equipment_in_db = cursor.execute(
        'SELECT * FROM equipment WHERE id = ?', (equipment,)
    )

    if not equipment_in_db:
        print(f"The '{equipment}' equipment isn't in the database.")
    else:
        try:
            cursor.execute(
                'INSERT INTO exercise (id, equipment_id) VALUES (?, ?)',
                (exercise, equipment)
            )
        except IntegrityError:
            print(f"The '{exercise}' exercise is already in the database!")
        else:
            conn.commit()
            print(
                f"The '{exercise}' exercise and its '{equipment}' equipment have "
                "been successfully added to the database!"
            )

    conn.close()


@click.command()
@click.argument('reps', type=int)
def add_reps(reps):
    '''Adds the specified number of reps to its table in the exercise database.'''
    conn = sqlite3.connect(DB_PATH)
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
    '''Adds the specified amount of resistance to its table in the exercise database.'''
    conn = sqlite3.connect(DB_PATH)
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
def add_exercise_info_to_week(week, exercise, reps, resistance):
    '''Adds the specified exercise, reps, and resistance to the provided week.'''
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # To make sure the week, exercise, reps, and resistance are in the database
    week_in_db = cursor.execute( 'SELECT * from week where id = ?', (week,) ).fetchone()
    exercise_in_db = cursor.execute( 'SELECT * from exercise where id = ?', (exercise,) ).fetchone()
    reps_in_db = cursor.execute( 'SELECT * from reps where id = ?', (reps,) ).fetchone()
    resistance_in_db = cursor.execute( 'SELECT * from resistance where id = ?', (resistance,) ).fetchone()

    # To make sure a duplicate row doesn't exist in the database
    duplicate_row_in_db = cursor.execute(
        '''
        SELECT * from week_exercise_reps_resistance
        WHERE week_id = ?
        AND exercise_id = ?
        AND reps_id = ?
        AND resistance_id = ?
        ''',
        (week, exercise, reps, resistance)
    ).fetchone()

    if not week_in_db:
        print(f"Week number {week} is not in the database.")
    elif not exercise_in_db:
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
            INSERT INTO week_exercise_reps_resistance
                (week_id, exercise_id, reps_id, resistance_id)
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
    '''Gets the equipment for the specified exercise in the exercise table.'''
    conn = sqlite3.connect(DB_PATH)
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
    '''Gets the equipment for the specified exercise in the exercise database.'''
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        '''
        SELECT resistance_id
        FROM week_exercise_reps_resistance
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
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # To make sure the old row exists in the database
    old_row_in_db = cursor.execute(
        '''
        SELECT *
        FROM week_exercise_reps_resistance
        WHERE week_id = ?
        AND exercise_id = ?
        AND reps_id = ?
        ''',
        (week, exercise, reps)
    ).fetchone()

    # To make sure that new values aren't in the database
    new_row_in_db = cursor.execute(
        '''
        SELECT *
        FROM week_exercise_reps_resistance
        WHERE resistance_id = ?
        AND week_id = ?
        AND exercise_id = ?
        AND reps_id = ?
        ''',
        (new_resistance, week, exercise, reps)
    ).fetchone()

    if not old_row_in_db:
        print(
            f"Week number {week} with the '{exercise}' exercise, "
            f"and {reps} reps isn't in the database."
        )
    elif new_row_in_db:
        print(
            f"Week number {week} with the '{exercise}' exercise, "
            f"{reps} reps, and '{new_resistance}' resistance is already in the database."
        )
    else:
        cursor.execute(
            '''
            UPDATE week_exercise_reps_resistance
            SET resistance_id = ?
            WHERE week_id = ?
            AND exercise_id = ?
            AND reps_id = ?
            ''',
            (new_resistance, week, exercise, reps)
        )
        conn.commit()
        print(
            f"Week number {week} with the '{exercise}' exercise, and {reps} reps had its "
            f"resistance successfully updated to '{new_resistance}'."
        )

    conn.close()
