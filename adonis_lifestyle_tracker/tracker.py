'''Creates a GUI to manage the nutrition and exercise information.'''
import os
import PySimpleGUI as sg
from adonis_lifestyle_tracker.common.common import get_sorted_tuple, handle_get_db_path
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

db_path = None

LABEL_SIZE = (10, 1)
INPUT_SIZE = (28, 1)
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
    [sg.T('Equipment', size=LABEL_SIZE), sg.InputCombo(tuple(), key='-EQUIPMENT-', size=(INPUT_SIZE))],
    [sg.T('Exercise', size=LABEL_SIZE), sg.InputCombo(tuple(), key='-EXERCISE-', size=INPUT_SIZE)],
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

    if event == 'Load Database':

        if os.path.isfile(values['-PATH-']) and values['-PATH-'].endswith('.db'):
            db_path = values['-PATH-']

            # Nutrition info
            window['-FOOD-'].update( values=get_sorted_tuple(db_path, 'id', 'food') )
            window['-NUTRITION_WEEK-'].update( values=get_sorted_tuple(db_path, 'id', 'week') )

            # Exercise info
            window['-EQUIPMENT-'].update( values=get_sorted_tuple(db_path, 'id', 'equipment') )
            window['-EXERCISE-'].update( values=get_sorted_tuple(db_path, 'id', 'exercise') )
            window['-EXERCISE_WEEK-'].update( values=get_sorted_tuple(db_path, 'week', 'week_exercise') )
            window['-REPS-'].update( values=get_sorted_tuple(db_path, 'reps', 'week_exercise') )
            window['-RESISTANCE-'].update( values=get_sorted_tuple(db_path, 'resistance', 'week_exercise') )

            sg.popup('The database information has been successfully loaded!', title='Success')
        else:
            sg.popup_error(
                'You must enter the absolute path to the database file!',
                title='Error'
            )
            window['-PATH-'].update('')
            continue

    # Nutrition
    if event == 'Add Food':
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
        handle_change_resistance(window, values, db_path)
    else:
        continue

window.close()
