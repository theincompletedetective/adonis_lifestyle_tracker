import sqlite3
from sqlite3 import IntegrityError


def add_food(db_path, food, calories, protein):
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

    try:
        cursor.execute('INSERT INTO food (id, calories, protein) VALUES (?, ?, ?);', (food, calories, protein))
    except IntegrityError:
        return f"The food '{food}' is already in the database."
    else:
        db.commit()
        return (
            f"The food '{food}' has been successfully added to the database, "
            f"with {calories} calories and {protein} grams of protein."
        )
    finally:
        db.close()


def add_total_calories_and_protein_for_week(db_path, week, total_calories, total_protein):
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

    try:
        cursor.execute(
            'INSERT INTO week (id, total_calories, total_protein) VALUES (?, ?, ?);',
            (week, total_calories, total_protein)
        )
    except IntegrityError:
        return f'Week {week} is already in the database.'
    else:
        db.commit()
        return (
            f'Week {week} has been successfully added to the database, '
            f'with {total_calories} total calories, and {total_protein} total grams of protein.'
        )
    finally:
        db.close()


def add_food_to_day_of_week(db_path, day, week_day, week, food):
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

    found_food = cursor.execute('SELECT * FROM food WHERE id == ?;', (food,)).fetchone()
    found_week = cursor.execute('SELECT * FROM week WHERE id == ?;', (week,)).fetchone()

    if found_food and not found_week:
        msg = f"Week {week} isn't in the database."
    elif found_week and not found_food:
        msg = f"The food '{food}' isn't in the database."
    else:
        cursor.execute('INSERT INTO week_day (week_id, ?) VALUES (?, ?);', (week_day, week, day))
        db.commit()
        msg = f"Food '{food}' has been successfully added to {week_day} of week {week}."

    db.close()
    return msg


def add_food_to_week(db_path, week_day, week, food, quantity=1):
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

    found_food = cursor.execute('SELECT * FROM food WHERE id == ?;', (food,)).fetchone()
    found_week = cursor.execute('SELECT * FROM week WHERE id == ?;', (week,)).fetchone()

    if found_food and not found_week:
        msg = f"Week {week} isn't in the database."
    elif found_week and not found_food:
        msg = f"The food '{food}' isn't in the database."
    else:
        for i in range(quantity):
            cursor.execute('INSERT INTO week_food (week_id, week_day, food_id) VALUES (?, ?);', (week, week_day, food))

        db.commit()
        msg = f"{quantity} of food '{food}' has been successfully added to {week_day} of week {week}."

    db.close()
    return msg
