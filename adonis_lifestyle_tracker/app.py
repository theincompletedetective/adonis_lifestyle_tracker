'''Creates a GUI to manage the nutrition and exercise information.'''
import os
import sys

import PySimpleGUI as sg
from adonis_lifestyle_tracker.handler.handle_nutrition import *
from adonis_lifestyle_tracker.handler.handle_exercise import *
from adonis_lifestyle_tracker.layout import layout

try:
    db_path = os.path.join(sys._MEIPASS, "app.db")
except AttributeError:
    db_path = 'app.db'

window = sg.Window('Adonis Lifestyle Tracker', layout)

while True:
    event, values = window.read()

    if event is None:
        break

    try:

        # Nutrition
        if event == 'Add Food':
            handle_add_food(window, values, db_path)
        elif event == 'Add Week':
            handle_add_weekly_totals(window, values, db_path)
        elif event == 'Add Food to Week':
            handle_add_weekly_food(window, values, db_path)
        elif event == 'Get Food':
            handle_get_food(values, db_path)
        elif event == 'Get Calories Left':
            handle_get_calories_left(values, db_path)
        elif event == 'Get Protein Left':
            handle_get_protein_left(values, db_path)
        elif event == 'Update Food':
            handle_update_food(window, values, db_path)
        elif event == 'Delete Food':
            handle_delete_food(window, values, db_path)
        elif event == 'Delete Week':
            handle_delete_week(window, values, db_path)
        # Exercise
        elif event == 'Add Equipment':
            handle_add_equipment(window, values, db_path)
        elif event == 'Add Exercise':
            handle_add_exercise(window, values, db_path)
        elif event == 'Update Equipment':
            handle_update_equipment(window, values, db_path)
        elif event == 'Get Equipment':
            handle_get_equipment(values, db_path)
        elif event == 'Get Resistance':
            handle_get_resistance(values, db_path)
        elif event == 'Update Resistance':
            handle_update_resistance(window, values, db_path)
        elif event == 'Delete Equipment':
            handle_delete_equipment(window, values, db_path)
        elif event == 'Delete Exercise':
            handle_delete_exercise(window, values, db_path)
        else:
            continue

    except TypeError:
        sg.popup_error(
            'You must enter the absolute path to the database!',
            title='Error'
        )

window.close()
