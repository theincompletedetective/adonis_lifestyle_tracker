'''Contains the scripts to manage the exercise information in the database.'''
import click
from adonis_lifestyle_tracker.script.common import DB_PATH
from adonis_lifestyle_tracker.exercise.add_exercise import (
    add_equipment,
)


@click.command()
@click.argument('equipment')
def add_equipment_script(equipment):
    '''Adds EQUIPMENT to the database.'''
    print( add_equipment(DB_PATH, equipment) )
