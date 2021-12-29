from adonis_lifestyle_tracker.handler.common import handle_load_database
from adonis_lifestyle_tracker.handler.handle_exercise import *
from adonis_lifestyle_tracker.exercise.exercise_layout import layout


db_path = None

window = sg.Window('Adonis Lifestyle Exercise Tracker', layout)

while True:
    event, values = window.read()

    if event is None:
        break

    if event == 'Load Database':
        db_path = handle_load_database(window, values)

    try:
        if event == 'Add Equipment':
            handle_add_equipment(window, values, db_path)
        elif event == 'Add Exercise':
            handle_add_exercise(window, values, db_path)
        elif event == 'Update Equipment':
            handle_update_equipment_for_exercise(window, values, db_path)
        elif event == 'Get Equipment':
            handle_get_equipment_for_exercise(values, db_path)
        elif event == 'Get Resistance':
            handle_get_resistance_for_exercise_and_reps(values, db_path)
        elif event == 'Update Resistance':
            handle_update_resistance_for_exercise(window, values, db_path)
        elif event == 'Delete Equipment':
            handle_delete_equipment(window, values, db_path)
        elif event == 'Delete Exercise':
            handle_delete_exercise(window, values, db_path)
        else:
            continue

    except TypeError:
        sg.popup_error('You must enter the absolute path to the database!', title='Error')

window.close()
