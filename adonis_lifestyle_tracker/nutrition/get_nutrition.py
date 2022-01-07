import sqlite3


def get_calories_and_protein_for_food(db_path, food):
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

    cursor.execute('SELECT calories, protein FROM food WHERE id == ?;', (food,))

    try:
        calories, protein = cursor.fetchone()
    except TypeError:
        return f"The food '{food}' isn't in the database."
    else:
        return f"The food '{food}' has {calories} calories and {protein} grams of protein."
    finally:
        db.close()


def get_total_calories_for_week(db_path, week):
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

    try:
        total_calories = cursor.execute("SELECT total_calories FROM week WHERE id == ?;", (week,)).fetchone()[0]
    except TypeError:
        return f"Week {week} isn't in the database."
    else:
        db.close()
        return f'Week {week} has {total_calories} total calories.'


def get_total_protein_for_week(db_path, week):
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

    try:
        total_protein = cursor.execute("SELECT total_protein FROM week WHERE id == ?;", (week,)).fetchone()[0]
    except TypeError:
        return f"Week {week} isn't in the database."
    else:
        db.close()
        return f'Week {week} has {total_protein} total grams of protein.'


def get_calories_left_for_week(db_path, week):
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

    try:
        total_calories = cursor.execute("SELECT total_calories FROM week WHERE id == ?;", (week,)).fetchone()[0]
    except TypeError:
        return f"Week {week} isn't in the database."
    else:
        cursor.execute("SELECT food_id FROM week_food WHERE week_id == ?;", (week,))

        for food_name_tuple in cursor.fetchall():
            cursor.execute("SELECT calories FROM food WHERE id == ?;", (food_name_tuple[0],))
            total_calories -= cursor.fetchone()[0]

        db.close()
        return f'You have {total_calories} calories left to eat for week {week}.'


def get_protein_left_for_week(db_path, week):
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

    try:
        total_protein = cursor.execute("SELECT total_protein FROM week WHERE id == ?", (week,)).fetchone()[0]
    except TypeError:
        return f"Week {week} isn't in the database."
    else:
        cursor.execute("SELECT food_id FROM week_food WHERE week_id = ?;", (week,))

        for food_name_tuple in cursor.fetchall():
            cursor.execute("SELECT protein FROM food WHERE id = ?;", (food_name_tuple[0],))
            total_protein -= cursor.fetchone()[0]

        db.close()

        if total_protein > 0:
            return f'You need to eat {total_protein} more grams of protein for week {week}.'
        else:
            return f'You have reached your protein goal for week {week}!'


def get_calories_eaten_for_weekday(db_path, weekday, week):
    db = sqlite3.connect(db_path)
    cursor = db.cursor()
    cursor.execute("SELECT food_id FROM week_food WHERE week_id == ? AND weekday == ?;", (week, weekday))

    calories_eaten = 0

    for food_name_tuple in cursor.fetchall():
        cursor.execute("SELECT calories FROM food WHERE id = ?;", (food_name_tuple[0],))
        calories_eaten += cursor.fetchone()[0]

    db.close()
    return f'You have eaten {calories_eaten} calories on {weekday}, for week {week}.'


def get_date_for_weekday(db_path, weekday, week):
    db = sqlite3.connect(db_path)
    cursor = db.cursor()
    cursor.execute(f"SELECT {weekday} FROM weekday WHERE week_id == ?;", (week,))
    date = cursor.fetchone()[0]
    db.close()
    return f'The date for {weekday} of week {week} is {date}.'
