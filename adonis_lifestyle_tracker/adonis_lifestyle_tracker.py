'''Creates a GUI to manage the nutrition and exercise information.'''
import PySimpleGUI as sg
from adonis_lifestyle_tracker.common.common import DB_PATH, get_sorted_tuple
from adonis_lifestyle_tracker.nutrition.handle_nutrition import (
    handle_add_food,
    handle_add_totals_to_week,
    handle_add_food_to_week,
    handle_get_food,
    handle_get_calories_left,
    handle_get_protein_left,
    handle_delete_food,
)
from adonis_lifestyle_tracker.exercise.handle_exercise import (
    handle_add_equipment,
    handle_add_exercise,
    handle_add_exercise_to_week,
    handle_get_equipment,
    handle_get_resistance,
    handle_change_resistance,
)


sg.theme('Reddit')

LABEL_SIZE = (10, 1)
INPUT_SIZE = (28, 1)
NUM_INPUT_SIZE = (6, 1)
BUTTON_SIZE = (18, 1)

ADD_BUTTON_COLOR = ('white', '#008000')
CHANGE_BUTTON_COLOR = ('black', '#ffd700')

# Nutrition Data
NUTRITION_WEEKS = get_sorted_tuple(DB_PATH, 'id', 'week')
FOODS = get_sorted_tuple(DB_PATH, 'id', 'food')

# Exercise Data
EXERCISE_WEEKS = get_sorted_tuple(DB_PATH, 'week', 'week_exercise')
EQUIPMENT = get_sorted_tuple(DB_PATH, 'id', 'equipment')
EXERCISES = get_sorted_tuple(DB_PATH, 'id', 'exercise')
REPS = get_sorted_tuple(DB_PATH, 'reps', 'week_exercise')
RESISTANCE = get_sorted_tuple(DB_PATH, 'resistance', 'week_exercise')

nutrition_layout = [
    [sg.T('Week', size=LABEL_SIZE), sg.InputCombo( NUTRITION_WEEKS, key='-NUTRITION_WEEK-', size=(5, 1) )],
    [sg.T('Food', size=LABEL_SIZE), sg.InputCombo( FOODS, key='-FOOD-', size=(30, 1) )],
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
    [sg.T('Week', size=LABEL_SIZE), sg.InputCombo( EXERCISE_WEEKS, key='-EXERCISE_WEEK-', size=(5, 1) )],
    [sg.T('Exercise', size=LABEL_SIZE), sg.InputCombo(EXERCISES, key='-EXERCISE-', size=INPUT_SIZE)],
    [sg.T('Equipment', size=LABEL_SIZE), sg.InputCombo(EQUIPMENT, key='-EQUIPMENT-', size=(INPUT_SIZE))],
    [sg.T('Reps', size=LABEL_SIZE), sg.InputCombo( REPS, key='-REPS-', size=(6, 1) )],
    [sg.T('Resistance', size=LABEL_SIZE), sg.InputCombo( RESISTANCE, key='-RESISTANCE-', size=(6, 1) )],
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
]

window = sg.Window('Adonis Lifestyle Tracker', layout)

while True:
    event, values = window.read()

    if event is None:
        break

    # Nutrition
    if event == 'Add Food':
        handle_add_food(DB_PATH, window, values)
    elif event == 'Add Totals to Week':
        handle_add_totals_to_week(DB_PATH, window, values)
    elif event == 'Add Food to Week':
        handle_add_food_to_week(DB_PATH, window, values)
    elif event == 'Get Food':
        handle_get_food(DB_PATH, values)
    elif event == 'Get Calories Left':
        handle_get_calories_left(DB_PATH, values)
    elif event == 'Get Protein Left':
        handle_get_protein_left(DB_PATH, values)
    elif event == 'Delete Food':
        handle_delete_food(DB_PATH, window, values)

    # Exercise
    elif event == 'Add Equipment':
        handle_add_equipment(DB_PATH, window, values)
    elif event == 'Add Exercise':
        handle_add_exercise(DB_PATH, window, values)
    elif event == 'Add Exercise to Week':
        handle_add_exercise_to_week(DB_PATH, window, values)
    elif event == 'Get Equipment':
        handle_get_equipment(DB_PATH, values)
    elif event == 'Get Resistance':
        handle_get_resistance(DB_PATH, values)
    elif event == 'Change Resistance':
        handle_change_resistance(DB_PATH, window, values)
    else:
        continue

window.close()
