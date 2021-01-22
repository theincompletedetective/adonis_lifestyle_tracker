'''Contains the functions needed to delete exercise information from the database.'''
import sqlite3
from sqlite3 import IntegrityError


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
        msg = f"The exercise '{exercise}' has been successfully deleted from the database."
    else:
        msg = f"The exercise '{exercise}' is not in the database."
    
    conn.close()
    return msg


def delete_week(db_path, week, exercise, reps, resistance):
    '''Deletes the specified week from the exercise database.'''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # To make sure the week, exercise, reps, and resistance are in the database
    week_in_db = cursor.execute(
        '''
        SELECT * FROM week_exercise
        WHERE week = ?
        AND exercise_id = ?
        AND reps = ?
        AND resistance = ?
        ''',
        (week, exercise, reps, resistance)
    ).fetchone()

    if week_in_db:
        cursor.execute(
            '''
            DELETE FROM week_exercise
            WHERE week = ?
            AND exercise_id = ?
            AND reps = ?
            AND resistance = ?
            ''',
            (week, exercise, reps, resistance)
        )
        conn.commit()
        msg = (
            f"Week {week} with the '{exercise}' exercise, {reps} reps, "
            f"and '{resistance}' resistance has been successfully removed from the database."
        )
    else:
        msg = (
            f"Week {week} with the '{exercise}' exercise, {reps} reps, "
            f"and '{resistance}' resistance is not in the database."
        )
    
    conn.close()
    return msg
