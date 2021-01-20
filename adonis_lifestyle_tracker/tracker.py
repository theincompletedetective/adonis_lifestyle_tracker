'''Creates a GUI to manage the nutrition and exercise information.'''
import PySimpleGUI as sg
from adonis_lifestyle_tracker.handler.common import handle_load_database
from adonis_lifestyle_tracker.handler.handle_nutrition import *
from adonis_lifestyle_tracker.handler.handle_exercise import *


sg.theme('Reddit')

db_path = None

LABEL_SIZE = (10, 1)
TEXT_INPUT_SIZE = (28, 1)
NUM_INPUT_SIZE = (6, 1)
BUTTON_SIZE = (18, 1)
ADD_BUTTON_COLOR = ('white', '#008000')
CHANGE_BUTTON_COLOR = ('black', '#ffd700')

nutrition_layout = [
    [sg.T('Week', size=LABEL_SIZE), sg.InputCombo( tuple(), key='-NUTRITION_WEEK-', size=(5, 1) )],
    [sg.T('Food', size=LABEL_SIZE), sg.InputCombo( tuple(), key='-FOOD-', size=(30, 1) )],
    [sg.T('Calories', size=LABEL_SIZE), sg.I(key='-KCAL-', size=NUM_INPUT_SIZE)],
    [sg.T('Protein', size=LABEL_SIZE), sg.I(key='-PROTEIN-', size=NUM_INPUT_SIZE)],
    [
        sg.B('Add Food', size=BUTTON_SIZE, button_color=ADD_BUTTON_COLOR),
        sg.B('Add Totals to Week', size=BUTTON_SIZE, button_color=ADD_BUTTON_COLOR),
        sg.B('Add Food to Week', size=BUTTON_SIZE, button_color=ADD_BUTTON_COLOR),
    ],
    [
        sg.B( 'Get Food', size=BUTTON_SIZE),
        sg.B( 'Get Calories Left', size=BUTTON_SIZE),
        sg.B( 'Get Protein Left', size=BUTTON_SIZE)
    ],
    [
        sg.B( 'Delete Food', size=BUTTON_SIZE, button_color=('black', '#ff4040') )
    ]
]

exercise_layout = [
    [sg.T('Equipment', size=LABEL_SIZE), sg.InputCombo(tuple(), key='-EQUIPMENT-', size=(TEXT_INPUT_SIZE))],
    [sg.T('Exercise', size=LABEL_SIZE), sg.InputCombo(tuple(), key='-EXERCISE-', size=TEXT_INPUT_SIZE)],
    [sg.T('Week', size=LABEL_SIZE), sg.InputCombo( tuple(), key='-EXERCISE_WEEK-', size=(5, 1) )],
    [sg.T('Reps', size=LABEL_SIZE), sg.InputCombo( tuple(), key='-REPS-', size=(6, 1) )],
    [sg.T('Resistance', size=LABEL_SIZE), sg.InputCombo( tuple(), key='-RESISTANCE-', size=(6, 1) )],
    [
        sg.B('Add Equipment', size=BUTTON_SIZE, button_color=ADD_BUTTON_COLOR),
        sg.B('Add Exercise', size=BUTTON_SIZE, button_color=ADD_BUTTON_COLOR),
        sg.B('Add Exercise to Week', size=BUTTON_SIZE, button_color=ADD_BUTTON_COLOR),
    ],
    [
        sg.B('Get Equipment', size=BUTTON_SIZE),
        sg.B('Get Resistance', size=BUTTON_SIZE),
        sg.B('Change Resistance', size=BUTTON_SIZE, button_color=CHANGE_BUTTON_COLOR)
    ]
]

layout = [
    [
        sg.TabGroup([[
            sg.Tab('Nutrition', nutrition_layout),
            sg.Tab('Exercise', exercise_layout)
        ]])
    ],
    [sg.Frame('Database', layout=[
        [
            sg.I(key='-PATH-', size=(38, 1), enable_events=True), sg.FileBrowse(),
            sg.B('Load Database', button_color=('white', '#8a2be2'))
        ]
    ])]
]

window = sg.Window('Adonis Lifestyle Tracker', layout)

while True:
    event, values = window.read()

    if event is None:
        break

    # Database
    if event == 'Load Database':
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
    elif event == 'Delete Food':
        handle_delete_food(window, values, db_path)
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
    elif event == 'Change Resistance':
        handle_update_resistance(window, values, db_path)
    else:
        continue

window.close()
