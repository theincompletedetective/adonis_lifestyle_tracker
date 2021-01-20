'''Contains the functions needed to delete exercise information from the database.'''
import sqlite3


def delete_equipment(db_path, equipment):
    '''Deletes the specified equipment from the database.'''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # To make sure equipment is in the database
    equipment_in_db = cursor.execute(
        'SELECT id FROM equipment WHERE id = ?', (equipment,)
    ).fetchone()

    if equipment_in_db:
        cursor.execute( 'DELETE FROM equipment WHERE id = ?', (equipment,) )
        conn.commit()
        msg = f"The '{equipment}' equipment has been successfully removed from the database."
    else:
        msg = f"The '{equipment}' equipment is not in the database."

    conn.close()
    return msg


def delete_exercise(db_path, exercise):
    '''Deletes the specified exercise from the database.'''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # To make sure exercise is in the database
    exercise_in_db = cursor.execute(
        'SELECT id FROM exercise WHERE id = ?', (exercise,)
    ).fetchone()

    if exercise_in_db:
        cursor.execute( 'DELETE FROM exercise WHERE id = ?', (exercise,) )
        cursor.execute( 'DELETE FROM week_exercise WHERE exercise_id = ?', (exercise,) )
        conn.commit()
        msg = f"The '{exercise}' exercise has been successfully removed from the database."
    else:
        msg = f"The '{exercise}' equipment is not in the database."

    conn.close()
    return msg
