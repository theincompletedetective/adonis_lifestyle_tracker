import sqlite3


def get_equipment(db_path, exercise):
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

    cursor.execute('SELECT equipment_id FROM exercise WHERE id = ?', (exercise,))

    try:
        return cursor.fetchone()[0]
    except TypeError:
        return f"The '{exercise}' exercise isn't in the database."
    finally:
        db.close()


def get_resistance(db_path, exercise, reps):
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

    cursor.execute(f'SELECT reps{reps} FROM exercise WHERE id = ?', (exercise,))

    try:
        return cursor.fetchone()[0]
    except TypeError:
        return f"The '{exercise}' exercise isn't in the database."
    finally:
        db.close()
