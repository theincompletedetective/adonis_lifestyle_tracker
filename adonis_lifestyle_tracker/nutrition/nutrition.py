'''Contains the functions needed to CRUD food data in the nutrition database.'''
import sqlite3


def get_food(food_name):
    '''Gets a food's calories and protein from the nutrition database.'''
    conn = sqlite3.connect('nutrition.db')
    cursor = conn.cursor()

    cursor.execute(
        '''
        SELECT kcal, protein FROM food
            WHERE food_name == ?;
        ''',
        (food_name,)
    )

    food_tuple = cursor.fetchone() # id, kcal, protein

    conn.commit()
    conn.close()

    return food_tuple


def add_food(food_name, kcal, protein):
    '''Adds a food's name, calories and protein to the nutrition database.'''
    conn = sqlite3.connect('nutrition.db')
    cursor = conn.cursor()

    cursor.execute(
        '''
        INSERT INTO food (food_name, kcal, protein)
            VALUES (?, ?, ?);
        ''',
        (food_name, kcal, protein)
    )

    conn.commit()
    conn.close()


def update_food_name(old_food_name, new_food_name):
    '''Updates the name of a food in the nutrition database.'''
    conn = sqlite3.connect('nutrition.db')
    cursor = conn.cursor()

    cursor.execute(
        '''
        UPDATE food SET food_name = ?
            WHERE food_name = ?;
        ''',
        (new_food_name, old_food_name)
    )

    conn.commit()
    conn.close()


def add_week(week, total_kcal, total_protein):
    '''Adds a week to the week database.'''
    conn = sqlite3.connect('nutrition.db')
    cursor = conn.cursor()

    cursor.execute(
        '''
        INSERT INTO week (id, total_kcal, total_protein)
            VALUES (?, ?, ?);
        ''',
        (week, total_kcal, total_protein)
    )

    conn.commit()
    conn.close()


def add_food_to_week(food_name, week):
    '''Adds a food to a given week.'''
    conn = sqlite3.connect('nutrition.db')
    cursor = conn.cursor()

    # To get the name for the provided food
    cursor.execute(
        "SELECT food_name FROM food WHERE food_name == ?;", (food_name,)
    )

    # To add the food's name to the food_week relation table
    cursor.execute(
        '''
        INSERT INTO food_week (food_name, week_id)
            VALUES (?, ?);
        ''',
        (cursor.fetchone()[0], week)
    )

    conn.commit()
    conn.close()


def get_weekly_kcal(week):
    conn = sqlite3.connect('nutrition.db')
    cursor = conn.cursor()

    cursor.execute(
        "SELECT total_kcal FROM week WHERE id == ?;", (week,)
    )

    total_weekly_kcal = cursor.fetchone()[0]

    conn.commit()
    conn.close()

    return total_weekly_kcal


def get_weekly_protein(week):
    conn = sqlite3.connect('nutrition.db')
    cursor = conn.cursor()

    cursor.execute(
        "SELECT total_protein FROM week WHERE id == ?", (week,)
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

    # To get all the names for the food consumed in a given week
    cursor.execute(
        "SELECT food_name FROM food_week WHERE week_id == ?;", (week,)
    )

    # To get the number of calories for each food consumed in a given week
    for food_name_tuple in cursor.fetchall():
        cursor.execute(
            "SELECT kcal FROM food WHERE food_name == ?;", (food_name_tuple[0],)
        )

        # To substract the number of calories for all foods consume in a given week
        # from the total number of available calories for that week
        total_weekly_kcal -= cursor.fetchone()[0]

    conn.commit()
    conn.close()

    # To return the number of calories left for the week
    if total_weekly_kcal >= 0:
        return total_weekly_kcal
    else:
        return 0


def get_protein_left_for_week(week):
    '''
    Calculates the total grams of protein left to consume
    for the week.
    '''
    total_weekly_protein = get_weekly_protein(week)

    conn = sqlite3.connect('nutrition.db')
    cursor = conn.cursor()

    # To get all the names for the food consumed in a given week
    cursor.execute(
        "SELECT food_name FROM food_week WHERE week_id = ?;", (week,)
    )

    # To get the grams of protein for each food consumed in a given week
    for food_name_tuple in cursor.fetchall():
        cursor.execute(
            "SELECT protein FROM food WHERE food_name = ?;", (food_name_tuple[0],)
        )

        # To substract the grams of protein for all foods consume in a given week
        # from the total grams required for that week
        total_weekly_protein -= cursor.fetchone()[0]

    conn.commit()
    conn.close()

    # To return the grams of protein left for the week
    if total_weekly_protein >= 0:
        return total_weekly_protein
    else:
        return 0
