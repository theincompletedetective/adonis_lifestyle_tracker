'''Contains the functions needed to get exercise information from the database.'''
import sqlite3


def get_equipment(db_path, exercise):
    '''
    Gets the equipment for the specified exercise from the exercise table
    in the database.
    '''
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

    cursor.execute(
        'SELECT equipment_id FROM exercise WHERE id = ?',
        (exercise,)
    )

    try:
        return cursor.fetchone()[0]
    except TypeError:
        return f"The '{exercise}' exercise isn't in the database."
    finally:
        db.close()


def get_resistance(db_path, exercise, reps):
    '''
    Gets the resistance for the specified exercise, and the provided number of reps.
    '''
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

    cursor.execute(
        f'SELECT reps{reps} FROM exercise WHERE id = ?', (exercise,)
    )

    try:
        return cursor.fetchone()[0]
    except TypeError:
        return (
            f"The '{exercise}' exercise isn't in the database."
        )
    finally:
        db.close()
