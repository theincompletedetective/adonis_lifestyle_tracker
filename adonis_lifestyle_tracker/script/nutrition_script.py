'''
Contains the command-line scripts needed to add and update nutrition information in the database.
'''
import click
from adonis_lifestyle_tracker.common import DB_PATH
from adonis_lifestyle_tracker.nutrition import (
    add_food,
    add_totals_to_week,
    add_food_to_week,
    get_food,
    get_calories_left,
    get_protein_left
)


@click.command()
@click.argument('food')
@click.option('-k', '--calories', required=True, type=int, help='Calories in the food.')
@click.option('-p', '--protein', required=True, type=int, help='Grams of protein in the food.')
def add_food_script(food, calories, protein):
    '''
    Adds the FOOD with the specified calories and protein to the food table
    in the database.
    '''
    print( add_food(DB_PATH, food, calories, protein) )


@click.command()
@click.argument('week', type=int)
@click.option('-k', '--total-calories', required=True, type=int, help='Nmber of calories for the week.')
@click.option('-p', '--total-protein', required=True, type=int, help='Number of grams of protein for the week.')
def add_totals_to_week_script(week, total_calories, total_protein):
    '''
    Adds week number WEEK, total calories, and total protein to the week table in the database.
    '''
    print( add_totals_to_week(DB_PATH, week, total_calories, total_protein) )


@click.command()
@click.argument('week', type=int)
@click.argument('food')
def add_food_to_week_script(week, food):
    '''Adds week number WEEK and FOOD to the week_food table in the database.'''
    print( add_food_to_week(DB_PATH, week, food) )


@click.command()
@click.argument('food')
def get_food_script(food):
    '''Prints the calories and protein for FOOD in the database.'''
    print( get_food(DB_PATH, food) )


@click.command()
@click.argument('week', type=int)
def get_calories_left_script(week):
    '''
    Prints the number of calories left for week number WEEK,
    based on all the foods in the week_food table, in the database.
    '''
    print( get_calories_left(DB_PATH, week) )


@click.command()
@click.argument('week', type=int)
def get_protein_left_script(week):
    '''
    Prints the grams of protein still needed for week number WEEK,
    based on all the foods in the week_food table, in the database.
    '''
    print( get_protein_left(DB_PATH, week) )
