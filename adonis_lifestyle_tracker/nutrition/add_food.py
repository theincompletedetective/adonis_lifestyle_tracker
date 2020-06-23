''''Adds a food's name, as well as its calories and protein to the database.'''
from sqlite3 import IntegrityError
import PySimpleGUI as sg
from adonis_lifestyle_tracker.config import Config
from adonis_lifestyle_tracker.gui.confirmation_gui import get_confirmation
from adonis_lifestyle_tracker.nutrition.nutrition import add_food


sg.theme('Reddit')

layout = [
    [
        sg.Text(
            'Food',
            tooltip='The name of the food to add to the database',
            size=Config.LABEL_SIZE
        ),
        sg.Input( key='-FOOD-', size=Config.FOOD_SIZE)
    ],
    [
        sg.Text('Calories (kcal)', size=Config.LABEL_SIZE),
        sg.Input(key='-CALORIES-', size=Config.NUMBER_SIZE)
    ],
    [
        sg.Text('Protein (g)', size=Config.LABEL_SIZE),
        sg.Input(key='-PROTEIN-', size=Config.NUMBER_SIZE)
    ],
    [
        sg.Submit(button_color=Config.SUBMIT_BUTTON_COLOR),
        sg.Cancel(button_color=Config.CANCEL_BUTTON_COLOR)
    ]
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
            f'add the food "{food}" to the nutrition database,\n'
            f'with {kcal} calories and {protein} grams of protein'
        )

        if confirmation:
            try:
                add_food(food, kcal, protein)
                sg.popup(
                    f'The food "{food}" has been successfully added\nto the nutrition database.',
                    title='Success Message'
                )
                # To clear the values from each field, after successfully adding a food
                window['-FOOD-'].update('')
                window['-CALORIES-'].update('')
                window['-PROTEIN-'].update('')
            except IntegrityError:
                sg.popup_error(
                    'You cannot add two foods with the same name to the database!',
                    title='Error Message'
                )
    else:
        continue

window.close()
