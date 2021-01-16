'''
Contains the functions needed to update exercise information in the database.
'''
import sqlite3
from sqlite3.dbapi2 import IntegrityError
import click
from adonis_lifestyle_tracker.config import EXERCISE_DB_PATH, check_in_db


@click.command()
@click.option('-o', '--old-equipment', required=True, help='Equipment currently in the database')
@click.option('-n', '--new-equipment', required=True, help='New name for equipment in the database')
def update_equipment(old_equipment, new_equipment):
    '''Updates the name of some equipment in the exercise database.'''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    # To make sure that new equipment isn't already in the database
    new_equipment_in_db = check_in_db(cursor, new_equipment)

    if new_equipment_in_db:
        print(f"The '{new_equipment}' equipment is already in the database.")
    else:
        try:
            cursor.execute(
                'UPDATE equipment SET id = ? WHERE id = ?',
                (new_equipment, old_equipment)
            )
        except IntegrityError:
            print(f"The '{old_equipment}' equipment is not in the database.")
        else:
            # To change the equipment for all exercises that use it
            cursor.execute(
                '''
                UPDATE exercise SET equipment_id = ? WHERE equipment_id = ?
                ''',
                (new_equipment, old_equipment)
            )
            conn.commit()
            print(f"The '{old_equipment}' equipment has been updated to '{new_equipment}'.")

    conn.close()


@click.command()
@click.option('-o', '--old-exercise', required=True, help='Exercise currently in the database')
@click.option('-n', '--new-exercise', required=True, help='New name for exercise in the database')
def update_exercise(old_exercise, new_exercise):
    '''Changes the name of an exercise in the database.'''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    # To make sure that new exercise isn't already in the database
    new_exercise_in_db = check_in_db(cursor, new_exercise)

    if new_exercise_in_db:
        print(f"The '{new_exercise}' exercise is already in the database.")
    else:
        try:
            cursor.execute(
                'UPDATE exercise SET id = ? WHERE id = ?',
                (new_exercise, old_exercise)
            )
        except IntegrityError:
            print(f"The '{old_exercise}' exercise is not in the database.")
        else:
            # To update each occurrence of the exercise in the week_exercise table
            cursor.execute(
                '''
                UPDATE week_exercise
                SET exercise_id = ?
                WHERE exercise_id = ?
                ''',
                (new_exercise, old_exercise)
            )
            conn.commit()
            print(f"The '{old_exercise}' exercise has been updated to '{new_exercise}'.")

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
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    # To make sure the week, exercise, and reps are already in the database
    week_in_db = cursor.execute(
        '''
        SELECT * FROM week_exercise
        WHERE week_id = ?
        AND exercise_id = ?
        AND reps_id = ?
        ''',
        (week, exercise, reps,)
    ).fetchone()

    # To make sure an identical row is not already in the database
    row_in_db = cursor.execute(
        '''
        SELECT * FROM week_exercise
        WHERE week_id = ?
        AND exercise_id = ?
        AND reps_id = ?
        AND resistance_id = ?
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
            UPDATE week_exercise
            SET resistance_id = ?
            WHERE week_id = ?
            AND exercise_id = ?
            AND reps_id = ?
            ''',
            (new_resistance, week, exercise, reps,)
        )
        conn.commit()
        print(
            f"The resistance for week {week}, the '{exercise}' exercise, "
            f"and {reps} reps has been successfully updated to {new_resistance}."
        )
        conn.close()
