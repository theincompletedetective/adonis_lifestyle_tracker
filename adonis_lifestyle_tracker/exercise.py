'''
Contains the functions needed to add and update exercise information in the database.
'''
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


def get_resistance(db_path, week, exercise, reps):
    '''
    Gets the resistance for the specified week, exercise, and number of reps
    in the week_exercise table in the database.
    '''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(
        '''
        SELECT resistance
        FROM week_exercise
        WHERE week = ?
        AND exercise_id = ?
        AND reps = ?
        ''',
        (week, exercise, reps)
    )

    try:
        return cursor.fetchone()[0]
    except TypeError:
        return (
            f"Week {week} with the '{exercise}' exercise "
            f"and {reps} reps is not in the database."
        )
    finally:
        conn.close()


def change_resistance(db_path, week, exercise, reps, new_resistance):
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
