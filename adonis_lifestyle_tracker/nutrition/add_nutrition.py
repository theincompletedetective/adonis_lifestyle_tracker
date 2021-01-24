'''Contains the functions needed to add nutrition information to the database.'''
import sqlite3
from sqlite3 import IntegrityError


def add_food(db_path, food, calories, protein):
    '''
    Adds the food with the specified calories and protein to the database.
    '''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute(
            '''
            INSERT INTO food (id, calories, protein)
                VALUES (?, ?, ?);
            ''',
            (food, calories, protein)
        )
    except IntegrityError:
        return f"The food '{food}' is already in the database."
    else:
        conn.commit()
        return (
            f"The food '{food}' has been successfully added to the database, "
            f"with {calories} calories and {protein} grams of protein."
        )
    finally:
        conn.close()


def add_weekly_totals(db_path, week, total_calories, total_protein):
    '''
    Adds a week, total calories, and total protein to the week table
    in the database.
    '''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute(
            '''
            INSERT INTO week (id, total_calories, total_protein)
                VALUES (?, ?, ?);
            ''',
            (week, total_calories, total_protein)
        )
    except IntegrityError:
        return f'Week {week} is already in the database.'
    else:
        conn.commit()
        return (
            f'Week {week} has been successfully added to the database, '
            f'with {total_calories} total calories, and {total_protein} '
            'total grams of protein.'
        )
    finally:
        conn.close()


def add_weekly_food(db_path, week, day, food):
    '''Adds a week and food to the week_food table in the database.'''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # To make sure food and week are already in the database
    found_food = cursor.execute(
        'SELECT * FROM food WHERE id == ?;', (food,)
    ).fetchone()

    found_week = cursor.execute(
        'SELECT * FROM week WHERE id == ?;', (week,)
    ).fetchone()

    if found_food and not found_week:
        msg = f"Week {week} isn't in the database."
    elif found_week and not found_food:
        msg = f"The food '{food}' isn't in the database."
    else:
        cursor.execute(
            '''
            INSERT INTO week_food (week_id, day_id, food_id)
                VALUES (?, ?, ?);
            ''',
            (week, day, food)
        )
        conn.commit()
        msg = f"The food '{food}' has been sucessfully added to day '{day}' of week {week}."

    conn.close()
    return msg
