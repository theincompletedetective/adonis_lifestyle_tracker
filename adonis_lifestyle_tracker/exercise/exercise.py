'''Contains the functions needed to CRUD exercise data in the database.'''
import sqlite3
from sqlite3 import IntegrityError
import click
from adonis_lifestyle_tracker.config import Config


@click.command()
@click.argument('week')
def add_week(week):
    '''Adds a week number to the week table of the exercise database.'''
    conn = sqlite3.connect(Config.EXERCISE_DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute( 'INSERT INTO week (id) VALUES (?)', (week,) )
    except IntegrityError:
        print(f'Week number {week} is already in the database.')
    else:
        conn.commit()
        print(f'Week number {week} has been successfully added to the database!')
    finally:
        conn.close()


@click.command()
@click.argument('exercise')
def add_exercise(exercise):
    '''Adds the specified exercise to the exercise table in the exercise database.'''
    conn = sqlite3.connect(Config.EXERCISE_DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute( 'INSERT INTO exercise (id) VALUES (?)', (exercise,) )
    except IntegrityError:
        print(f'The exercise "{exercise}" is already in the database.')
    else:
        conn.commit()
        print(f'The exercise "{exercise}" has been successfully added to the database!')
    finally:
        conn.close()


@click.command()
@click.argument('tool')
def add_equipment(tool):
    '''Adds the specified tool to the equipment table in the exercise database.'''
    conn = sqlite3.connect(Config.EXERCISE_DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute( 'INSERT INTO equipment (id) VALUES (?)', (tool,) )
    except IntegrityError:
        print(f'The equipment "{tool}" is already in the database.')
    else:
        conn.commit()
        print(f'The equipment "{tool}" has been successfully added to the database!')
    finally:
        conn.close()


@click.command()
@click.argument('resistance')
def add_resistance(resistance):
    '''Adds the specified resistance to the resistance table in the exercise database.'''
    conn = sqlite3.connect(Config.EXERCISE_DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute( 'INSERT INTO resistance (id) VALUES (?)', (resistance,) )
    except IntegrityError:
        print(f'The resistance "{resistance}" is already in the database.')
    else:
        conn.commit()
        print(f'The resistance "{resistance}" has been successfully added to the database!')
    finally:
        conn.close()


@click.command()
@click.argument('reps')
def add_reps(reps):
    '''Adds the specified reps to the reps table in the exercise database.'''
    conn = sqlite3.connect(Config.EXERCISE_DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute( 'INSERT INTO reps (id) VALUES (?)', (reps,) )
    except IntegrityError:
        print(f'{reps} reps is already in the database.')
    else:
        conn.commit()
        print(f'{reps} reps has been successfully added to the database!')
    finally:
        conn.close()


@click.command()
@click.option('-w', '--week', required=True, help='Week number.')
@click.option('-e', '--exercise', required=True, help='Name of the exercise.')
@click.option('-t', '--tool', required=True, help='Name of the equipment used for the exercise.')
@click.option('-r', '--resistance', help='Amount of resistance used for the exercise.')
@click.option('--reps', help='Number of repititions used for the exercise.')
def add_exercise_to_week(week, exercise, tool, resistance, reps):
    '''
    Adds the specified week, equipment, resistance, and reps to the exercise_relation
    table in the exercise database.
    '''
    conn = sqlite3.connect(Config.EXERCISE_DB_PATH)
    cursor = conn.cursor()

    # TODO: Make sure that the week is already in the database
    cursor.execute('SELECT id from week WHERE id == ?', (week,) )
    week_in_db = cursor.fetchone()

    # TODO: Make sure that the exercise is already in the database
    cursor.execute('SELECT id from exercise WHERE id == ?', (exercise,) )
    exercise_in_db = cursor.fetchone()

    # TODO: Make sure that the equipment is already in the database
    cursor.execute('SELECT id from equipment WHERE id == ?', (tool,) )
    tool_in_db = cursor.fetchone()

    # TODO: Make sure that the resistance is already in the database
    cursor.execute('SELECT id from resistance WHERE id == ?', (resistance,) )
    resistance_in_db = cursor.fetchone()

    # TODO: Make sure that the number of reps is already in the database
    cursor.execute('SELECT id from reps WHERE id == ?', (reps,) )
    reps_in_db = cursor.fetchone()

    if not week_in_db:
        print(f"The week {week} is not in the database.")
    elif not exercise_in_db:
        print(f"The exercise '{exercise}' is not in the database.")
    elif not tool_in_db:
        print(f"The equipment '{tool}' is not in the database.")
    elif not resistance_in_db:
        print(f"The resistance '{resistance}' is not in the database.")
    elif not reps_in_db:
        print(f"{reps} reps is not in the database.")
    else:
        try:
            cursor.execute(
                '''
                INSERT INTO exercise_relation (week_id, exercise_id, equipment_id, resistance_id, reps_id)
                    VALUES (?, ?, ?, ?, ?);
                ''',
                (week, exercise, tool, resistance, reps)
            )
        except IntegrityError:
            print(
                f'Week {week} with exercise "{exercise}," '
                f'equipment "{tool}," resistance "{resistance}," '
                f'and {reps} reps is already in the database.'
            )
        else:
            conn.commit()
            print(
                f'Week {week} with exercise "{exercise}," '
                f'equipment "{tool}," resistance "{resistance}," '
                f'and {reps} reps has been successfully added to the database!'
            )
        finally:
            conn.close()
