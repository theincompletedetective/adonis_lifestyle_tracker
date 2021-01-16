'''Contains the absolute path to the nutrition and exercise databases.'''
import os


NUTRITION_DB_PATH = os.path.join(os.path.dirname(__file__), 'nutrition', 'nutrition.db')
EXERCISE_DB_PATH = os.path.join(os.path.dirname(__file__), 'exercise', 'exercise.db')


def check_db(cursor, table, value=None):
    '''
    Checks to see whether or not the provided value is in the specified database table.
    '''
    if value:
        return cursor.execute(
            'SELECT * FROM ? WHERE id = ?', (table, value)
        ).fetchone()
    else:
        return cursor.execute(
            'SELECT * FROM ? WHERE id = ?', (table, table)
        ).fetchone()
