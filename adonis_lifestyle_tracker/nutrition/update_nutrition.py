'''Contains the functions needed to update the nutrition information in the database.'''
import sqlite3
from sqlite3 import IntegrityError


def update_food(db_path, food, calories=None, protein=None):
    '''Updates the calories and/or protein in the specified food.'''
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

    try:

        if calories and not protein:
            cursor.execute(
                'UPDATE food SET calories = ? WHERE id = ?',
                (calories, food)
            )
            msg = f"The calories for food '{food}' have been updated to {calories}."
        elif protein and not calories:
            cursor.execute(
                'UPDATE food SET protein = ? WHERE id = ?',
                (protein, food)
            )
            msg = f"The grams of protein for food '{food}' have been updated to {protein}."
        else:
            cursor.execute(
                'UPDATE food SET calories = ? WHERE id = ?',
                (calories, food)
            )
            cursor.execute(
                'UPDATE food SET protein = ? WHERE id = ?',
                (protein, food)
            )
            msg = (
                f"The calories for food '{food}' have been updated to {calories}, "
                f"and its grams of protein has been updated to {protein}."
            )

    except IntegrityError:
        msg = f"The food '{food}' isn't in the database."
    else:
        db.commit()
    finally:
        db.close()
        return msg
