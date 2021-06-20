import sqlite3
from sqlite3 import IntegrityError


def add_equipment(db_path, equipment):
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

    try:
        cursor.execute('INSERT INTO equipment (id) VALUES (?)', (equipment,))
    except IntegrityError:
        return f"The '{equipment}' equipment is already in the database."
    else:
        db.commit()
        return f"The '{equipment}' equipment has been successfully added to the database."
    finally:
        db.close()


def add_exercise(db_path, exercise, equipment):
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

    equipment_in_db = cursor.execute('SELECT id FROM equipment WHERE id = ?', (equipment,)).fetchone()

    if equipment_in_db:
        try:
            cursor.execute('INSERT INTO exercise (id, equipment_id) VALUES (?, ?)', (exercise, equipment))
        except IntegrityError:
            msg = f"The '{exercise}' exercise is already in the database."
        else:
            db.commit()
            msg = (
                f"The '{exercise}' exercise with the '{equipment}' equipment has been successfully added to the database."
            )
    else:
        msg = f"The '{equipment}' equipment is not in the database."

    db.close()
    return msg
