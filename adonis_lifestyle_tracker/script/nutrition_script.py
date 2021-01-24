'''Contains the scripts to manage the nutrition information in the database.'''
import click
from adonis_lifestyle_tracker.script.common import DB_PATH
from adonis_lifestyle_tracker.nutrition.add_nutrition import *
from adonis_lifestyle_tracker.nutrition.get_nutrition import *


@click.command()
@click.argument('food')
@click.option(
    '-k', '--calories', required=True, type=int, help='Number of calories in the food.'
)
@click.option(
    '-p', '--protein', required=True, type=int, help='Grams of protein in the food.'
)
def add_food_script(food, calories, protein):
    '''Adds FOOD to the database, with its calories and grams of protein.'''
    print( add_food(DB_PATH, food, calories, protein) )


@click.command()
@click.argument('week', type=int)
@click.option(
    '-k', '--total-calories', required=True, type=int, help='Total number of calories to eat for the week.'
)
@click.option(
    '-p', '--total-protein', required=True, type=int, help='Total grams of protein to eat in the week.'
)
def add_weekly_totals_script(week, total_calories, total_protein):
    '''
    Adds the total calories and grams of protein to the specified WEEK in the database.
    '''
    print( add_weekly_totals(DB_PATH, week, total_calories, total_protein) )


@click.command()
@click.argument('week', type=int)
@click.argument('food')
def add_weekly_food_script(week, food):
    '''Adds WEEK and FOOD to the week_food relation table in the database.'''
    print( add_weekly_food(DB_PATH, week, food) )


@click.command()
@click.argument('food')
def get_food_script(food):
    '''Prints FOOD's protein and calories.'''
    print( get_food(DB_PATH, food) )


@click.command()
@click.argument('week', type=int)
def get_calories_left_script(week):
    '''Prints the calories left to consume for WEEK.'''
    print( get_calories_left(DB_PATH, week) )


@click.command()
@click.argument('week', type=int)
def get_protein_left_script(week):
    '''Prints the grams of protein left to consume for WEEK.'''
    print( get_protein_left(DB_PATH, week) )
