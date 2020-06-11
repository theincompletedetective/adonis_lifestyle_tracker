'''Contains functions needed to CRUD data in nutrition database.'''

import sqlite3


def get_food(food_name):
    conn = sqlite3.connect('nutrition.db')
    cursor = conn.cursor()

    cursor.execute(
        f"select * from food where food_name == '{food_name}'"
    )

    # fetchone() returns a tuple
    food_tuple = cursor.fetchone()

    conn.commit()
    conn.close()

    return food_tuple


def add_food(name, kcal, protein):
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


def add_week(total_kcal, total_protein):
    conn = sqlite3.connect('nutrition.db')
    cursor = conn.cursor()

    cursor.execute(
        f'''
        INSERT INTO week (total_kcal, total_protein)
            VALUES ({total_kcal}, {total_protein});
        '''
    )

    conn.commit()
    conn.close()


def get_food_id(food_name):
    '''Gets the ID for a food, from its name.'''
    conn = sqlite3.connect('nutrition.db')
    cursor = conn.cursor()

    cursor.execute(
        f'''
        select id from food where food_name == '{food_name}'
        '''
    )

    # fetchone() returns a tuple
    food_id = cursor.fetchone()[0]

    conn.commit()
    conn.close()

    return food_id


def add_food_to_week(food_id, week_id):
    conn = sqlite3.connect('nutrition.db')
    cursor = conn.cursor()

    cursor.execute(
        f'''
        INSERT INTO food_week (food_id, week_id)
            VALUES ({food_id}, {week_id});
        '''
    )

    conn.commit()
    conn.close()
