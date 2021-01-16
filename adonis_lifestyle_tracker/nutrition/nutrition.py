'''Contains the functions needed to CRUD food data in the nutrition database.'''
import sqlite3
from sqlite3 import IntegrityError
import click
from adonis_lifestyle_tracker.config import NUTRITION_DB_PATH


@click.command()
@click.option('-f', '--food', required=True, help='Name of the food.')
@click.option('-k', '--calories', required=True, type=int, help='Calories in the food.')
@click.option('-p', '--protein', required=True, type=int, help='Grams of protein in the food.')
def add_food(food, calories, protein):
    '''Adds the food with the specified calories and protein to the database.'''
    conn = sqlite3.connect(NUTRITION_DB_PATH)
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
        print(f'The food "{food}" is already in the database.')
    else:
        conn.commit()
        print(
            f'The food "{food}", with {calories} calories and {protein} grams of protein '
            'has been successfully added to the nutrition database.'
        )
    finally:
        conn.close()


@click.command()
@click.option('-w', '--week', required=True, type=int, help='Week number.')
@click.option('-k', '--total-calories', required=True, type=int, help='Nmber of calories for the week.')
@click.option('-p', '--total-protein', required=True, type=int, help='Number of grams of protein for the week.')
def add_totals_to_week(week, total_calories, total_protein):
    '''
    Adds a week, total calories, and total protein to the week table in the nutrition database.
    '''
    conn = sqlite3.connect(NUTRITION_DB_PATH)
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
        print(f'Week {week} is already in the nurition database.')
    else:
        conn.commit()
        print(
            f'Week {week} has been successfully added to the nutrition database, '
            f'with {total_calories} total calories, and {total_protein} total grams of protein.'
        )
    finally:
        conn.close()


@click.command()
@click.option('-f', '--food', required=True, help='Name of the food.')
@click.option('-w', '--week', required=True, type=int, help='Week number.')
def add_food_to_week(food, week):
    '''Adds a week and food to the week_food table in the nutrition database.'''
    conn = sqlite3.connect(NUTRITION_DB_PATH)
    cursor = conn.cursor()

    # To make sure food and week are already in the database
    found_food = cursor.execute( 'SELECT * FROM food WHERE id == ?;', (food,) ).fetchone()
    found_week = cursor.execute( 'SELECT * FROM week WHERE id == ?;', (week,) ).fetchone()

    if found_food and not found_week:
        print(f'Week {week} is not in the nutrition database.')
    elif found_week and not found_food:
        print(f'The food "{food}" is not in the nutrition database.')
    else:
        cursor.execute(
            'INSERT INTO week_food (week_id, food_id) VALUES (?, ?);',
            (week, food)
        )
        conn.commit()
        print(f'The food "{food}" has been added to week {week}.')

    conn.close()


@click.command()
@click.argument('food')
def get_food(food):
    '''Gets a food's calories and protein from the nutrition database.'''
    conn = sqlite3.connect(NUTRITION_DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        'SELECT calories, protein FROM food WHERE id == ?;', (food,)
    )

    try:
        calories, protein = cursor.fetchone()
    except TypeError:
        print(f"The food '{food}' isn't in the nutrition database.")
    else:
        print(f'The food "{food}" has {calories} calories, and {protein} grams of protein.')
    finally:
        conn.close()


@click.command()
@click.argument('week', type=int)
def get_calories_left(week):
    '''
    Calculates the total number of calories left to consume
    for the week.
    '''
    conn = sqlite3.connect(NUTRITION_DB_PATH)
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
            print(f'You have {total_weekly_calories} calories left for the week.')
        else:
            print('You have zero calories left for the week!')


@click.command()
@click.argument('week', type=int)
def get_protein_left(week):
    '''
    Calculates the total grams of protein left to consume
    for the week.
    '''
    conn = sqlite3.connect(NUTRITION_DB_PATH)
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
            print(f'You have {total_weekly_protein} grams of protein left for the week.')
        else:
            print(f'You have zero grams of protein left for the week!')
