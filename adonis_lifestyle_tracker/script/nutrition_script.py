'''
Contains the command-line scripts needed to add and update nutrition information in the database.
'''
import click
from adonis_lifestyle_tracker.config import NUTRITION_DB_PATH
from adonis_lifestyle_tracker.nutrition.nutrition import (
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
    in the nutrition database.
    '''
    print( add_food(NUTRITION_DB_PATH, food, calories, protein) )


@click.command()
@click.option('-w', '--week', required=True, type=int, help='Week number.')
@click.option('-k', '--total-calories', required=True, type=int, help='Nmber of calories for the week.')
@click.option('-p', '--total-protein', required=True, type=int, help='Number of grams of protein for the week.')
def add_totals_to_week_script(week, total_calories, total_protein):
    '''
    Adds a week, total calories, and total protein to the week table in the nutrition database.
    '''
    print( add_totals_to_week(NUTRITION_DB_PATH, week, total_calories, total_protein) )


@click.command()
@click.option('-f', '--food', required=True, help='Name of the food.')
@click.option('-w', '--week', required=True, type=int, help='Week number.')
def add_food_to_week_script(food, week):
    '''Adds a week and food to the week_food table in the nutrition database.'''
    print( add_food_to_week(NUTRITION_DB_PATH, food, week) )


@click.command()
@click.argument('food')
def get_food_script(food):
    '''Prints the calories and protein for FOOD in the nutrition database.'''
    print( get_food(NUTRITION_DB_PATH, food) )


@click.command()
@click.argument('week', type=int)
def get_calories_left_script(week):
    '''
    Prints the number of calories left for week number WEEK,
    based on all the foods in the week_food table, in the nutrition database.
    '''
    print( get_calories_left(NUTRITION_DB_PATH, week) )


@click.command()
@click.argument('week', type=int)
def get_protein_left(week):
    '''
    Prints the grams of protein still needed for week number WEEK,
    based on all the foods in the week_food table, in the nutrition database.
    '''
    print( get_protein_left(NUTRITION_DB_PATH, week) )
