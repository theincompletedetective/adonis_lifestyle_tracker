'''Contains the functions needed to delete exercise information from the database.'''
import sqlite3


def delete_equipment(db_path, equipment):
    '''Deletes the specified equipment from the database.'''
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

    # To make sure equipment is already in the equipment table
    equipment_in_db = cursor.execute(
        'SELECT id FROM equipment WHERE id = ?', (equipment,)
    ).fetchone()

    if equipment_in_db:
        cursor.execute(
            'DELETE FROM equipment WHERE id = ?', (equipment,)
        )
        db.commit()
        msg = (
                f"The equipment '{equipment}' has been deleted from the database."
            )
    else:
        msg = f"The '{equipment}' equipment is not in the database."

    db.close()
    return msg


def delete_exercise(db_path, exercise):
    '''Deletes the specified exercise from the databaes.'''
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

    # To make sure the exercise is already in the exercise table
    exercise_in_db = cursor.execute(
        'SELECT id from exercise WHERE id = ?', (exercise,)
    ).fetchone()

    if exercise_in_db:
        cursor.execute( 'DELETE FROM exercise WHERE id = ?', (exercise,) )
        db.commit()
        msg = f"The '{exercise}' exercise has been deleted from the database."
    else:
        msg = f"The '{exercise}' exercise is not in the database."

    db.close()
    return msg
