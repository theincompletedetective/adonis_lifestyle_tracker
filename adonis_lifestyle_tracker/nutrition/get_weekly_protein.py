'''Displays the grams of protein left to consume for the specified week.'''

import PySimpleGUI as sg
from adonis_lifestyle_tracker.gui.confirmation_gui import get_confirmation
from adonis_lifestyle_tracker.nutrition.nutrition import get_protein_left_for_week


sg.theme('Reddit')

layout = [
    [sg.Text('Week Number'), sg.Input( key='-WEEK-', size=(10, 1) )],
    [
        sg.Button( 'Get Protein Left', button_color=('black', '#5d9c6d') ),
        sg.Cancel( button_color=('black', '#ff0000') )
    ]
]

window = sg.Window('Get Weekly Protein', layout)

while True:
    event, values = window.read()

    if event is None:
        break
    elif event == 'Cancel':

        if get_confirmation('close the Get Weekly Protein window'):
            break

    elif event == 'Get Protein Left':

        try:
            sg.popup(
                f"Protein Left: {get_protein_left_for_week( int(values['-WEEK-']) )}g",
                title='Info Message'
            )
        except ValueError:
            sg.popup_error('You must enter a number for the week', title='Error Message')
            continue

    else:
        continue

window.close()