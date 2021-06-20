import sqlite3


def delete_food(db_path, food):
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

    food_in_db = cursor.execute('SELECT id FROM food WHERE id = ?', (food,)).fetchone()

    if not food_in_db:
        msg = f"The food '{food}' isn't in the database."
    else:
        cursor.execute( 'DELETE FROM food WHERE id = ?', (food,) )
        cursor.execute( 'DELETE FROM week_food WHERE food_id = ?', (food,) )
        db.commit()
        msg = f"The food '{food}' has been deleted from the database."

    db.close()
    return msg


def delete_week(db_path, week):
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

    week_in_db = cursor.execute('SELECT id FROM week WHERE id = ?', (week,)).fetchone()

    if not week_in_db:
        msg = f"Week {week} isn't in the database."
    else:
        cursor.execute( 'DELETE FROM week WHERE id = ?', (week,) )
        cursor.execute( 'DELETE FROM week_food WHERE week_id = ?', (week,) )
        db.commit()
        msg = f"Week {week} has been deleted from the database."

    db.close()
    return msg
