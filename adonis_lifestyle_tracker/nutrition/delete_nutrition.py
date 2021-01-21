'''Contains the functions needed to delete nutrition information from the database.'''
import sqlite3


def delete_food(db_path, food):
    '''Deletes the specified food from the database.'''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # To make sure the food is already in the database
    food_in_db = cursor.execute(
        'SELECT id FROM food WHERE id = ?', (food,)
    ).fetchone()

    if food_in_db:
        cursor.execute( 'DELETE FROM food WHERE id = ?', (food,) )

        # To delete all the rows in the week_food table with the specified food
        cursor.execute( 'DELETE FROM week_food WHERE food_id = ?', (food,) )

        conn.commit()
        msg = f"The food '{food}' has been deleted from the database."
    else:
        msg = f"The food '{food}' is not in the database." 
    
    conn.close()
    return msg
