'''
Adds a new week of exercises to the database exercises, along with each rep range.
'''

import PySimpleGUI as sg
from adonis_lifestyle_tracker.gui.confirmation_gui import get_confirmation
from adonis_lifestyle_tracker.exercise.exercise import add_week


TEXT_SIZE = (20, 1)
INPUT_SIZE = (15, 1)

sg.theme('Reddit')

layout = [
    [sg.Text('Week Number', size=TEXT_SIZE), sg.Input(key='-WEEK_NUM-', size=INPUT_SIZE)],
    [sg.Text('Exercise', size=TEXT_SIZE), sg.Input( key='-EXERCISE-', size=(30, 1) )],
    [sg.Text('5 Reps Resistance', size=TEXT_SIZE), sg.Input(key='-5_REPS-', size=INPUT_SIZE)],
    [sg.Text('8 Reps Resistance', size=TEXT_SIZE), sg.Input(key='-8_REPS-', size=INPUT_SIZE)],
    [sg.Text('13 Reps Resistance', size=TEXT_SIZE), sg.Input(key='-13_REPS-', size=INPUT_SIZE)],
    [sg.Text('21 Reps Resistance', size=TEXT_SIZE), sg.Input(key='-21_REPS-', size=INPUT_SIZE)],
    [
        sg.Button('Add Week', button_color=('white', '#008000')),
        sg.Cancel( button_color=('black', '#ff0000') )
    ]
]

window = sg.Window('Add Week GUI', layout)

while True:
    event, values = window.read()

    if event in (None, 'Cancel'):
        break
    elif event == 'Add Week':
        exercise_id = get_exercise_id(values['-EXERCISE-'])
        add_exercise_to_week(exercise_id, week_id)
    else:
        continue

window.close()