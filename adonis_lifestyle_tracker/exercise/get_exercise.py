'''Contains the functions needed to get exercise information from the database.'''
import sqlite3


def get_equipment(db_path, exercise):
    '''
    Gets the equipment for the specified exercise from the exercise table
    in the database.
    '''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(
        'SELECT equipment_id FROM exercise WHERE id = ?',
        (exercise,)
    )

    try:
        return cursor.fetchone()[0]
    except TypeError:
        return f"The '{exercise}' exercise is not in the database."
    finally:
        conn.close()


def get_resistance(db_path, exercise, reps):
    '''
    Gets the resistance for the specified exercise, and the provided number of reps.
    '''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(
        f'SELECT reps{reps} FROM exercise WHERE id = ?', (exercise,)
    )

    try:
        return cursor.fetchone()[0]
    except TypeError:
        return (
            f"The '{exercise}' exercise is not in the database."
        )
    finally:
        conn.close()
