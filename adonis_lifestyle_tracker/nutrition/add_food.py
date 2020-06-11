''''Adds a food, as well as its calories and protein to the database.'''

import PySimpleGUI as sg
from adonis_lifestyle_tracker.gui.confirmation_gui import get_confirmation
from adonis_lifestyle_tracker.nutrition.nutrition import add_food


TEXT_SIZE = (12, 1)
INPUT_SIZE = (10, 1)


sg.theme('Reddit')

layout = [
    [sg.Text('Food', size=TEXT_SIZE), sg.Input( key='-FOOD-', size=(25, 1) )],
    [sg.Text('Calories (kcal)', size=TEXT_SIZE), sg.Input(key='-CALORIES-', size=INPUT_SIZE)],
    [sg.Text('Protein (g)', size=TEXT_SIZE), sg.Input(key='-PROTEIN-', size=INPUT_SIZE)],
    [sg.Submit(button_color=('white', '#008000')), sg.Cancel( button_color=('black', '#ff0000') )]
]

window = sg.Window('Add Food GUI', layout)

while True:
    event, values = window.read()

    if event in (None, 'Cancel'):
        break
    elif event == 'Submit':

        if values['-FOOD-'].strip():
            food = values['-FOOD-']
        else:
            sg.popup_error('You must select a food.', title='Error')
            continue
        
        try:
            kcal = int(values['-CALORIES-'])
        except ValueError:
            sg.popup_error(
                'You must select a number for the calories.',
                title='Error'
            )
            continue

        try:
            protein = int(values['-PROTEIN-'])
        except ValueError:
            sg.popup_error(
                'You must select a number for the grams of protein.',
                title='Error'
            )
            continue
        
        confirmation = get_confirmation(
            f'add the food "{food}" to the nutrition database'
        )

        if confirmation:
            add_food(food, kcal, protein)
            sg.popup(
                f'The following food has been successfully added to the database: "{food}".',
                title='Success Message'
            )

    else:
        continue

window.close()