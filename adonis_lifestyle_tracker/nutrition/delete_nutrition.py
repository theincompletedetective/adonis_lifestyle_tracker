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


def delete_nutrition_week(db_path, week):
    '''Deletes the specified week from the week table in the database.'''
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

    # To make sure the food is in the database
    week_in_db = cursor.execute(
        'SELECT id FROM week WHERE id = ?', (week,)
    ).fetchone()

    if week_in_db:
        # To delete the week from the week table
        cursor.execute( 'DELETE FROM week WHERE id == ?', (week,) )

        # To delete each row with the week in the week_food table
        cursor.execute( 'DELETE FROM week_food WHERE week_id == ?', (week,) )

        db.commit()
        msg = f"Week {week} has been successfully removed from the database."
    else:
        msg = f"Week {week} is not in the database."

    db.close()
    return msg
