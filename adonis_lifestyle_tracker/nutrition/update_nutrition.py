'''Contains the functions needed to get nutrition information in the database.'''
import sqlite3


def update_food(db_path, food, calories=None, protein=None):
    '''Updates the calories, protein, or both for the specified food in the database.'''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # To make sure food is in database
    food_in_db = cursor.execute(
        'SELECT id FROM food WHERE id = ?', (food,)
    ).fetchone()

    if food_in_db:

        if calories and not protein:
            cursor.execute( 'UPDATE food SET calories = ? WHERE id = ?', (calories, food) )
            conn.commit()
            msg = f"The calories for food '{food}' have been successfully updated to {calories}."
        elif protein and not calories:
            cursor.execute( 'UPDATE food SET protein = ? WHERE id = ?', (protein, food) )
            conn.commit()
            msg = f"The protein for food '{food}' has been successfully updated to {protein} grams."
        elif protein and calories:
            cursor.execute( 'UPDATE food SET calories = ? WHERE id = ?', (calories, food) )
            cursor.execute( 'UPDATE food SET protein = ? WHERE id = ?', (protein, food) )
            conn.commit()
            msg = (
                f"The calories for food '{food}' have been successfully updated to {calories}, "
                f"and its protein to {protein} grams."
            )
        else:
            msg = 'You must update the protein, calories, or both.'

    else:
        msg = f"The food '{food}' is not in the database."

    conn.close()
    return msg
