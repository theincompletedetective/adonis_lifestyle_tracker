''''Gets a food's name, calories and protein from the database.'''

import pprint
import PySimpleGUI as sg
from adonis_lifestyle_tracker.gui.confirmation_gui import get_confirmation
from adonis_lifestyle_tracker.nutrition.nutrition import get_food


sg.theme('Reddit')

layout = [
    [sg.Text( 'Food To Find', size=(12, 1) ), sg.Input( key='-FOOD-', size=(25, 1) )],
    [sg.Submit(button_color=('white', '#008000')), sg.Cancel( button_color=('black', '#ff0000') )]
]

window = sg.Window('View Food GUI', layout)

while True:
    event, values = window.read()

    if event in (None, 'Cancel'):
        break
    elif event == 'Submit':
        stripped_food = values['-FOOD-'].strip()

        if stripped_food:
            food = values['-FOOD-']
        else:
            sg.popup_error('You must select a food.', title='Error')
            continue

        kcal, protein = get_food(food)

        sg.popup(
            f"Calories: {kcal}kcal\nProtein: {protein}g",
            title=food
        )
    else:
        continue

window.close()
