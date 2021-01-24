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


def add_weekly_exercise(db_path, week, exercise):
    '''
    Adds the specified exercise to the provided week in the database.
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
                INSERT INTO week_exercise (week, exercise_id)
                    VALUES(?, ?)
                ''',
                (week, exercise)
            )
        except IntegrityError:
            msg = (
                f"The '{exercise}' exercise has already been added to week {week}."
            )
        else:
            conn.commit()
            msg = (
                f"The '{exercise}' exercise has been successfully added to week {week}."
            )
    else:
        msg = f"The '{exercise}' exercise isn't in the database."

    conn.close()
    return msg
