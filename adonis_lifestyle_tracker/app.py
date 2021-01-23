'''Creates a GUI to manage the nutrition and exercise information.'''
import PySimpleGUI as sg
from adonis_lifestyle_tracker.handler.common import handle_load_database, get_date
from adonis_lifestyle_tracker.handler.handle_nutrition import *
from adonis_lifestyle_tracker.handler.handle_exercise import *
from adonis_lifestyle_tracker.layout import layout


db_path = None
day = None

window = sg.Window('Adonis Lifestyle Tracker', layout)

while True:
    event, values = window.read()

    if event is None:
        break
    
    # Database
    if event == '-PATH-':
        db_path = handle_load_database(window, values)
    # Day
    elif event == 'Choose Day':
        day = get_date()

        if day:
            sg.popup(
                f'You have selected the following date: {day}.',
                title='Success'
            )
            window['Choose Day'].update('Change Day')

    elif event == 'View Day':

        if day:
            sg.popup(day, title='Info')
        else:
            sg.popup('There is no day to choose.', title='Info')

    try:

        # Nutrition
        if event == 'Add Food':
            handle_add_food(window, values, db_path)
        elif event == 'Add Weekly Totals':
            handle_add_weekly_totals(window, values, db_path)
        elif event == 'Add Weekly Food':
            handle_add_food_to_week(day, window, values, db_path)
        elif event == 'Get Food':
            handle_get_food(values, db_path)
        elif event == 'Get Calories Left':
            handle_get_calories_left(values, db_path)
        elif event == 'Get Protein Left':
            handle_get_protein_left(values, db_path)
        # Exercise
        elif event == 'Add Equipment':
            handle_add_equipment(window, values, db_path)
        elif event == 'Add Exercise':
            handle_add_exercise(window, values, db_path)
        elif event == 'Add Weekly Exercise':
            handle_add_weekly_exercise(window, values, db_path)
        elif event == 'Get Equipment':
            handle_get_equipment(values, db_path)
        elif event == 'Get Resistance':
            handle_get_resistance(values, db_path)
        elif event == 'Update Resistance':
            handle_update_resistance(window, values, db_path)
        else:
            continue

    except TypeError:
        sg.popup_error(
            'You must enter the absolute path to the database!',
            title='Error'
        )

window.close()
