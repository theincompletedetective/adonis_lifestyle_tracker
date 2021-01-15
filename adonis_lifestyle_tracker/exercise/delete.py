'''
Contains the functions needed to delete exercise information in the database.
'''
import sqlite3
from sqlite3.dbapi2 import IntegrityError
import click
from adonis_lifestyle_tracker.config import EXERCISE_DB_PATH


@click.command()
@click.argument('week')
def delete_week(week):
    '''Deletes the specified week from its table in the exercise database.'''
    conn = sqlite3.connect(EXERCISE_DB_PATH)
    cursor = conn.cursor()

    try:
      cursor.execute( 'DELETE FROM week WHERE id = ?', (week,) )
    except IntegrityError:
        print(f"Week {week} is not in the database.")
    else:
        # To delete every row in the relation table where the week appears
        cursor.execute(
          'DELETE FROM week_exercise_reps_resistance WHERE week_id = ?',
          (week,)
        )
        conn.commit()
        print(
            f"Week {week} has been successfully removed from the database."
        )
    finally:
      conn.close()


def delete_equipment(equipment):
  '''
  Deletes the specified equipment from its table in the database.
  '''
  conn = sqlite3.connect(EXERCISE_DB_PATH)
  cursor = conn.cursor()

  try:
    cursor.execute( 'DELETE FROM equipment WHERE id = ?', (equipment,) )
  except IntegrityError:
    print(f"The '{equipment}' equipment is not in the database.")
  else:
    # To delete the equipment from every exercise that uses it
    cursor.execute(
      'UPDATE exercise SET equipment_id = null WHERE equipment_id = ?',
      (equipment,)
    )
    conn.commit()
    print(
        f"The '{equipment}' equipment has been successfully removed from the database."
    )
  finally:
    conn.close()


def delete_exercise(exercise):
  '''
  Deletes the specified exercise and its equipment from its table in the database.
  '''
  conn = sqlite3.connect(EXERCISE_DB_PATH)
  cursor = conn.cursor()

  try:
    cursor.execute( 'DELETE FROM exercise WHERE id = ?', (exercise,) )
  except IntegrityError:
    print(f"The '{exercise}' exercise is not in the database.")
  else:
    # To delete the exercise from every week that has it
    cursor.execute(
      '''
      UPDATE week_exercise_reps_resistance
      SET exercise_id = null
      WHERE exercise_id = ?
      ''',
      (exercise,)
    )
    conn.commit()
    print(
        f"The '{exercise}' exercise has been successfully removed from the database."
    )
  finally:
    conn.close()


def delete_reps(reps):
  '''
  Deletes the specified reps from its table in the database.
  '''
  conn = sqlite3.connect(EXERCISE_DB_PATH)
  cursor = conn.cursor()

  try:
    cursor.execute( 'DELETE FROM reps WHERE id = ?', (reps,) )
  except IntegrityError:
    print(f"{reps} reps is not in the database.")
  else:
    # To delete the reps from every week that has it
    cursor.execute(
      '''
      UPDATE week_exercise_reps_resistance
      SET reps_id = null
      WHERE reps_id = ?
      ''',
      (reps,)
    )
    conn.commit()
    print(f"{reps} reps has been successfully deleted from the database.")
  finally:
    conn.close()


def delete_resistance(resistance):
  '''
  Deletes the specified resistance from its table in the database.
  '''
  conn = sqlite3.connect(EXERCISE_DB_PATH)
  cursor = conn.cursor()

  try:
    cursor.execute( 'DELETE FROM resistance WHERE id = ?', (resistance,) )
  except IntegrityError:
    print(f"'{resistance}' resistance is not in the database.")
  else:
    # To delete the resistance from every week that has it
    cursor.execute(
      '''
      UPDATE week_exercise_reps_resistance
      SET resistance_id = null
      WHERE resistance_id = ?
      ''',
      (resistance,)
    )
    conn.commit()
    print(f"'{resistance}' reps has been successfully deleted from the database.")
  finally:
    conn.close()
