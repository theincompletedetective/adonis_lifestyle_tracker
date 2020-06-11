''''Adds a food to a specific week, in the nutrition database.'''

import PySimpleGUI as sg
from adonis_lifestyle_tracker.gui.confirmation_gui import get_confirmation
from adonis_lifestyle_tracker.nutrition.nutrition import add_food_to_week


TEXT_SIZE = (13, 1)
INPUT_SIZE = (10, 1)


sg.theme('Reddit')

layout = [
    [sg.Text('Food Name', size=TEXT_SIZE), sg.Input( key='-FOOD-', size=(25, 1) )],
    [sg.Text('Week Number', size=TEXT_SIZE), sg.Input(key='-WEEK-', size=INPUT_SIZE)],
    [sg.Submit(button_color=('white', '#008000')), sg.Cancel( button_color=('black', '#ff0000') )]
]

window = sg.Window('Add Food to Week GUI', layout)

while True:
    event, values = window.read()

    if event in (None, 'Cancel'):
        break
    elif event == 'Submit': 

        if values['-FOOD-'].strip():
            food = values['-FOOD-'].strip()
        else:
            sg.popup_error(
                'You must select a food.', title='Error'
            )
            continue

        try:
            week_num = int(values['-WEEK-'])
        except ValueError:
            sg.popup_error(
                'You must select a number for the week.',
                title='Error'
            )
            continue
        
        confirmation = get_confirmation(
            f"Add the following food to week {week_num}? '{food}'"
        )

        if confirmation:
            add_food_to_week(food, week_num)
            sg.popup(
                'The food has been added to the week number, in the database!',
                title='Success Message'
            )

    else:
        continue

window.close()
