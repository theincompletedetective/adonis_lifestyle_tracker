import sqlite3


def update_food(db_path, food, calories=None, protein=None):
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

    food_in_db = cursor.execute('SELECT id FROM food WHERE id = ?', (food,)).fetchone()

    has_calories = calories is not None and calories > 0
    has_protein = protein is not None and protein >= 0

    if not food_in_db:
        msg = f"The food '{food}' isn't in the database."
    elif has_calories and not has_protein:
        cursor.execute('UPDATE food SET calories = ? WHERE id = ?', (calories, food))
        db.commit()
        msg = f"The calories for food '{food}' have been updated to {calories}."
    elif has_protein and not has_calories:
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
