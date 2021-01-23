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


def update_resistance(db_path, week, exercise, reps, new_resistance):
    '''
    Changes the resistance used for the specified exercise, at the given rep range,
    for the provided week in the week_exercise table in the database.
    '''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # To see if an identical row is in the database
    full_row_in_db = cursor.execute(
        '''
        SELECT * from week_exercise
        WHERE week = ?
        AND exercise_id = ?
        AND reps = ?
        AND resistance = ?
        ''',
        (week, exercise, reps, new_resistance)
    ).fetchone()

    # To see if the week, exercise, and reps are in the database
    part_row_in_db = cursor.execute(
        '''
        SELECT * from week_exercise
        WHERE week = ?
        AND exercise_id = ?
        AND reps = ?
        ''',
        (week, exercise, reps)
    ).fetchone()

    if full_row_in_db:
        msg = (
            f"Week {week} with the '{exercise}' exercise, {reps} reps, "
            f"and '{new_resistance}' resistance is already in the database."
        )
    elif part_row_in_db:
        cursor.execute(
            '''
            UPDATE week_exercise
            SET resistance = ?
            WHERE week = ?
            AND exercise_id = ?
            AND reps = ?
            ''',
            (new_resistance, week, exercise, reps)
        )

        conn.commit()
        msg = (
            f"The resistance for week {week}, the '{exercise}' exercise, "
            f"and {reps} reps has been successfully updated to '{new_resistance}'."
        )
    else:
        msg = (
            f"Week {week} with the '{exercise}' exercise "
            f"and {reps} reps is not in the database."
        )

    conn.close()
    return msg
