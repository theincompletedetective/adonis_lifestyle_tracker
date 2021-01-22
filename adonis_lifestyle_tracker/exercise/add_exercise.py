'''Contains the functions needed to add exercise information to the database.'''
import sqlite3
from sqlite3 import IntegrityError


def add_equipment(db_path, equipment):
    '''
    Adds new equipment to the equipment table in the database.
    '''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute(
            'INSERT INTO equipment (id) VALUES (?)', (equipment,)
        )
    except IntegrityError:
        return f"The '{equipment}' equipment is already in the database."
    else:
        conn.commit()
        return (
            f"The '{equipment}' equipment has been successfully added to the database."
        )
    finally:
        conn.close()


def add_exercise(db_path, exercise, equipment):
    '''
    Adds a new exercise and its equipment to the exercise table in the database.
    '''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # To make sure equipment is already in the equipment table
    equipment_in_db = cursor.execute(
        'SELECT id FROM equipment WHERE id = ?', (equipment,)
    ).fetchone()

    if equipment_in_db:
        try:
            cursor.execute(
                'INSERT INTO exercise (id, equipment_id) VALUES (?, ?)',
                (exercise, equipment)
            )
        except IntegrityError:
            msg = f"The '{exercise}' exercise is already in the database."
        else:
            conn.commit()
            msg = (
                f"The '{exercise}' exercise with the '{equipment}' "
                "equipment has been successfully added to the database."
            )
    else:
        msg = f"'{equipment}' equipment is not in the database."

    conn.close()
    return msg


def add_exercise_to_week(db_path, week, exercise, reps, resistance):
    '''
    Adds an exercise to the specified week in the week_exercise table
    in the database.
    '''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # To make sure the exercise is already in the exercise table
    exercise_in_db = cursor.execute(
        'SELECT id from exercise WHERE id = ?', (exercise,)
    ).fetchone()

    if exercise_in_db:
        try:
            cursor.execute(
                '''
                INSERT INTO week_exercise
                    (week, exercise_id, reps, resistance)
                VALUES(?, ?, ?, ?)
                ''',
                (week, exercise, reps, resistance)
            )
        except IntegrityError:
            msg = (
                f"Week {week} with the '{exercise}' exercise and {reps} reps "
                "is already in the database."
            )
        else:
            conn.commit()
            msg = (
                f"Week {week} with the '{exercise}' exercise, '{reps}' reps, "
                f"and '{resistance}' resistance has been successfully added to the database."
            )
    else:
        msg = f"The '{exercise}' exercise is not in the database."

    conn.close()
    return msg
