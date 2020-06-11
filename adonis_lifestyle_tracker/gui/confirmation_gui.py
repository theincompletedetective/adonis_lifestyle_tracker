'''Contains the functions to confirm some action(s).'''

import PySimpleGUI as sg


def get_confirmation(act_to_confirm):
    sg.theme('Reddit')

    layout = [
        [sg.Text(f'Are you sure you want to {act_to_confirm}?')],
        [
            sg.Button('Yes', button_color=('white', '#008000') ),
            sg.Button('No', button_color=('black', '#ff0000') )
        ]
    ]

    window = sg.Window('Confirmation Prompt', layout)

    while True:
        event = window.read()[0]

        if event in (None, 'No'):
            break
        elif event == 'Yes':
            window.close()
            return True
        else:
            continue
    
    window.close()
    return False
