'''
Adds each exercises, the number of reps, and the resistance per rep to the database.
'''

import PySimpleGUI as sg


TEXT_SIZE = (17, 1)
INPUT_SIZE = (20, 1)


sg.theme('Reddit')

layout = [
    [sg.Text('Exercise Name', size=TEXT_SIZE), sg.Input( key='-EXERCISE-', size=(25, 1) )],
    [sg.Text('Equipment', size=TEXT_SIZE), sg.Input( key='-EQUIPMENT-', size=(25, 1) )],
    [sg.Text('5 Reps Resistance', size=TEXT_SIZE), sg.Input(key='-5_REPS-', size=INPUT_SIZE)],
    [sg.Text('8 Reps Resistance', size=TEXT_SIZE), sg.Input(key='-8_REPS-', size=INPUT_SIZE)],
    [sg.Text('13 Reps Resistance', size=TEXT_SIZE), sg.Input(key='-13_REPS-', size=INPUT_SIZE)],
    [sg.Text('21 Reps Resistance', size=TEXT_SIZE), sg.Input(key='-12_REPS-', size=INPUT_SIZE)],
    [sg.Submit(button_color=('white', '#008000')), sg.Cancel( button_color=('black', '#ff0000') )]
]

window = sg.Window('Workout Exercise Manager', layout)

while True:
    event, values = window.read()

    if event in (None, 'Cancel'):
        break
    elif event == 'Submit':
        pass
    else:
        continue

window.close()