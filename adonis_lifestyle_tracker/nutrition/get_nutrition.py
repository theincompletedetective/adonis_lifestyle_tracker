'''Contains the functions needed to get nutrition information from the database.'''
import sqlite3


def get_food(db_path, food):
    '''Gets a food's calories and protein from the food table in the database.'''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(
        'SELECT calories, protein FROM food WHERE id == ?;', (food,)
    )

    try:
        calories, protein = cursor.fetchone()
    except TypeError:
        return f"The food '{food}' isn't in the database."
    else:
        return f'The food "{food}" has {calories} calories and {protein} grams of protein.'
    finally:
        conn.close()


def get_calories_left(db_path, week):
    '''
    Gets the total number of calories left to consume for the specified week.
    '''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        total_weekly_calories = cursor.execute(
            "SELECT total_calories FROM week WHERE id == ?;", (week,)
        ).fetchone()[0]
    except TypeError:
        return f'Week {week} is not in the database.'
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
    Gets the total grams of protein left to consume for the specified week.
    '''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        total_weekly_protein = cursor.execute(
            "SELECT total_protein FROM week WHERE id == ?", (week,)
        ).fetchone()[0]
    except TypeError:
        return f"Week {week} is not in the database."
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