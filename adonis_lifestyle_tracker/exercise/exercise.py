'''
Contains the functions needed to add exercise information to the database.
'''
import sqlite3
from sqlite3 import IntegrityError
import click
from adonis_lifestyle_tracker.config import EXERCISE_DB_PATH


def check_db(cursor, table, value):
    '''
    Checks to see whether or not the provided value is in the specified database table.
    '''
    return cursor.execute(
        f'SELECT * FROM {table} WHERE id = ?', (value,)
    ).fetchone()


@click.command()
@click.argument('week', type=int)
def add_week(week):
    '''Adds the specified week to exercise database.'''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute( 'INSERT INTO week (id) VALUES (?)', (week,) )
    except IntegrityError:
        print(f"Week {week} is already in the exercise database.")
    else:
        conn.commit()
        print(
            f"Week {week} has been successfully added to the exercise database."
        )
    finally:
        conn.close()


@click.command()
@click.argument('equipment')
def add_equipment(equipment):
    '''Adds the specified equipment to the exercise database.'''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute(
            'INSERT INTO equipment (id) VALUES (?)', (equipment,)
        )
    except IntegrityError:
        print(f"The '{equipment}' equipment is already in the database.")
    else:
        conn.commit()
        print(
            f"The '{equipment}' equipment has been successfully added to the database."
        )
    finally:
        conn.close()


@click.command()
@click.argument('exercise')
@click.argument('equipment')
def add_exercise(exercise, equipment):
    '''
    Adds the specified exercise and its equipment to the exercise database.
    '''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    # To make sure that the equipment is already in the database
    equipment_in_db = check_db(cursor, 'equipment', equipment)

    if equipment_in_db:
        try:
            cursor.execute(
                'INSERT INTO exercise (id, equipment_id) VALUES (?, ?)',
                (exercise, equipment)
            )
        except IntegrityError:
            print(f"The '{exercise}' exercise is already in the database.")
        else:
            conn.commit()
            print(f"The '{exercise}' exercise has been successfully added to the database.")

    else:
        print(f"The '{equipment}' equipment needs to be added to the database.")

    conn.close()


@click.command()
@click.argument('reps', type=int)
def add_reps(reps):
    '''Adds the specified reps to the exercise database.'''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute(
            'INSERT INTO reps (id) VALUES (?)', (reps,)
        )
    except IntegrityError:
        print(f"{reps} reps is already in the database.")
    else:
        conn.commit()
        print(
            f"{reps} reps has been successfully added to the database."
        )
    finally:
        conn.close()


@click.command()
@click.argument('resistance')
def add_resistance(resistance):
    '''Adds the specified resistance to the exercise database.'''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute(
            'INSERT INTO resistance (id) VALUES (?)', (resistance,)
        )
    except IntegrityError:
        print(f"'{resistance}' resistance is already in the database.")
    else:
        conn.commit()
        print(
            f"'{resistance}' resistance has been successfully added to the database."
        )
    finally:
        conn.close()


@click.command()
@click.option('-w', '--week', required=True, type=int, help='Week number.')
@click.option('-e', '--exercise', required=True, help='Name of the exercise.')
@click.option('--reps', required=True, type=int, help='Number of repetitions of a given exercise.')
@click.option('-r', '--resistance', required=True, help='Amount of resistance for a given exercise.')
def add_exercse_to_week(week, exercise, reps, resistance):
    '''
    Adds the specified exercise, reps, and resistance to the provided week in the exercise database.
    '''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    # To make sure the week is in the database
    week_in_db = check_db(cursor, 'week', week)

    # To make sure the exercise is in the database
    exercise_in_db = check_db(cursor, 'exercise', exercise)

    # To make sure the reps are in the database
    reps_in_db = check_db(cursor, 'reps', reps)

    # To make sure the resistance is in the database
    resistance_in_db = check_db(cursor, 'resistance', resistance)

    if not week_in_db:
      print(f"Week {week} needs to be added to the database.")
    elif not exercise_in_db:
      print(f"The '{exercise}' exercise needs to be added to the database.")
    elif not reps_in_db:
      print(f"{reps} reps needs to be added to the database.")
    elif not resistance_in_db:
      print(f"'{resistance}' resistance needs to be added to the database.")
    else:
        try:
            cursor.execute(
                '''
                INSERT INTO week_exercise
                    (week_id, exercise_id, reps_id, resistance_id)
                VALUES(?, ?, ?, ?)
                ''',
                (week, exercise, reps, resistance)
            )
        except IntegrityError:
            print(
                f"Week {week} with the '{exercise}' exercise, '{reps}' reps, "
                f"and '{resistance}' resistance is already in the the database."
            )
        else:
            conn.commit()
            print(
                f"Week {week} with the '{exercise}' exercise, '{reps}' reps, "
                f"and '{resistance}' resistance has been successfully added to the database."
            )

    conn.close()


@click.command()
@click.argument('exercise')
def get_equipment(exercise):
    '''Gets the equipment for the specified exercise in the database.'''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    cursor.execute( 'SELECT equipment_id FROM exercise WHERE id = ?', (exercise,) )

    try:
        print(cursor.fetchone()[0])
    except TypeError:
        print(f"The '{exercise}' exercise is not in the database!")
    finally:
        conn.close()


@click.command()
@click.option('-w', '--week', required=True, type=int, help='Week number.')
@click.option('-e', '--exercise', required=True, help='Name of the exercise.')
@click.option('-r', '--reps', required=True, type=int, help='Number of repetitions of a given exercise.')
def get_resistance(week, exercise, reps):
    '''Gets the resistance for the specified week, exercise, and reps, in the exercise database.'''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        '''
        SELECT resistance_id
        FROM week_exercise
        WHERE week_id = ?
        AND exercise_id = ?
        AND reps_id = ?
        ''',
        (week, exercise, reps)
    )

    try:
        print(cursor.fetchone()[0])
    except TypeError:
        print(
            f"Week {week} with the '{exercise}' exercise and {reps} reps is not in the database."
        )
    finally:
        conn.close()


@click.command()
@click.option('-o', '--old-equipment', required=True, help='Equipment currently in the database')
@click.option('-n', '--new-equipment', required=True, help='New name for equipment in the database')
def update_equipment(old_equipment, new_equipment):
    '''Changes the name of the specified equipment in the exercise database.'''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    # To make sure that new equipment isn't already in the database
    new_equipment_in_db = check_db(cursor, 'equipment', new_equipment)

    if new_equipment_in_db:
        print(f"The '{new_equipment}' equipment is already in the database.")
    else:
        try:
            cursor.execute(
                'UPDATE equipment SET id = ? WHERE id = ?',
                (new_equipment, old_equipment)
            )
        except IntegrityError:
            print(f"The '{old_equipment}' equipment is not in the database.")
        else:
            # To change the equipment for all exercises that use it
            cursor.execute(
                '''
                UPDATE exercise SET equipment_id = ? WHERE equipment_id = ?
                ''',
                (new_equipment, old_equipment)
            )
            conn.commit()
            print(f"The '{old_equipment}' equipment has been updated to '{new_equipment}'.")

    conn.close()


@click.command()
@click.option('-o', '--old-exercise', required=True, help='Exercise currently in the database')
@click.option('-n', '--new-exercise', required=True, help='New name for exercise in the database')
def update_exercise(old_exercise, new_exercise):
    '''Changes the name of the specified exercise in the database.'''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    # To make sure that new exercise isn't already in the database
    new_exercise_in_db = check_db(cursor, 'exercise', new_exercise)

    if new_exercise_in_db:
        print(f"The '{new_exercise}' exercise is already in the database.")
    else:
        try:
            cursor.execute(
                'UPDATE exercise SET id = ? WHERE id = ?',
                (new_exercise, old_exercise)
            )
        except IntegrityError:
            print(f"The '{old_exercise}' exercise is not in the database.")
        else:
            # To update each occurrence of the exercise in the week_exercise table
            cursor.execute(
                '''
                UPDATE week_exercise
                SET exercise_id = ?
                WHERE exercise_id = ?
                ''',
                (new_exercise, old_exercise)
            )
            conn.commit()
            print(f"The '{old_exercise}' exercise has been updated to '{new_exercise}'.")

    conn.close()


@click.command()
@click.option('-w', '--week', required=True, type=int, help='Week number.')
@click.option('-e', '--exercise', required=True, help='Name of the exercise.')
@click.option('-r', '--reps', required=True, type=int, help='Number of repetitions of a given exercise.')
@click.option('-n', '--new-resistance', required=True, help='Updated amount of resistance for a given exercise.')
def update_resistance(week, exercise, reps, new_resistance):
    '''
    Changes the resistance used for the specified exercise, at the given rep range, for the provided week.
    '''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    # To make sure the week, exercise, and reps are already in the database
    week_in_db = cursor.execute(
        '''
        SELECT * FROM week_exercise
        WHERE week_id = ?
        AND exercise_id = ?
        AND reps_id = ?
        ''',
        (week, exercise, reps,)
    ).fetchone()

    if not week_in_db:
        print(
            f"Week {week} with the '{exercise}' exercise and {reps} reps isn't in the database."
        )
    else:
        cursor.execute(
            '''
            UPDATE week_exercise
            SET resistance_id = ?
            WHERE week_id = ?
            AND exercise_id = ?
            AND reps_id = ?
            ''',
            (new_resistance, week, exercise, reps,)
        )
        conn.commit()
        print(
            f"The resistance for week {week}, the '{exercise}' exercise, "
            f"and {reps} reps has been successfully updated to {new_resistance}."
        )

    conn.close()


@click.command()
@click.argument('week')
def delete_week(week):
    '''Deletes the specified week from the exercise database.'''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    # To make sure the week is in the database
    week_in_db = check_db(cursor, 'week', week)

    if week_in_db:
        cursor.execute( 'DELETE FROM week WHERE id = ?', (week,) )

        # To delete every row in the week_exercise table where the week appears
        cursor.execute(
            'DELETE FROM week_exercise WHERE week_id = ?',
            (week,)
        )
        conn.commit()
        print(
            f"Week {week} has been successfully removed from the database."
        )
    else:
        print(f"Week {week} is not in the database.")

    conn.close()


@click.command()
@click.argument('equipment')
def delete_equipment(equipment):
    '''
    Deletes the specified equipment from the exercise database.
    '''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    # To make sure the equipment is in the database
    equipment_in_db = check_db(cursor, 'equipment', equipment)

    if equipment_in_db:
        cursor.execute( 'DELETE FROM equipment WHERE id = ?', (equipment,) )

        # To delete the equipment from every exercise that uses it
        cursor.execute(
            'UPDATE exercise SET equipment_id = null WHERE equipment_id = ?',
            (equipment,)
        )
        conn.commit()
        print(
            f"The '{equipment}' equipment has been successfully removed from the database."
        )
    else:
        print(f"The '{equipment}' equipment is not in the database.")

    conn.close()


@click.command()
@click.argument('exercise')
def delete_exercise(exercise):
    '''
    Deletes the specified exercise and its equipment from the exercise database.
    '''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    # To make sure the exercise is in the database
    exercise_in_db = check_db(cursor, 'exercise', exercise)

    if exercise_in_db:
        cursor.execute( 'DELETE FROM exercise WHERE id = ?', (exercise,) )

        # To delete every row in the week_exercise table where the exercise appears
        cursor.execute(
            'DELETE FROM week_exercise WHERE exercise_id = ?',
            (exercise,)
        )
        conn.commit()
        print(
            f"The '{exercise}' exercise has been successfully removed from the database."
        )
    else:
        print(f"The '{exercise}' exercise is not in the database.")

    conn.close()


@click.command()
@click.argument('reps')
def delete_reps(reps):
    '''Deletes the specified reps from the exercise database.'''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    # To make sure the reps are in the database
    reps_in_db = check_db(cursor, 'reps', reps)

    if reps_in_db:
        cursor.execute( 'DELETE FROM reps WHERE id = ?', (reps,) )

         # To delete every row in the week_exercise table where the reps appears
        cursor.execute(
            'DELETE FROM week_exercise WHERE reps_id = ?',
            (reps,)
        )
        conn.commit()
        print(f"{reps} reps has been successfully deleted from the database.")
    else:
        print(f"{reps} reps is not in the database.")

    conn.close()


@click.command()
@click.argument('resistance')
def delete_resistance(resistance):
    '''Deletes the specified resistance from the exercise database.'''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    # To make sure the resistance is in the database
    resistance_in_db = check_db(cursor, 'resistance', resistance)

    if resistance_in_db:
        cursor.execute( 'DELETE FROM resistance WHERE id = ?', (resistance,) )

        # To delete every row in the week_exercise table where the resistance appears
        cursor.execute(
            'DELETE FROM week_exercise WHERE resistance_id = ?',
            (resistance,)
        )
        conn.commit()
        print(f"'{resistance}' reps has been successfully deleted from the database.")
    else:
        print(f"'{resistance}' resistance is not in the database.")

    conn.close()
