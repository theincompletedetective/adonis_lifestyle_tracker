'''
Adds each day's calories and protein to the database, and provides an update
for how much protein/many calories are left for the week.
'''

import PySimpleGUI as sg


TEXT_SIZE = (17, 1)
INPUT_SIZE = (10, 1)


sg.theme('Reddit')

layout = [
    [sg.Text('Number of Calories', size=TEXT_SIZE), sg.Input(key='-CALORIES-', size=INPUT_SIZE)],
    [sg.Text('Grams of Protein', size=TEXT_SIZE), sg.Input(key='-PROTEIN-', size=INPUT_SIZE)],
    [sg.Submit(button_color=('white', '#008000')), sg.Cancel( button_color=('black', '#ff0000') )]
]

window = sg.Window('Daily Nutrition Manager', layout)

while True:
    event, values = window.read()

    if event in (None, 'Cancel'):
        break
    elif event == 'Submit':
        pass
    else:
        continue

window.close()