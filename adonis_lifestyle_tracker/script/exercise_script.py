'''Contains the scripts to manage the exercise information in the database.'''
import click
from adonis_lifestyle_tracker.script.common import DB_PATH
from adonis_lifestyle_tracker.exercise.add_exercise import *
from adonis_lifestyle_tracker.exercise.get_exercise import *
from adonis_lifestyle_tracker.exercise.update_exercise import *


@click.command()
@click.argument('equipment')
def add_equipment_script(equipment):
    '''Adds EQUIPMENT to the database.'''
    print( add_equipment(DB_PATH, equipment) )


@click.command()
@click.argument('exercise')
@click.argument('equipment')
def add_exercise_script(exercise, equipment):
    '''Adds EXERCISE and its EQUIPMENT to the database.'''
    print( add_exercise(DB_PATH, exercise, equipment) )


@click.command()
@click.argument('exercise')
def get_equipment_script(exercise):
    '''Prints the equipment for EXERCISE in the database.'''
    print( get_equipment(DB_PATH, exercise) )


@click.command()
@click.argument('week', type=int)
@click.argument('exercise')
@click.argument('reps', type=int)
def get_resistance_script(week, exercise, reps):
    '''
    Prints WEEK's resistance for the specified EXERCISE and REPS.
    '''
    print( get_resistance(DB_PATH, week, exercise, reps) )


@click.command()
@click.argument('exercise')
@click.argument('reps', type=int)
@click.argument('resistance')
def update_resistance_script(exercise, reps, resistance):
    '''Updates EXERCISE's RESISTANCE for the number of REPS in the database.'''
    print( update_resistance(DB_PATH, exercise, reps, resistance) )


@click.command()
@click.argument('exercise')
@click.argument('equipment')
def update_equipment_script(exercise, equipment):
    '''Updates the EQUIPMENT for EXERCISE in the database.'''
    print( update_equipment(DB_PATH, exercise, equipment) )
