''''Adds a food to a specific week, in the nutrition database.'''
import PySimpleGUI as sg
from adonis_lifestyle_tracker.config import Config
from adonis_lifestyle_tracker.confirmation.confirmation import get_confirmation
from adonis_lifestyle_tracker.nutrition.nutrition import add_food_to_week

sg.theme('Reddit')

layout = [
    [
        sg.Text(Config.FOOD_LABEL, size=Config.LABEL_SIZE),
        sg.Input(key=Config.FOOD_KEY, size=Config.FOOD_SIZE)
    ],
    [
        sg.Text(Config.WEEK_LABEL, size=Config.LABEL_SIZE),
        sg.Input(key=Config.WEEK_KEY, size=Config.WEEK_SIZE)
    ],
    [
        sg.Button(
            'Add Food to Week',
            button_color=Config.SUBMIT_BUTTON_COLOR
        ),
        sg.Cancel(button_color=Config.CANCEL_BUTTON_COLOR)
    ]
]

window = sg.Window('Add Food to Week GUI', layout)

while True:
    event, values = window.read()

    if event in (None, 'Cancel'):
        break
    elif event == 'Add Food to Week':
        stripped_food = values[Config.FOOD_KEY].strip()

        if stripped_food:
            food = stripped_food.title()
        else:
            sg.popup_error('You must select a food.', title='Error')
            continue

        try:
            week_num = int(values[Config.WEEK_KEY])
        except ValueError:
            sg.popup_error(
                'You must select a number for the week.',
                title='Error Message'
            )
            continue

        confirmation = get_confirmation(f'add food "{food}" to week {week_num}')

        if confirmation:
            try:
                add_food_to_week(food, week_num)
                sg.popup(
                    f'"{food}" has been successfully added to week {week_num}!',
                    title='Success Message'
                )
            except TypeError:
                sg.popup_error(
                    'You have entered a food that is not in the database.',
                    title='Error Message'
                )
    else:
        continue

window.close()
