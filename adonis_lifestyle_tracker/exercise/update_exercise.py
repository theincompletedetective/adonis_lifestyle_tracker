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
