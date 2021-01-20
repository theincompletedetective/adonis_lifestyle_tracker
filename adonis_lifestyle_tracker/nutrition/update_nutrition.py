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


def update_week_totals(db_path, week, total_calories, total_protein):
    '''Updates the total calories and protein for the specified week.'''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # To make sure week is already in the database
    week_in_db = cursor.execute(
        'SELECT id FROM week WHERE id = ?', (week,)
    ).fetchone()

    if week_in_db:
        cursor.execute(
            '''
            UPDATE week
            SET total_calories = ?
            AND total_protein = ?
            WHERE id = ?
            ''',
            (total_calories, total_protein, week)
        )
        conn.commit()
        msg = (
            f'The total calories for week {week} has been successfully updated to {total_calories}, '
            f' and the total grams of protein has been successfully updated to {total_protein}.'
        )
    else:
        msg = f"Week {week} is not in the database."

    conn.close()
    return msg
