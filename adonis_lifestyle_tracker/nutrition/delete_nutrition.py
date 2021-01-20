'''Contains the functions needed to delete nutrition information from the database.'''
import sqlite3


def delete_food(db_path, food):
    '''Deletes the specified food from the database.'''
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

    # To make sure the food is in the database
    food_in_db = cursor.execute(
        'SELECT id FROM food WHERE id = ?', (food,)
    ).fetchone()

    if food_in_db:
        # To delete the food from the food table
        cursor.execute( 'DELETE FROM food WHERE id == ?', (food,) )

        # To delete each row with the food in the week_food table
        cursor.execute( 'DELETE FROM week_food WHERE food_id == ?', (food,) )

        db.commit()
        msg = f"The food '{food}' has been successfully removed from the database."
    else:
        msg = f"The food '{food}' is not in the database."

    db.close()
    return msg
