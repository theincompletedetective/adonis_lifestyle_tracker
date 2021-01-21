'''Contains the functions needed to update nutrition information in the database.'''
import sqlite3
from sqlite3 import IntegrityError


def update_food(db_path, food, calories=None, protein=None):
    '''
    Adds the food with the specified calories and protein to the database.
    '''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # To make sure the food is already in the database
    food_in_db = cursor.execute(
        'SELECT id FROM food WHERE id = ?',
        (food,)
    ).fetchone()

    if food_in_db:

        if calories and protein:
            cursor.execute(
                '''
                UPDATE food
                SET calories = ?, protein = ?
                WHERE id = ?;
                ''',
                (calories, protein, food)
            )
            conn.commit()
            msg = (
                f"The calories for food '{food}' have been updated to {calories}, "
                f"and its grams of protein have been updated to {protein}."
            )
        elif calories and not protein:
            cursor.execute(
                '''
                UPDATE food SET calories = ? WHERE id = ?;
                ''',
                (calories, food)
            )
            conn.commit()
            msg = f"The calories for food '{food}' have been updated to {calories}."
        else: # protein only
            cursor.execute(
                '''
                UPDATE food SET protein = ? WHERE id = ?;
                ''',
                (protein, food)
            )
            conn.commit()
            msg = f"The grams of protein for food '{food}' have been updated to {protein}."

    else:
        msg = f"The '{food}' food is not in the database."
    
    conn.close()
    return msg
