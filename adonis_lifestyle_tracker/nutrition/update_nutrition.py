'''
Contains the functions needed to update nutrition information in the database.
'''
import sqlite3


def update_food(db_path, food, calories=None, protein=None):
    '''
    Adds the food with the specified calories and protein to the database.
    '''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # To make sure the food is already in the database
    food_in_db = cursor.execute(
        'SELECT id FROM food WHERE id = ?', (food,)
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
                f"The calories for the '{food}' food have been updated "
                f"to {calories}, and its grams of protein have been "
                f"updated to {protein}."
            )
        elif calories and not protein:
            cursor.execute(
                '''
                UPDATE food SET calories = ? WHERE id = ?;
                ''',
                (calories, food)
            )
            conn.commit()
            msg = (
                f"The calories for the '{food}' food have been updated "
                f"to {calories}."
            )
        else: # protein only
            cursor.execute(
                '''
                UPDATE food SET protein = ? WHERE id = ?;
                ''',
                (protein, food)
            )
            conn.commit()
            msg = (
                f"The grams of protein for the '{food}' food have been updated "
                f"to {protein}."
            )

    else:
        msg = f"The '{food}' food is not in the database."

    conn.close()
    return msg


def update_weekly_totals(db_path, week, total_calories, total_protein):
    '''Updates the total calories and protein for the specified week.'''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # To make sure week is in database
    week_in_db = cursor.execute(
        'SELECT id FROM week WHERE id = ?', (week,)
    ).fetchone()

    if week_in_db:
        cursor.execute(
            'UPDATE week SET total_calories = ? WHERE id = ?', (total_calories, week)
        )
        cursor.execute(
            'UPDATE week SET total_protein = ? WHERE id = ?', (total_protein, week,)
        )

        conn.commit()
        msg = (
            f"Total calories for week {week} have been updated to {total_calories}, "
            f"and the total protein has been updated to {total_protein} grams."
        )
    else:
        msg = f"Week {week} is not in the database."

    conn.close()
    return msg
