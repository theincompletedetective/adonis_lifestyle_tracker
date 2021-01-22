'''Contains the scripts to manage the nutrition information in the database.'''
import click
from adonis_lifestyle_tracker.script.common import DB_PATH
from adonis_lifestyle_tracker.nutrition.add_nutrition import (
    add_food,
)


@click.command()
@click.argument('food')
@click.option(
    '-k', '--calories', required=True, help='Number of calories in the food.'
)
@click.option(
    '-p', '--protein', required=True, help='Grams of protein in the food.'
)
def add_food_script(food, calories, protein):
    '''Adds FOOD to the database with its calories and grams of protein.'''
    print( add_food(DB_PATH, food, calories, protein) )
