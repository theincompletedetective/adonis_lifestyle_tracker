'''Contains the functions needed to delete exercise information from the database.'''
import sqlite3


def delete_equipment(db_path, equipment):
    '''Deletes the specified equipment and any exercises that use it from the database.'''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # To make sure the equipment is already in the database
    equipment_in_db = cursor.execute(
        'SELECT id FROM equipment WHERE id = ?', (equipment,)
    ).fetchone()

    if equipment_in_db:
        cursor.execute( 'DELETE FROM equipment WHERE id = ?', (equipment,) )
        cursor.execute( 'DELETE FROM exercise WHERE equipment_id = ?', (equipment,) )
        conn.commit()
        msg = f"The '{equipment}' equipment has been successfully deleted from the database."
    else:
        msg = f"The '{equipment}' equipment is not in the database."

    conn.close()
    return msg


def delete_exercise(db_path, exercise):
    '''Deletes the specified exercise and its equipment from the database.'''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # To make sure the exercise is already in the database
    exercise_in_db = cursor.execute(
        'SELECT id FROM exercise WHERE id = ?', (exercise,)
    ).fetchone()

    if exercise_in_db:
        cursor.execute( 'DELETE FROM exercise WHERE id = ?', (exercise,) )

        # To delete every week with the specified exercise
        cursor.execute(
            'DELETE FROM week_exercise WHERE exercise_id = ?',
            (exercise,)
        )
        conn.commit()
        msg = f"The '{exercise}' exercise has been successfully deleted from the database."
    else:
        msg = f"The '{exercise}' exercise is not in the database."

    conn.close()
    return msg


def delete_weekly_exercise(db_path, week, exercise):
    '''Deletes the specified week from the exercise database.'''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # To make sure the week and exercise are in the database
    exercise_in_week = cursor.execute(
        'SELECT * FROM week_exercise WHERE exercise_id = ?',
        (exercise,)
    ).fetchone()

    if exercise_in_week:
        cursor.execute(
            'DELETE FROM week_exercise WHERE exercise = ?',
            (exercise,)
        )
        conn.commit()
        msg = (
            f"The '{exercise}' exercise has been successfully deleted from week {week}."
        )
    else:
        msg = (
            f"The '{exercise}' exercise is not in week {week} in the database."
        )

    conn.close()
    return msg
