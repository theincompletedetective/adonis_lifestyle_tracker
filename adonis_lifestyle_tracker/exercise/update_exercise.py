import sqlite3


def update_resistance(db_path, exercise, reps, new_resistance):
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

    exercise_in_db = cursor.execute('SELECT id from exercise WHERE id = ?', (exercise,)).fetchone()

    if exercise_in_db:
        cursor.execute(f'UPDATE exercise SET reps{reps} = ?', (new_resistance,))
        db.commit()
        msg = (
            f"The resistance for the '{exercise}' exercise and {reps} reps has been successfully updated to '{new_resistance}'."
        )
    else:
        msg = f"The '{exercise}' exercise is not in the database."

    db.close()
    return msg


def update_equipment(db_path, exercise, new_equipment):
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

    equipment_in_db = cursor.execute('SELECT id FROM equipment WHERE id = ?', (new_equipment,)).fetchone()

    if equipment_in_db:
        cursor.execute('UPDATE exercise SET equipment_id = ? WHERE id = ?', (new_equipment, exercise))
        db.commit()
        msg = f"The equipment for the '{exercise}' exercise has been successfully updated to '{new_equipment}'."
    else:
        msg = f"The '{new_equipment}' equipment is not in the database."

    db.close()
    return msg
