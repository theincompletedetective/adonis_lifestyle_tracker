'''
Contains the functions needed to delete exercise information from the database.
'''
import sqlite3
from sqlite3.dbapi2 import IntegrityError
import click
from adonis_lifestyle_tracker.config import EXERCISE_DB_PATH, check_db


@click.command()
@click.argument('week')
def delete_week(week):
    '''Deletes the specified week from the exercise database.'''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    # To make sure the week is in the database
    week_in_db = check_db(cursor, week)

    if week_in_db:
        try:
            cursor.execute( 'DELETE FROM week WHERE id = ?', (week,) )
        except IntegrityError:
          print(f"Week {week} is not in the database.")
        else:
            # To delete every row in the relation table where the week appears
            cursor.execute(
                'DELETE FROM week_exercise WHERE week_id = ?',
                (week,)
            )
            conn.commit()
            print(
                f"Week {week} has been successfully removed from the database."
            )
    else:
        print(f"Week {week} is not in the database.")

    conn.close()


def delete_equipment(equipment):
    '''
    Deletes the specified equipment from the exercise database.
    '''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    # To make sure the equipment is in the database
    equipment_in_db = check_db(cursor, equipment)

    if equipment_in_db:
        try:
            cursor.execute( 'DELETE FROM equipment WHERE id = ?', (equipment,) )
        except IntegrityError:
            print(f"The '{equipment}' equipment is not in the database.")
        else:
            # To delete the equipment from every exercise that uses it
            cursor.execute(
                'UPDATE exercise SET equipment_id = null WHERE equipment_id = ?',
                (equipment,)
            )
            conn.commit()
            print(
                f"The '{equipment}' equipment has been successfully removed from the database."
            )
    else:
        print(f"The '{equipment}' equipment is not in the database.")

    conn.close()


def delete_exercise(exercise):
    '''
    Deletes the specified exercise and its equipment from the exercise database.
    '''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    # To make sure the exercise is in the database
    exercise_in_db = check_db(cursor, exercise)

    if exercise_in_db:
        try:
            cursor.execute( 'DELETE FROM exercise WHERE id = ?', (exercise,) )
        except IntegrityError:
            print(f"The '{exercise}' exercise is not in the database.")
        else:
            # To delete every week with the exercise
            cursor.execute(
                'DELETE FROM week_exercise WHERE exercise_id = ?',
                (exercise,)
            )
            conn.commit()
            print(
                f"The '{exercise}' exercise has been successfully removed from the database."
            )
    else:
        print(f"The '{exercise}' exercise is not in the database.")

    conn.close()


def delete_reps(reps):
    '''Deletes the specified reps from the exercise database.'''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    # To make sure the reps are in the database
    reps_in_db = check_db(cursor, reps)

    if reps_in_db:
        try:
            cursor.execute( 'DELETE FROM reps WHERE id = ?', (reps,) )
        except IntegrityError:
            print(f"{reps} reps is not in the database.")
        else:
            # To delete every week with the reps
            cursor.execute(
                'DELETE FROM week_exercise WHERE reps_id = ?',
                (reps,)
            )
            conn.commit()
            print(f"{reps} reps has been successfully deleted from the database.")
    else:
        print(f"{reps} reps is not in the database.")

    conn.close()


def delete_resistance(resistance):
    '''Deletes the specified resistance from the exercise database.'''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    # To make sure the resistance is in the database
    resistance_in_db = check_db(cursor, resistance)

    if resistance_in_db:
        try:
            cursor.execute( 'DELETE FROM resistance WHERE id = ?', (resistance,) )
        except IntegrityError:
            print(f"'{resistance}' resistance is not in the database.")
        else:
            # To delete every week with the resistance
            cursor.execute(
                'DELETE FROM week_exercise WHERE resistance_id = ?',
                (resistance,)
            )
            conn.commit()
            print(f"'{resistance}' reps has been successfully deleted from the database.")
    else:
        print(f"'{resistance}' resistance is not in the database.")

    conn.close()
