'''Contains the functions needed to CRUD food data in the nutrition database.'''
import sqlite3
from sqlite3 import IntegrityError
import click


def get_weekly_kcal(week):
    conn = sqlite3.connect('nutrition.db')
    cursor = conn.cursor()

    cursor.execute(
        "SELECT total_kcal FROM week WHERE id == ?;", (week,)
    )

    try:
        total_weekly_kcal = cursor.fetchone()[0]
    except TypeError:
        print(f'Week {week} is not in the nutrition database!')
    else:
        conn.commit()
        return total_weekly_kcal
    finally:
        conn.close()


def get_weekly_protein(week):
    conn = sqlite3.connect('nutrition.db')
    cursor = conn.cursor()

    cursor.execute(
        "SELECT total_protein FROM week WHERE id == ?", (week,)
    )

    try:
        total_weekly_protein = cursor.fetchone()[0]
    except TypeError:
        print(f'Week {week} is not in the nutrition database!')
    else:
        conn.commit()
        return total_weekly_protein
    finally:
        conn.close()


@click.command()
@click.option('-f', '--food', required=True, help='Name of the food.')
def get_food(food):
    '''Gets a food's calories and protein from the nutrition database.'''
    conn = sqlite3.connect('nutrition.db')
    cursor = conn.cursor()

    try:
        cursor.execute(
            'SELECT kcal, protein FROM food WHERE food == ?;', (food,)
        )
        kcal, protein = cursor.fetchone()[1:] # id, kcal, protein
        print(f'{food} has {kcal} calories, and {protein} grams of protein.')
    except TypeError:
        print(f"The food '{food}' is not currently in the nutrition database!")
    finally:
        conn.close()


@click.command()
@click.option('-f', '--food', required=True, help='Name of the food.')
@click.option('-k', '--kcal', required=True, type=int, help='Number of calories in the food.')
@click.option('-p', '--protein', required=True, type=int, help='Number of grams of protein in the food.')
def add_food(food, kcal, protein):
    '''Adds the food with the specified calories and protein to the database.'''
    conn = sqlite3.connect('nutrition.db')
    cursor = conn.cursor()

    try:
        cursor.execute(
            '''
            INSERT INTO food (food, kcal, protein)
                VALUES (?, ?, ?);
            ''',
            (food, kcal, protein)
        )
    except IntegrityError:
        print('You cannot add two foods with the same name to the database!')
    else:
        print(f'The food "{food}" has been successfully added to the nutrition database!')
        conn.commit()
    finally:
        conn.close()


@click.command()
@click.option('-w', '--week', required=True, type=int, help='Week number to add.')
@click.option('-k', '--total-kcal', required=True, type=int, help='Total number of calories for the week.')
@click.option('-p', '--total-protein', required=True, type=int, help='Total number of grams of protein for the week.')
def add_week(week, total_kcal, total_protein):
    '''Adds a week to the week table in the nutrition database.'''
    conn = sqlite3.connect('nutrition.db')
    cursor = conn.cursor()

    try:
        cursor.execute(
            '''
            INSERT INTO week (id, total_kcal, total_protein)
                VALUES (?, ?, ?);
            ''',
            (week, total_kcal, total_protein)
        )
    except IntegrityError:
        print(f'Week {week} is already in the nurition database!')
    else:
        print(
            f'Week {week} has been added to the database, '
            f'with {total_kcal} total calories, and {total_protein} total grams of protein.'
        )
        conn.commit()
    finally:
        conn.close()


@click.command()
@click.option('-f', '--food', required=True, help='Name of the food.')
@click.option('-w', '--week', required=True, type=int, help='Week number to which to add a food.')
def add_food_to_week(food, week):
    '''Adds a food and week to the food_week table in the nutrition database.'''
    conn = sqlite3.connect('nutrition.db')
    cursor = conn.cursor()

    # To make sure food and week are already in the database
    cursor.execute( 'SELECT * FROM food WHERE food == ?;', (food,) )
    found_food = cursor.fetchone()

    cursor.execute( 'SELECT * FROM week WHERE id == ?;', (week,) )
    found_week = cursor.fetchone()

    if found_food and not found_week:
        print(f'Week {week} is not in the nutrition database!')
    elif found_week and not found_food:
        print(f'The food "{food}" is not in the nutrition database!')
    else:
        cursor.execute(
            'INSERT INTO food_week (food, week) VALUES (?, ?);',
            (food, week)
        )
        conn.commit()
        conn.close()
        print(f'The food "{food}" has been added to week {week}.')


@click.command()
@click.option('-w', '--week', required=True, type=int, help='Week number for which to get calories.')
def get_weekly_kcal_left(week):
    '''
    Calculates the total number of calories left to consume
    for the week.
    '''
    total_weekly_kcal = get_weekly_kcal(week)

    conn = sqlite3.connect('nutrition.db')
    cursor = conn.cursor()

    # To get all the names for the food consumed in a given week
    cursor.execute(
        "SELECT food FROM food_week WHERE week == ?;", (week,)
    )

    # To get the number of calories for each food consumed in a given week
    for food_name_tuple in cursor.fetchall():
        cursor.execute(
            "SELECT kcal FROM food WHERE food == ?;", (food_name_tuple[0],)
        )

        # To substract the grams of protein for each food consumed in the week
        total_weekly_kcal -= cursor.fetchone()[0]

    conn.commit()
    conn.close()

    if total_weekly_kcal >= 0:
        print(f'You have {total_weekly_kcal} calories left for the week.')
    else:
        print('You have zero calories left for the week!')


@click.command()
@click.option('-w', '--week', required=True, type=int, help='Week number for which to get protein.')
def get_weekly_protein_left(week):
    '''
    Calculates the total grams of protein left to consume
    for the week.
    '''
    total_weekly_protein = get_weekly_protein(week)

    conn = sqlite3.connect('nutrition.db')
    cursor = conn.cursor()

    # To get all the names for the food consumed in a given week
    cursor.execute(
        "SELECT food FROM food_week WHERE week = ?;", (week,)
    )

    # To get the grams of protein for each food consumed in a given week
    for food_name_tuple in cursor.fetchall():
        cursor.execute(
            "SELECT protein FROM food WHERE food = ?;", (food_name_tuple[0],)
        )

        # To substract the grams of protein for each food consumed in the week
        total_weekly_protein -= cursor.fetchone()[0]

    conn.commit()
    conn.close()

    if total_weekly_protein >= 0:
        print(f'You have {total_weekly_protein} grams of protein left for the week.')
    else:
        print(f'You have zero grams of protein left for the week!')
