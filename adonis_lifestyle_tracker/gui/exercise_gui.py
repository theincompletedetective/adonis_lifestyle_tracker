'''
Contains the functions needed to add and update exercise information in the database,
using a GUI.
'''
import os
import PySimpleGUI as sg
from adonis_lifestyle_tracker.config import EQUIPMENT, EXERCISES
from adonis_lifestyle_tracker.exercise import (
    add_equipment,
    add_exercise,
    add_exercise_to_week,
    get_equipment,
    get_resistance,
    change_resistance
)


sg.theme('Reddit')

db_path = None

LABEL_SIZE = (10, 1)
INPUT_SIZE = (28, 1)
BUTTON_SIZE = (18, 1)

ADD_BUTTON_COLOR = ('white', '#008000')
CHANGE_BUTTON_COLOR = ('black', '#ffd700')

layout = [
    [sg.T('Database', size=LABEL_SIZE), sg.I(key='-PATH-'), sg.FileBrowse()],
    [sg.T('Exercise', size=LABEL_SIZE), sg.InputCombo(EXERCISES, key='-EXERCISE-')],
    [sg.T('Equipment', size=LABEL_SIZE), sg.InputCombo(EQUIPMENT, key='-EQUIPMENT-')],
    [sg.T('Resistance', size=LABEL_SIZE), sg.I( key='-RESISTANCE-', size=(10, 1) )],
    [sg.T('Week', size=LABEL_SIZE), sg.I( key='-WEEK-', size=(5, 1) )],
    [sg.T('Reps', size=LABEL_SIZE), sg.InputCombo( (3, 5, 8, 13, 21), key='-REPS-' )],
    [
        sg.B('Add Equipment', size=BUTTON_SIZE, button_color=ADD_BUTTON_COLOR),
        sg.B('Add Exercise', size=BUTTON_SIZE, button_color=ADD_BUTTON_COLOR),
        sg.B('Add Exercise to Week', size=BUTTON_SIZE, button_color=ADD_BUTTON_COLOR),
    ],
    [
        sg.B('Get Equipment', size=BUTTON_SIZE),
        sg.B('Get Resistance', size=BUTTON_SIZE),
        sg.B('Change Resistance', size=BUTTON_SIZE, button_color=CHANGE_BUTTON_COLOR)
    ],
    [
        sg.Cancel( size=BUTTON_SIZE, button_color=('black', '#ff4040') )
    ]
]

window = sg.Window('Exercise Manager', layout)

while True:
    event, values = window.read()

    if event in (None, 'Cancel'):
        break

    if event == 'Add Equipment':
        equipment = values['-EQUIPMENT-'].strip()

        if os.path.isfile( values['-PATH-'].strip() ):
            db_path = values['-PATH-'].strip()
        else:
            sg.popup_error(
                'You must provide the absolute path to the database!',
                title='Error'
            )
            continue

        if equipment:
            sg.popup(add_equipment(db_path, equipment), title='Message')
        else:
            sg.popup_error('You must provide equipment!', title='Error')

    elif event == 'Add Exercise':
        exercise = values['-EXERCISE-'].strip()
        equipment = values['-EQUIPMENT-'].strip()

        if os.path.isfile( values['-PATH-'].strip() ):
            db_path = values['-PATH-'].strip()
        else:
            sg.popup_error(
                'You must provide the absolute path to the database!',
                title='Error'
            )
            continue

        if exercise and equipment:
            sg.popup(add_exercise(db_path, exercise, equipment), title='Message')
        else:
            sg.popup_error(
                'You must provide an exercise and its equipment!',
                title='Error'
            )

    elif event == 'Add Exercise to Week':

        if os.path.isfile( values['-PATH-'].strip() ):
            db_path = values['-PATH-'].strip()
        else:
            sg.popup_error(
                'You must provide the absolute path to the database!',
                title='Error'
            )
            continue

        try:
            week = int(values['-WEEK-'])
        except ValueError:
            sg.popup_error('You must choose a number for the week!', title='Error')
            continue

        exercise = values['-EXERCISE-'].strip()

        try:
            reps = int(values['-REPS-'])
        except ValueError:
            sg.popup_error('You must choose a number for the reps!', title='Error')
            continue

        resistance = values['-RESISTANCE-'].strip()

        if exercise and resistance:
            sg.popup(
                add_exercise_to_week(db_path, week, exercise, reps, resistance),
                title='Message'
            )
        else:
            sg.popup_error(
                'You must provide an exercise and resistance!', title='Error'
            )

    elif event == 'Change Resistance':

        if os.path.isfile( values['-PATH-'].strip() ):
            db_path = values['-PATH-'].strip()
        else:
            sg.popup_error(
                'You must provide the absolute path to the database!',
                title='Error'
            )
            continue

        try:
            week = int(values['-WEEK-'])
        except ValueError:
            sg.popup_error('You must choose a number for the week!', title='Error')
            continue

        exercise = values['-EXERCISE-'].strip()

        try:
            reps = int(values['-REPS-'])
        except ValueError:
            sg.popup_error('You must choose a number for the reps!', title='Error')
            continue

        new_resistance = values['-RESISTANCE-'].strip()

        if exercise and new_resistance:
            sg.popup(
                change_resistance(db_path, week, exercise, reps, new_resistance),
                title='Message'
            )
        else:
            sg.popup_error(
                'You must provide an exercise and resistance!', title='Error'
            )

    elif event == 'Get Resistance':

        if os.path.isfile( values['-PATH-'].strip() ):
            db_path = values['-PATH-'].strip()
        else:
            sg.popup_error(
                'You must provide the absolute path to the database!',
                title='Error'
            )
            continue

        try:
            week = int(values['-WEEK-'])
        except ValueError:
            sg.popup_error('You must choose a number for the week!', title='Error')
            continue

        exercise = values['-EXERCISE-'].strip()

        try:
            reps = int(values['-REPS-'])
        except ValueError:
            sg.popup_error('You must choose a number for the reps!', title='Error')
            continue

        if exercise and reps:
            sg.popup(
                get_resistance(db_path, week, exercise, reps),
                title='Message'
            )
        else:
            sg.popup_error(
                'You must provide an exercise and number of reps!', title='Error'
            )

    elif event == 'Get Equipment':
        exercise = values['-EXERCISE-'].strip()

        if os.path.isfile( values['-PATH-'].strip() ):
            db_path = values['-PATH-'].strip()
        else:
            sg.popup_error(
                'You must provide the absolute path to the database!',
                title='Error'
            )
            continue

        if exercise:
            sg.popup( get_equipment(db_path, exercise), title='Message' )
        else:
            sg.popup_error('You must provide an exercise!', title='Error')

    else:
        continue

window.close()
