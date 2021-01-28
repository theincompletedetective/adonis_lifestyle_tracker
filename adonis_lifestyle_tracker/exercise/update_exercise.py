'''Contains the functions needed to update exercise information in the database.'''
import sqlite3


def update_resistance(db_path, exercise, reps, resistance):
    '''
    Updates the resistance used for the specified exercise and rep range.
    '''
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

    # To make sure the exercise is already in the exercise table
    exercise_in_db = cursor.execute(
        'SELECT id from exercise WHERE id = ?', (exercise,)
    ).fetchone()

    if exercise_in_db:
        cursor.execute( f'UPDATE exercise SET reps{reps} = ?', (resistance,) )
        db.commit()
        msg = (
            f"The resistance for the '{exercise}' exercise and {reps} reps "
            f"has been successfully updated to '{resistance}'."
        )
    else:
        msg = f"The '{exercise}' exercise is not in the database."

    db.close()
    return msg


def update_equipment(db_path, exercise, equipment):
    '''Updates the equipment for the specified exercise.'''
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

    # To make sure equipment is already in the equipment table
    equipment_in_db = cursor.execute(
        'SELECT id FROM equipment WHERE id = ?', (equipment,)
    ).fetchone()

    if equipment_in_db:
        cursor.execute(
            'UPDATE exercise SET equipment_id = ? WHERE id = ?',
            (equipment, exercise)
        )
        db.commit()
        msg = (
                f"The equipment for the '{exercise}' exercise has been "
                f"successfully updated to '{equipment}'."
            )
    else:
        msg = f"The '{equipment}' equipment is not in the database."

    db.close()
    return msg
