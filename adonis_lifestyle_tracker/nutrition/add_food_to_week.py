''''Adds a food to a specific week, in the nutrition database.'''
import PySimpleGUI as sg
from adonis_lifestyle_tracker.config import Config
from adonis_lifestyle_tracker.gui.confirmation_gui import get_confirmation
from adonis_lifestyle_tracker.nutrition.nutrition import add_food_to_week

sg.theme('Reddit')

layout = [
    [
        sg.Text(Config.FOOD_LABEL, size=Config.LABEL_SIZE),
        sg.Input(key='-FOOD-', size=Config.FOOD_SIZE)
    ],
    [
        sg.Text(Config.WEEK_LABEL, size=Config.LABEL_SIZE),
        sg.Input(key='-WEEK-', size=Config.WEEK_SIZE)
    ],
    [
        sg.Button(
            Config.SUBMIT_BUTTON_TEXT,
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
    elif event == 'Add Food':
        stripped_food = values['-FOOD-'].strip()

        if stripped_food:
            food = stripped_food.title()
        else:
            sg.popup_error('You must select a food.', title='Error')
            continue

        try:
            week_num = int(values['-WEEK-'])
        except ValueError:
            sg.popup_error('You must select a week number.', title='Error')
            continue

        confirmation = get_confirmation(f'add food "{food}" to week {week_num}')

        if confirmation:
            try:
                add_food_to_week(food, week_num)
                sg.popup(
                    'The food has been successfully added to the week!',
                    title='Success Message'
                )
            except TypeError:
                sg.popup_error(
                    'You have selected a food that is not in the database.',
                    title='Error Message'
                )
    else:
        continue

window.close()
