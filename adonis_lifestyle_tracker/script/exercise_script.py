'''
Contains the command-line scripts needed to add and update exercise information in the database.
'''
import click
from adonis_lifestyle_tracker.script.common import DB_PATH
from adonis_lifestyle_tracker.exercise.add_exercise import (
    add_equipment,
    add_exercise,
    add_exercise_to_week,
)
from adonis_lifestyle_tracker.exercise.get_exercise import (
    get_equipment,
    get_resistance,
)
from adonis_lifestyle_tracker.exercise.update_exercise import (
    update_resistance,
)
from adonis_lifestyle_tracker.exercise.delete_exercise import (
    delete_equipment,
    delete_exercise,
)


@click.command()
@click.argument('equipment')
def add_equipment_script(equipment):
    '''
    Adds the specified EQUIPMENT to the equipment table in the database.
    '''
    print( add_equipment(DB_PATH, equipment) )


@click.command()
@click.argument('exercise')
@click.argument('equipment')
def add_exercise_script(exercise, equipment):
    '''
    Adds the specified EXERCISE and its EQUIPMENT to the exercise table
    in the database.
    '''
    print( add_exercise(DB_PATH, exercise, equipment) )


@click.command()
@click.argument('week', type=int)
@click.argument('exercise')
@click.argument('reps', type=int)
@click.argument('resistance')
def add_exercise_to_week_script(week, exercise, reps, resistance):
    '''
    Adds the specified EXERCISE, REPS, and RESISTANCE to the provided WEEK
    in the database's week_exercise table.
    '''
    print( add_exercise_to_week(DB_PATH, week, exercise, reps, resistance) )


@click.command()
@click.argument('exercise')
def get_equipment_script(exercise):
    '''Prints the EQUIPMENT for the specified EXERCISE in the database's exercise table.'''
    print( get_equipment(DB_PATH, exercise) )


@click.command()
@click.argument('week', type=int)
@click.argument('exercise')
@click.argument('reps', type=int)
def get_resistance_script(week, exercise, reps):
    '''
    Prints the RESISTANCE for the specified WEEK, EXERCISE, and REPS
    in the database's week_exercise table.
    '''
    print( get_resistance(DB_PATH, week, exercise, reps) )


@click.command()
@click.argument('week', type=int)
@click.argument('exercise')
@click.argument('reps', type=int)
@click.argument('new_resistance')
def update_resistance_script(week, exercise, reps, new_resistance):
    '''
    Changes the RESISTANCE for the specified EXERCISE, at the given number of REPS,
    for the provided WEEK, in the database's week_exercise table.
    '''
    print( update_resistance(DB_PATH, week, exercise, reps, new_resistance) )


@click.command()
@click.argument('equipment')
def delete_equipment_script(equipment):
    '''
    Deletes EQUIPMENT from the equipment table in the database.
    '''
    print( delete_equipment(DB_PATH, equipment) )


@click.command()
@click.argument('exercise')
def delete_exercise_script(exercise):
    '''
    Deletes EXERCISE from the exercise table in the database.
    '''
    print( delete_exercise(DB_PATH, exercise) )