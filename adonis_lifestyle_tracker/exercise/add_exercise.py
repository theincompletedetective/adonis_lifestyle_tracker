'''
Adds each exercises, the number of reps, and the resistance per rep to the database.
'''

import PySimpleGUI as sg
from adonis_lifestyle_tracker.gui.confirmation_gui import get_confirmation
from adonis_lifestyle_tracker.exercise.exercise import add_exercise


TEXT_SIZE = (15, 1)
INPUT_SIZE = (20, 1)


sg.theme('Reddit')

layout = [
    [sg.Text('Exercise Name', size=TEXT_SIZE), sg.Input( key='-EXERCISE-', size=(25, 1) )],
    [sg.Text('Equipment Used', size=TEXT_SIZE), sg.Input( key='-EQUIPMENT-', size=(25, 1) )],
    [
        sg.Button('Add Exercise', button_color=('white', '#008000')),
        sg.Cancel( button_color=('black', '#ff0000') )
    ]
]

window = sg.Window('Add Exercise GUI', layout)

while True:
    event, values = window.read()

    if event in (None, 'Cancel'):
        break
    elif event == 'Add Exercise':

        if values['-EXERCISE-'].strip():
            exercise = values['-EXERCISE-']
        else:
            sg.popup_error('You must enter an exercise.', title='Error')
            continue

        if values['-EQUIPMENT-'].strip():
            equipment = values['-EQUIPMENT-']
        else:
            sg.popup_error(
                'You must enter exercise equipment.',
                title='Error'
            )
            continue

        confirmation = get_confirmation(
            f'add the exercise "{exercise}" to the database,\nwith the "{equipment}" equipment'
        )

        if confirmation:
            add_exercise(exercise, equipment)
            sg.popup(
                f'The exercise and equipment have been successfully added to the database!',
                title='Success Message'
            )

    else:
        continue

window.close()