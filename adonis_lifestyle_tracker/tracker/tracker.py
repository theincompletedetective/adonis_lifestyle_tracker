'''Creates a GUI to manage the nutrition and exercise information.'''
import os
import sys
import PySimpleGUI as sg
from adonis_lifestyle_tracker.handler.handle_nutrition import *
from adonis_lifestyle_tracker.handler.handle_exercise import *
from adonis_lifestyle_tracker.tracker.tracker_layout import layout


try:
    DB_PATH = os.path.join(sys._MEIPASS, 'tracker.db')
except AttributeError:
    DB_PATH = os.path.join( os.path.dirname(__file__), 'tracker.db' )

window = sg.Window('Adonis Lifestyle Tracker', layout)

while True:
    event, values = window.read()

    if event is None:
        break

    # Nutrition
    if event == 'Add Food':
        handle_add_food(window, values, DB_PATH)
    elif event == 'Add Totals to Week':
        handle_add_totals_to_week(window, values, DB_PATH)
    elif event == 'Add Food to Week':
        handle_add_food_to_week(window, values, DB_PATH)
    elif event == 'Get Food':
        handle_get_food(values, DB_PATH)
    elif event == 'Get Calories Left':
        handle_get_calories_left(values, DB_PATH)
    elif event == 'Get Protein Left':
        handle_get_protein_left(values, DB_PATH)
    elif event == 'Get Week Totals':
        handle_get_week_totals(values, DB_PATH)
    elif event == 'Update Food':
        handle_update_food(window, values, DB_PATH)
    elif event == 'Delete Food':
        handle_delete_food(window, values, DB_PATH)
    # Exercise
    elif event == 'Add Equipment':
        handle_add_equipment(window, values, DB_PATH)
    elif event == 'Add Exercise':
        handle_add_exercise(window, values, DB_PATH)
    elif event == 'Add Exercise to Week':
        handle_add_exercise_to_week(window, values, DB_PATH)
    elif event == 'Get Equipment':
        handle_get_equipment(values, DB_PATH)
    elif event == 'Get Resistance':
        handle_get_resistance(values, DB_PATH)
    elif event == 'Update Resistance':
        handle_update_resistance(window, values, DB_PATH)
    elif event == 'Update Exercise':
        handle_update_exercise(window, values, DB_PATH)
    else:
        continue

window.close()
