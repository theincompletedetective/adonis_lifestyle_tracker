'''Creates a GUI to manage the Adonis Lifestyle System exercise information.'''
import PySimpleGUI as sg
from adonis_lifestyle_tracker.handler.common import handle_load_database
from adonis_lifestyle_tracker.handler.handle_exercise import *
from adonis_lifestyle_tracker.layout.exercise_layout import layout


db_path = None

window = sg.Window('Adonis Lifestyle Exercise Tracker', layout)

while True:
    event, values = window.read()

    if event is None:
        break

    # Database
    if event == '-PATH-':
        db_path = handle_load_database(window, values)

    try:

        if event == 'Add Equipment':
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
        elif event == 'Update Exercise':
            handle_update_exercise(window, values, db_path)
        elif event == 'Delete Exercise':
            handle_delete_exercise(window, values, db_path)
        elif event == 'Delete Week':
            handle_delete_week(window, values, db_path)
        else:
            continue

    except TypeError:
        sg.popup_error(
            'You must enter the absolute path to the database!',
            title='Error'
        )
        continue

window.close()
