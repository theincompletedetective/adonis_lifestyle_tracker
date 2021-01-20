'''Contains the functions needed to update exercise information in the database.'''
import sqlite3


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
