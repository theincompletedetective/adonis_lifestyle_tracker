'''
Contains the functions needed to delete nutrition information
from the database.
'''
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
        msg = f"The '{food}' food has been deleted from the database."
    else:
        msg = f"The '{food}' food is not in the database."

    conn.close()
    return msg


def delete_week(db_path, week):
    '''Deletes the specified week, with its total calories and protein, from the database.'''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # To make sure week is in database
    week_in_db = cursor.execute(
        'SELECT id FROM week WHERE id = ?', (week,)
    ).fetchone()

    if week_in_db:
        cursor.execute( 'DELETE FROM week WHERE id = ?', (week,) )
        cursor.execute( 'DELETE FROM week_food WHERE week_id = ?', (week,) )

        conn.commit()
        msg = f"Week {week} has been sucessfully deleted from the database."
    else:
        msg = f"Week {week} is not in the database."

    conn.close()
    return msg


def delete_daily_food(db_path, week, day, food):
    '''Deletes the food from the specified day of the provided week.'''
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

    # To make sure week is in database
    week_in_db = cursor.execute(
        'SELECT id FROM week WHERE id = ?', (week,)
    ).fetchone()

    # To make sure the food is in database
    food_in_db = cursor.execute(
        'SELECT id FROM food WHERE id = ?', (food,)
    ).fetchone()

    if not week_in_db:
        msg = f"Week {week} is not in the database."
    elif not food_in_db:
        msg = f"The '{food}' food is not in the database."
    else:
        cursor.execute(
            '''
            DELETE FROM week_food
            WHERE week_id = ?
            AND day_id = ?
            AND food_id = ?
            ''',
            (week, day, food)
        )
        db.commit()
        msg = (
            f"The '{food}' food has been successfully deleted "
            f"from day '{day}', in week {week}."
        )
    
    db.close()
    return msg


def delete_weekly_food(db_path, week, food):
    '''Deletes the food from the specified week in the database.'''
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

    # To make sure week is in database
    week_in_db = cursor.execute(
        'SELECT id FROM week WHERE id = ?', (week,)
    ).fetchone()

    # To make sure the food is in database
    food_in_db = cursor.execute(
        'SELECT id FROM food WHERE id = ?', (food,)
    ).fetchone()

    if not week_in_db:
        msg = f"Week {week} is not in the database."
    elif not food_in_db:
        msg = f"The '{food}' food is not in the database."
    else:
        cursor.execute(
            '''
            DELETE FROM week_food
            WHERE week_id = ?
            AND food_id = ?
            ''',
            (week, food)
        )
        db.commit()
        msg = (
            f"The '{food}' food has been successfully deleted from week {week}."
        )
    
    db.close()
    return msg
