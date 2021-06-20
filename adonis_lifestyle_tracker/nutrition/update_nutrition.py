import sqlite3


def update_food(db_path, food, calories=None, protein=None):
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

    food_in_db = cursor.execute('SELECT id FROM food WHERE id = ?', (food,)).fetchone()

    if not food_in_db:
        msg = f"The food '{food}' isn't in the database."
    elif calories and not protein:
        cursor.execute('UPDATE food SET calories = ? WHERE id = ?', (calories, food))
        db.commit()
        msg = f"The calories for food '{food}' have been updated to {calories}."
    elif protein and not calories:
        cursor.execute('UPDATE food SET protein = ? WHERE id = ?', (protein, food))
        db.commit()
        msg = f"The grams of protein for food '{food}' have been updated to {protein}."
    else:
        cursor.execute('UPDATE food SET calories = ? WHERE id = ?', (calories, food))
        cursor.execute('UPDATE food SET protein = ? WHERE id = ?', (protein, food))
        db.commit()
        msg = (
            f"The calories for food '{food}' have been updated to {calories}, "
            f"and its grams of protein has been updated to {protein}."
        )

    db.close()
    return msg
