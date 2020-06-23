''''Gets a food's name, calories and/or protein from the database.'''
import pprint
import PySimpleGUI as sg
from adonis_lifestyle_tracker.config import Config
from adonis_lifestyle_tracker.gui.confirmation_gui import get_confirmation
from adonis_lifestyle_tracker.nutrition.nutrition import get_food


sg.theme('Reddit')

layout = [
    [
        sg.Text('Food', size=Config.LABEL_SIZE ),
        sg.Input(key='-FOOD-', size=Config.FOOD_SIZE)
    ],
    [
        sg.Submit(button_color=Config.SUBMIT_BUTTON_COLOR),
        sg.Cancel(button_color=Config.CANCEL_BUTTON_COLOR)
    ]
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

        try:
            kcal, protein = get_food(food)
            sg.popup(
                f"Calories: {kcal}kcal\nProtein: {protein}g",
                title=food
            )
        except TypeError:
            sg.popup(
                'The food you selected was not in the database. '
                'Please select a different food, and try again.',
                title='Error Message'
            )
    else:
        continue

window.close()
