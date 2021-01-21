'''Creates a GUI to manage the nutrition and exercise information.'''
import PySimpleGUI as sg
from adonis_lifestyle_tracker.handler.common import handle_load_database
from adonis_lifestyle_tracker.handler.handle_nutrition import *
from adonis_lifestyle_tracker.handler.handle_exercise import *
from adonis_lifestyle_tracker.tracker_layout import layout


sg.theme('Reddit')

db_path = None

window = sg.Window('Adonis Lifestyle Tracker', layout)

while True:
    event, values = window.read()

    if event is None:
        break

    # Database
    if event == '-PATH-':
        db_path = handle_load_database(window, values)
    # Nutrition
    elif event == 'Add Food':
        handle_add_food(window, values, db_path)
    elif event == 'Add Totals to Week':
        handle_add_totals_to_week(window, values, db_path)
    elif event == 'Add Food to Week':
        handle_add_food_to_week(window, values, db_path)
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
    elif event == 'Add Exercise to Week':
        handle_add_exercise_to_week(window, values, db_path)
    elif event == 'Get Equipment':
        handle_get_equipment(values, db_path)
    elif event == 'Get Resistance':
        handle_get_resistance(values, db_path)
    elif event == 'Update Resistance':
        handle_update_resistance(window, values, db_path)
    else:
        continue

window.close()
