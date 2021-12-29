from adonis_lifestyle_tracker.handler.common import handle_load_database
from adonis_lifestyle_tracker.handler.handle_nutrition import *
from adonis_lifestyle_tracker.nutrition.nutrition_layout import layout


db_path = None

window = sg.Window('Adonis Lifestyle Nutrition Tracker', layout)

while True:
    event, values = window.read()

    if event is None:
        break

    if event == 'Load Database':
        db_path = handle_load_database(window, values)

    try:

        if event == 'Add Food':
            handle_add_food(window, values, db_path)
        elif event == 'Add Week':
            handle_add_total_calories_and_protein_for_week(window, values, db_path)
        elif event == 'Add Food to Week':
            handle_add_food_to_week(window, values, db_path)
        elif event == 'Get Food':
            handle_get_calories_and_protein_for_food(values, db_path)
        elif event == 'Get Calories Left':
            handle_get_calories_left_for_week(values, db_path)
        elif event == 'Get Protein Left':
            handle_get_protein_left_for_week(values, db_path)
        elif event == 'Update Food':
            handle_update_calories_and_protein_for_food(window, values, db_path)
        elif event == 'Delete Food':
            handle_delete_food(window, values, db_path)
        elif event == 'Delete Week':
            handle_delete_week(window, values, db_path)
        else:
            continue

    except TypeError:
        sg.popup_error('You must enter the absolute path to the database!', title='Error')

window.close()
