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
from adonis_lifestyle_tracker.nutrition.update_nutrition import (
    update_food,
    update_week_totals,
)
from adonis_lifestyle_tracker.nutrition.delete_nutrition import (
    delete_food,
    delete_nutrition_week
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


def handle_update_food(values, db_path=None):
    '''Handles the event to update the name, calories, or protein for a food.'''
    if db_path:
        food = values['-FOOD-'].strip()

        # You can enter either one, or both
        calories = None
        protein = None

        if values['-KCAL-'].strip():
            try:
                calories = int(values['-KCAL-'])
            except ValueError:
                sg.popup_error(
                    'You must provide a number for the calories!',
                    title='Error'
                )
                return

        if values['-PROTEIN-'].strip():
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
                f"Are you sure you want to update the calories for food '{food}' to {calories}, "
                f"and its protein to {protein} grams?",
                title='Confirmation'
            )

            if confirmation == 'Yes':
                sg.popup(
                    update_food(db_path, food, calories=calories, protein=protein),
                    title='Message'
                )

        elif food and calories and not protein:
            confirmation = sg.popup_yes_no(
                f"Are you sure you want to update the calories for food '{food}' to {calories}?",
                title='Confirmation'
            )

            if confirmation == 'Yes':
                sg.popup(
                    update_food(db_path, food, calories=calories),
                    title='Message'
                )

        elif food and not calories and protein:

            confirmation = sg.popup_yes_no(
                f"Are you sure you want to update the protein for food '{food}' to {protein} grams?",
                title='Confirmation'
            )

            if confirmation == 'Yes':
                sg.popup(
                    update_food(db_path, food, protein=protein),
                    title='Message'
                )

        elif food and not calories and not protein:
            sg.popup_error(
                'You must enter protein, calories, or both, if you enter a food!',
                title='Error'
            )
        else:
            sg.popup_error('You must enter a food!', title='Error')

    else:
        sg.popup(
            'You must enter the absolute path to the database!',
            title='Error'
        )


def handle_update_week_totals(window, values, db_path=None):
    '''Handles the event to update the total calories and protein for the specified week.'''
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
            f"Are you sure you want to update week {week} with {calories} total calories "
            f"and {protein} total grams of protein?",
            title='Confirmation'
        )

        if confirmation == 'Yes':
            sg.popup(
                update_week_totals(db_path, week, calories, protein),
                title='Message'
            )

            window['-NUTRITION_WEEK-'].update('')
            window['-KCAL-'].update('')
            window['-PROTEIN-'].update('')
    else:
        sg.popup(
            'You must enter the absolute path to the database!',
            title='Error'
        )


def handle_delete_food(window, values, db_path=None):
    '''Handles the event to delete the specified food from the database.'''
    if db_path:
        food = values['-FOOD-'].strip()

        if food:
            confirmation = sg.popup_yes_no(
                f"Are you sure you want to delete food '{food}' from the database?",
                title='Confirmation'
            )

            if confirmation == 'Yes':
                sg.popup(delete_food(db_path, food), title='Message')

                window['-FOOD-'].update('')

                window['-FOOD-'].update( values=get_sorted_tuple(db_path, 'id', 'food') )
        else:
            sg.popup_error('You must enter a food!', title='Error')

    else:
        sg.popup(
            'You must enter the absolute path to the database!',
            title='Error'
        )


def handle_delete_week(window, values, db_path=None):
    '''Handles the event to delete the specified week from the week table in the database.'''
    if db_path:
        try:
            week = int(values['-NUTRITION_WEEK-'])
        except ValueError:
            sg.popup_error(
                'You must provide a number for the week!',
                title='Error'
            )
            return

        confirmation = sg.popup_yes_no(
            f"Are you sure you want to delete week {week} from the database?",
            title='Confirmation'
        )

        if confirmation == 'Yes':
            sg.popup(delete_nutrition_week(db_path, week), title='Message')

            window['-NUTRITION_WEEK-'].update('')

            window['-NUTRITION_WEEK-'].update( values=get_sorted_tuple(db_path, 'id', 'week') )

    else:
        sg.popup(
            'You must enter the absolute path to the database!',
            title='Error'
        )
