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
        elif event == 'Add Food to Day':
            handle_add_food_to_day_of_week(window, values, db_path)
        elif event == "Get Food's Calories and Protein":
            handle_get_calories_and_protein_for_food(values, db_path)
        elif event == 'Get Calories Eaten for Day':
            handle_get_calories_eaten_for_weekday(window, values, db_path)
        elif event == 'Get Total Calories for Week':
            handle_get_total_calories(values, db_path)
        elif event == 'Get Total Protein for Week':
            handle_get_total_protein(values, db_path)
        elif event == 'Get Calories Left for Week':
            handle_get_calories_left_for_week(values, db_path)
        elif event == 'Get Protein Left for Week':
            handle_get_protein_left_for_week(values, db_path)
        elif event == 'Update Calories':
            handle_update_calories_for_food(window, values, db_path)
        elif event == 'Update Protein':
            handle_update_protein_for_food(window, values, db_path)
        elif event == 'Delete Food':
            handle_delete_food(window, values, db_path)
        elif event == 'Delete Week':
            handle_delete_week(window, values, db_path)
        else:
            continue

    except TypeError:
        sg.popup_error('You must enter the absolute path to the database!', title='Error')

window.close()
