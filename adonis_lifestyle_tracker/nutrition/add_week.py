''''Adds a week's total calories and protein to the nutrition database.'''

import PySimpleGUI as sg
from adonis_lifestyle_tracker.gui.confirmation_gui import get_confirmation
from adonis_lifestyle_tracker.nutrition.nutrition import add_week


TEXT_SIZE = (20, 1)
INPUT_SIZE = (10, 1)


sg.theme('Reddit')

layout = [
    [sg.Text('Week Number', size=TEXT_SIZE), sg.Input(key='-WEEK-', size=INPUT_SIZE)],
    [sg.Text('Total Calories (kcal)', size=TEXT_SIZE), sg.Input(key='-CALORIES-', size=INPUT_SIZE)],
    [sg.Text('Total Protein (g)', size=TEXT_SIZE), sg.Input(key='-PROTEIN-', size=INPUT_SIZE)],
    [sg.Submit(button_color=('white', '#008000')), sg.Cancel( button_color=('black', '#ff0000') )]
]

window = sg.Window('Add Week GUI', layout)

while True:
    event, values = window.read()

    if event in (None, 'Cancel'):
        break
    elif event == 'Submit':
        try:
            week = int(values['-WEEK-'])
        except ValueError:
            sg.popup_error(
                'You must select a number for the week.',
                title='Error'
            )
            continue
       
        try:
            total_kcal = int(values['-CALORIES-'])
        except ValueError:
            sg.popup_error(
                'You must select a number for the calories.',
                title='Error'
            )
            continue

        try:
            total_protein = int(values['-PROTEIN-'])
        except ValueError:
            sg.popup_error(
                'You must select a number for the protein.',
                title='Error'
            )
            continue
        
        confirmation = get_confirmation(
            f'Add the following total calories and total protein to week number {week}?\n'
            f'Total Calories: {total_kcal}\nTotal Protein: {total_protein}'
        )

        if confirmation:
            add_week(week, total_kcal, total_protein)
            sg.popup(
                'The total calories and protein have been added to the database!',
                title='Success Message'
            )

    else:
        continue

window.close()
