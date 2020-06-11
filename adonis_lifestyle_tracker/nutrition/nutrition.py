'''Contains functions needed to CRUD food data in nutrition database.'''

import sqlite3
from copy import deepcopy


def get_food(food_name):
    '''Gets a food's ID, name, calories and protein.'''
    conn = sqlite3.connect('nutrition.db')
    cursor = conn.cursor()

    cursor.execute(
        f"select * from food where food_name == '{food_name}'"
    )

    food_tuple = cursor.fetchone() # id, name, kcal, protein

    conn.commit()
    conn.close()

    return food_tuple


def add_food(name, kcal, protein):
    '''Adds a food to the food database.'''
    conn = sqlite3.connect('nutrition.db')
    cursor = conn.cursor()

    cursor.execute(
        f'''
        INSERT INTO food (food_name, kcal, protein)
            VALUES ('{name}', {kcal}, {protein});
        '''
    )

    conn.commit()
    conn.close()


def add_week(week, total_kcal, total_protein):
    '''Adds a week to the week database.'''
    conn = sqlite3.connect('nutrition.db')
    cursor = conn.cursor()

    cursor.execute(
        f'''
        INSERT INTO week (id, total_kcal, total_protein)
            VALUES ({week}, {total_kcal}, {total_protein});
        '''
    )

    conn.commit()
    conn.close()


def add_food_to_week(food_name, week):
    '''Adds a food to a given week.'''
    conn = sqlite3.connect('nutrition.db')
    cursor = conn.cursor()

    cursor.execute(
        f"select id from food where food_name == '{food_name}'"
    )

    food_id = cursor.fetchone()[0]

    cursor.execute(
        f'''
        INSERT INTO food_week (food_id, week_id)
            VALUES ({food_id}, {week});
        '''
    )

    conn.commit()
    conn.close()


def get_weekly_kcal(week):
    conn = sqlite3.connect('nutrition.db')
    cursor = conn.cursor()

    cursor.execute(
        "select total_kcal from week where id == ?", (week,)
    )

    total_weekly_kcal = cursor.fetchone()[0]

    conn.commit()
    conn.close()

    return total_weekly_kcal


def get_weekly_protein(week):
    conn = sqlite3.connect('nutrition.db')
    cursor = conn.cursor()

    cursor.execute(
        "select total_protein from week where id == ?", (week,)
    )

    total_weekly_protein = cursor.fetchone()[0]

    conn.commit()
    conn.close()

    return total_weekly_protein


def get_kcal_left_for_week(week):
    '''
    Calculates the total number of calories left to consume
    for the week.
    '''
    total_weekly_kcal = get_weekly_kcal(week)

    conn = sqlite3.connect('nutrition.db')
    cursor = conn.cursor()

    # To get all the IDs for the food consumed in a given week
    cursor.execute(
        f"select food_id from food_week where week_id == {week};"
    )

    # To get the number of calories for each food consumed in a given week
    for food_id in cursor.fetchall():
        cursor.execute(
            "select kcal from food where id == ?", food_id
        )

        # To substract the number of calories for all foods consume in a given week
        # from the total number of available calories for that week
        total_weekly_kcal -= cursor.fetchone()[0]

    conn.commit()
    conn.close()

    # To return the number of calories left for the week
    return total_weekly_kcal


def get_protein_left_for_week(week):
    '''
    Calculates the total grams of protein left to consume
    for the week.
    '''
    total_weekly_protein = get_weekly_protein(week)

    conn = sqlite3.connect('nutrition.db')
    cursor = conn.cursor()

    # To get all the IDs for the food consumed in a given week
    cursor.execute(
        f"select food_id from food_week where week_id == {week};"
    )

    # To get the grams of protein for each food consumed in a given week
    for food_id in cursor.fetchall():
        cursor.execute(
            "select protein from food where id == ?", food_id
        )

        # To substract the grams of protein for all foods consume in a given week
        # from the total grams required for that week
        total_weekly_protein -= cursor.fetchone()[0]

    conn.commit()
    conn.close()

    # To return the grams of protein left for the week
    return total_weekly_protein
