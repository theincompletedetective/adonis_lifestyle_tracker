'''Contains the scripts to manage the exercise information in the database.'''
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
    update_exercise,
    update_resistance,
)
from adonis_lifestyle_tracker.exercise.delete_exercise import (
    delete_equipment,
    delete_exercise,
    delete_week,
)


@click.command()
@click.argument('equipment')
def add_equipment_script(equipment):
    '''Adds EQUIPMENT to the database.'''
    print( add_equipment(DB_PATH, equipment) )


@click.command()
@click.argument('exercise')
@click.argument('equipment')
def add_exercise_script(exercise, equipment):
    '''Adds EXERCISE and EQUIPMENT to the exercise table in the database.'''
    print( add_exercise(DB_PATH, exercise, equipment) )


@click.command()
@click.argument('week', type=int)
@click.argument('exercise')
@click.argumet('reps', type=int)
@click.option('-r', '--resistance', required=True, help='Amount of resistance used for the exercise.')
def add_exercise_to_week_script(week, exercise, reps, resistance):
    '''Adds the specified exercise, reps, and resistance to the specified WEEK.'''
    print( add_exercise_to_week(DB_PATH, week, exercise, reps, resistance) )


@click.command()
@click.argument('exercise')
def get_equipment_script(exercise):
    '''Prints the equipment for EXERCISE in the database.'''
    print( get_equipment(DB_PATH, exercise) )


@click.command()
@click.argument('week', type=int)
@click.argument('exercise')
@click.argumet('reps', type=int)
def get_resistance_script(week, exercise, reps):
    '''Gets the resistance for the specified exercise and rep range for WEEK.'''
    print( get_resistance(DB_PATH, week, exercise, reps) )


@click.command()
@click.argument('exercise')
@click.argument('equipment')
def update_exercise_script(exercise, equipment):
    '''Updates the EQUIPMENT for EXERCISE.'''
    print( update_exercise(DB_PATH, exercise, equipment) )



@click.command()
@click.argument('week', type=int)
@click.argument('exercise')
@click.argumet('reps', type=int)
def update_resistance_script(week, exercise, reps):
    '''Updates the resistance of the exercise and reps for WEEK.'''
    print( update_resistance(DB_PATH, week, exercise, reps) )


@click.command()
@click.argument('exercise')
def delete_exercise_script(exercise):
    '''Deletes EXERCISE in the database.'''
    print( delete_exercise(DB_PATH, exercise) )


@click.command()
@click.argument('week', type=int)
@click.argument('exercise')
@click.argumet('reps', type=int)
@click.option('-r', '--resistance', required=True, help='Amount of resistance used for the exercise.')
def delete_week_script(week, exercise, reps, resistance):
    '''Deletes the specified exercise, reps, and resistance from the specified WEEK.'''
    print( delete_week(DB_PATH, week, exercise, reps, resistance) )


@click.command()
@click.argument('equipment')
def delete_equipment_script(equipment):
    '''Deletes EQUIPMENT from the database.'''
    print( delete_equipment(DB_PATH, equipment) )
