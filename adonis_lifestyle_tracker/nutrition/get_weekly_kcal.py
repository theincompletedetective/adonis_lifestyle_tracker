'''Manages the nutrition database, using a GUI.'''

import PySimpleGUI as sg
from adonis_lifestyle_tracker.gui.confirmation_gui import get_confirmation


sg.theme('Reddit')

layout = [
    [sg.Text('Choose whether to get the number of calories or amount of protein left:')],
    [
        sg.Button( 'Get Calories Left', button_color=('', '') ),
        sg.Button( 'Get Protein Left', button_color=('', '') ),
        sg.Cancel( button_color=('black', '#ff0000') )
    ]
]

window = sg.Window('Nutrition Manager', layout)

while True:
    event, values = window.read()

    if event is None:
        break
    elif event == 'Cancel':
        if get_confirmation('close the Nutrition Manager window'):
            break
    elif event == 'Get Calories Left':
        pass
    elif event == 'Get Protein Left':
        pass
    else:
        continue

window.close()