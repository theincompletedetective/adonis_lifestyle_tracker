'''Contains the handler functions to manage the nutrition information in the manager GUI.'''
import PySimpleGUI as sg
from adonis_lifestyle_tracker.handler.common import get_sorted_tuple
from adonis_lifestyle_tracker.nutrition.add_nutrition import (
    add_food,
    add_totals_to_week,
    add_food_to_week,
)
from adonis_lifestyle_tracker.nutrition.get_nutrition import (
    get_food,
    get_calories_left,
    get_protein_left,
)


def handle_add_food(window, values, db_path=None):
    '''Handles the event for adding a new food to the database.'''
    if db_path:
        food = values['-FOOD-'].strip()

        try:
            calories = int(values['-KCAL-'])
        except ValueError:
            sg.popup_error(
                'You must provide a number for the calories!',
                title='Error'
            )
            return

        try:
            protein = int(values['-PROTEIN-'])
        except ValueError:
            sg.popup_error(
                'You must provide a number for the grams of protein!',
                title='Error'
            )
            return

        if food and calories and protein:
            confirmation = sg.popup_yes_no(
                f"Are you sure you want to add food '{food}' with {calories} calories "
                f"and {protein} grams of protein to the database?",
                title='Confirmation'
            )

            if confirmation == 'Yes':
                sg.popup(
                    add_food(db_path, food, calories, protein), title='Message'
                )

                # To clear the food-specific fields
                window['-FOOD-'].update('')
                window['-KCAL-'].update('')
                window['-PROTEIN-'].update('')

                # To add all foods to the drop-down menu
                window['-FOOD-'].update( values=get_sorted_tuple(db_path, 'id', 'food') )
    else:
        sg.popup(
            'You must enter the absolute path to the database!',
            title='Error'
        )


def handle_add_totals_to_week(window, values, db_path=None):
    '''
    Handles the event for adding a new week with its total calories
    and protein to the database.
    '''
    if db_path:
        try:
            week = int(values['-NUTRITION_WEEK-'])
        except ValueError:
            sg.popup_error(
                'You must provide a number for the week!',
                title='Error'
            )
            return

        try:
            calories = int(values['-KCAL-'])
        except ValueError:
            sg.popup_error(
                'You must provide a number for the calories!',
                title='Error'
            )
            return

        try:
            protein = int(values['-PROTEIN-'])
        except ValueError:
            sg.popup_error(
                'You must provide a number for the grams of protein!',
                title='Error'
            )
            return

        confirmation = sg.popup_yes_no(
            f"Are you sure you want to add week {week} with {calories} total calories "
            f"and {protein} total grams of protein to the database?",
            title='Confirmation'
        )

        if confirmation == 'Yes':
            sg.popup(
                add_totals_to_week(db_path, week, calories, protein),
                title='Message'
            )

            window['-NUTRITION_WEEK-'].update('')
            window['-KCAL-'].update('')
            window['-PROTEIN-'].update('')

            window['-NUTRITION_WEEK-'].update( values=get_sorted_tuple(db_path, 'id', 'week') )
    else:
        sg.popup(
            'You must enter the absolute path to the database!',
            title='Error'
        )


def handle_add_food_to_week(window, values, db_path=None):
    '''Handles the event to add a food to a given week.'''
    if db_path:
        food = values['-FOOD-'].strip()

        try:
            week = int(values['-NUTRITION_WEEK-'])
        except ValueError:
            sg.popup_error(
                'You must provide a number for the week!',
                title='Error'
            )
            return

        if food:
            confirmation = sg.popup_yes_no(
                f"Are you sure you want to add food '{food}' to week {week}?",
                title='Confirmation'
            )

            if confirmation == 'Yes':
                sg.popup(
                    add_food_to_week(db_path, week, food),
                    title='Message'
                )

                window['-NUTRITION_WEEK-'].update('')
                window['-FOOD-'].update('')
        else:
            sg.popup_error('You must enter a food!', title='Error')

    else:
        sg.popup(
            'You must enter the absolute path to the database!',
            title='Error'
        )


def handle_get_food(values, db_path=None):
    '''Handles the event to display the calories and protein for the specified food.'''
    if db_path:
        food = values['-FOOD-'].strip()

        if food:
            sg.popup(get_food(db_path, food), title='Message')
        else:
            sg.popup_error('You must enter a food!', title='Error')

    else:
        sg.popup(
            'You must enter the absolute path to the database!',
            title='Error'
        )


def handle_get_calories_left(values, db_path=None):
    '''Handles the event to get the number of calories left to consume for a given week.'''
    if db_path:
        try:
            week = int(values['-NUTRITION_WEEK-'])
        except ValueError:
            sg.popup_error(
                'You must provide a number for the week!',
                title='Error'
            )
        else:
            sg.popup(get_calories_left(db_path, week), title='Message')

    else:
        sg.popup(
            'You must enter the absolute path to the database!',
            title='Error'
        )


def handle_get_protein_left(values, db_path=None):
    '''
    Handles the event to get the number of grams of protein left to consume
    for a given week.
    '''
    if db_path:
        try:
            week = int(values['-NUTRITION_WEEK-'])
        except ValueError:
            sg.popup_error(
                'You must provide a number for the week!',
                title='Error'
            )
        else:
            sg.popup(get_protein_left(db_path, week), title='Message')

    else:
        sg.popup(
            'You must enter the absolute path to the database!',
            title='Error'
        )
