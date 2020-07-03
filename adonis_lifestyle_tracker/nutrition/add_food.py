''''Adds a food's name, calories and protein to the nutrition database.'''
from sqlite3 import IntegrityError
import PySimpleGUI as sg
from adonis_lifestyle_tracker.config import Config
from adonis_lifestyle_tracker.confirmation.confirmation import get_confirmation
from adonis_lifestyle_tracker.nutrition.nutrition import add_food


sg.theme('Reddit')

layout = [
    [
        sg.Text(
            Config.FOOD_LABEL,
            tooltip=Config.FOOD_TOOLTIP,
            size=Config.LABEL_SIZE
        ),
        sg.Input( key=Config.FOOD_KEY, size=Config.FOOD_SIZE)
    ],
    [
        sg.Text(Config.KCAL_LABEL, size=Config.LABEL_SIZE),
        sg.Input(key=Config.KCAL_KEY, size=Config.NUMBER_SIZE)
    ],
    [
        sg.Text(Config.PROTEIN_LABEL, size=Config.LABEL_SIZE),
        sg.Input(key=Config.PROTEIN_KEY, size=Config.NUMBER_SIZE)
    ],
    [
        sg.Button('Add Food', button_color=Config.SUBMIT_BUTTON_COLOR),
        sg.Cancel(button_color=Config.CANCEL_BUTTON_COLOR)
    ]
]

window = sg.Window('Add Food GUI', layout)

while True:
    event, values = window.read()

    if event in (None, 'Cancel'):
        break
    elif event == 'Add Food':

        if values[Config.FOOD_KEY].strip():
            food = values[Config.FOOD_KEY]
        else:
            sg.popup_error('You must select a food.', title='Error Message')
            continue

        try:
            kcal = int(values[Config.KCAL_KEY])
        except ValueError:
            sg.popup_error(
                'You must select a number for the calories.',
                title='Error Message'
            )
            continue

        try:
            protein = int(values[Config.PROTEIN_KEY])
        except ValueError:
            sg.popup_error(
                'You must select a number for the grams of protein.',
                title='Error Message'
            )
            continue

        confirmation = get_confirmation(
            f'add the food "{food}" to the nutrition database,\n'
            f'with {kcal} calories and {protein} grams of protein'
        )

        if confirmation:
            try:
                add_food(food, kcal, protein)
                sg.popup(
                    f'The food "{food}" has been successfully added\n'
                    'to the nutrition database.',
                    title='Success Message'
                )
                # To clear the values from each field, after successfully adding a food
                window[Config.FOOD_KEY].update('')
                window[Config.KCAL_KEY].update('')
                window[Config.PROTEIN_KEY].update('')
            except IntegrityError:
                sg.popup_error(
                    'You cannot add two foods with the same name '
                    'to the database!',
                    title='Error Message'
                )
    else:
        continue

window.close()
