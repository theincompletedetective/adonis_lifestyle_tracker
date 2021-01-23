'''Contains the functions needed to update exercise information in the database.'''
import sqlite3


def rename_equipment(db_path, old_equipment, new_equipment):
    '''Updates the name of the equipment in the database.'''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # To make sure equipment is already in the equipment table
    equipment_in_db = cursor.execute(
        'SELECT id FROM equipment WHERE id = ?', (old_equipment,)
    ).fetchone()

    if equipment_in_db:
        cursor.execute(
            'UPDATE equipment SET id = ? WHERE id = ?',
            (new_equipment, old_equipment)
        )
        conn.commit()
        msg = (
            f"The name for '{old_equipment}' has been updated to '{new_equipment}'."
        )
    else:
        msg = f"The '{old_equipment}' equipment is not in the database."

    conn.close()
    return msg


def update_exercise(db_path, exercise, equipment):
    '''Updates the equipment for the specified exercise.'''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # To make sure equipment is already in the equipment table
    equipment_in_db = cursor.execute(
        'SELECT id FROM equipment WHERE id = ?', (equipment,)
    ).fetchone()

    # To make sure the exercise is already in the database
    exercise_in_db = cursor.execute(
        'SELECT id FROM exercise WHERE id = ?', (exercise,)
    ).fetchone()

    if not equipment_in_db:
        msg = f"The '{equipment}' equipment is not in the database."
    elif not exercise_in_db:
        msg = f"The '{exercise}' exercise is not in the database."
    else:
        cursor.execute(
            'UPDATE exercise SET equipment_id = ? WHERE id = ?',
            (equipment, exercise)
        )
        conn.commit()
        msg = (
            f"The equipment for the '{exercise}' execise has been "
            f"successfully updated to '{equipment}'."
        )

    conn.close()
    return msg


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
            f"The '{exercise}' exercise had its resistance for {reps} reps "
            f"updated to '{resistance}'."
        )
    else:
        msg = f"The '{exercise}' exercise is not in the database."

    db.close()
    return msg
