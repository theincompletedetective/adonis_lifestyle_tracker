'''Contains the functions needed to CRUD food data in the nutrition database.'''
import sqlite3
from sqlite3 import IntegrityError


def add_food(db_path, food, calories, protein):
    '''Adds the food with the specified calories and protein to the database.'''
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
        return f'The food "{food}" is already in the database.'
    else:
        conn.commit()
        return (
            f'The food "{food}", with {calories} calories and {protein} grams of protein '
            'has been successfully added to the nutrition database.'
        )
    finally:
        conn.close()


def add_totals_to_week(db_path, week, total_calories, total_protein):
    '''
    Adds a week, total calories, and total protein to the week table in the nutrition database.
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
        return f'Week {week} is already in the nurition database.'
    else:
        conn.commit()
        return (
            f'Week {week} has been successfully added to the nutrition database, '
            f'with {total_calories} total calories, and {total_protein} total grams of protein.'
        )
    finally:
        conn.close()


def add_food_to_week(db_path, food, week):
    '''Adds a week and food to the week_food table in the nutrition database.'''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # To make sure food and week are already in the database
    found_food = cursor.execute( 'SELECT * FROM food WHERE id == ?;', (food,) ).fetchone()
    found_week = cursor.execute( 'SELECT * FROM week WHERE id == ?;', (week,) ).fetchone()

    if found_food and not found_week:
        msg = f'Week {week} is not in the nutrition database.'
    elif found_week and not found_food:
        msg =  f'The food "{food}" is not in the nutrition database.'
    else:
        cursor.execute(
            'INSERT INTO week_food (week_id, food_id) VALUES (?, ?);',
            (week, food)
        )
        conn.commit()
        msg = f'The food "{food}" has been added to week {week}.'

    conn.close()
    return msg


def get_food(db_path, food):
    '''Gets a food's calories and protein from the nutrition database.'''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(
        'SELECT calories, protein FROM food WHERE id == ?;', (food,)
    )

    try:
        calories, protein = cursor.fetchone()
    except TypeError:
        return f"The food '{food}' isn't in the nutrition database."
    else:
        return f'The food "{food}" has {calories} calories, and {protein} grams of protein.'
    finally:
        conn.close()


def get_calories_left(db_path, week):
    '''
    Calculates the total number of calories left to consume
    for the week.
    '''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        total_weekly_calories = cursor.execute(
            "SELECT total_calories FROM week WHERE id == ?;", (week,)
        ).fetchone()[0]
    except TypeError:
        print(f'Week {week} is not in the nutrition database.')
    else:
        # To get all the names for the food consumed in a given week
        cursor.execute(
            "SELECT food_id FROM week_food WHERE week_id == ?;", (week,)
        )

        # To get the number of calories for each food consumed in a given week
        for food_name_tuple in cursor.fetchall():
            cursor.execute(
                "SELECT calories FROM food WHERE id == ?;", (food_name_tuple[0],)
            )

            # To substract the grams of protein for each food consumed in the week
            total_weekly_calories -= cursor.fetchone()[0]

        conn.commit()
        conn.close()

        if total_weekly_calories >= 0:
            return f'You have {total_weekly_calories} calories left for the week.'
        else:
            return 'You have zero calories left for the week!'


def get_protein_left(db_path, week):
    '''
    Calculates the total grams of protein left to consume
    for the week.
    '''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        total_weekly_protein = cursor.execute(
            "SELECT total_protein FROM week WHERE id == ?", (week,)
        ).fetchone()[0]
    except TypeError:
        print(f"Week {week} is not in the nutrition database.")
    else:
        # To get all the names for the food consumed in a given week
        cursor.execute(
            "SELECT food_id FROM week_food WHERE week_id = ?;", (week,)
        )

        # To get the grams of protein for each food consumed in a given week
        for food_name_tuple in cursor.fetchall():
            cursor.execute(
                "SELECT protein FROM food WHERE id = ?;", (food_name_tuple[0],)
            )

            # To substract the grams of protein for each food consumed in the week
            total_weekly_protein -= cursor.fetchone()[0]

        conn.commit()
        conn.close()

        if total_weekly_protein >= 0:
            return f'You still have to eat {total_weekly_protein} more grams of protein for the week.'
        else:
            return f'You have eaten all the grams of protein needed for the week!'
