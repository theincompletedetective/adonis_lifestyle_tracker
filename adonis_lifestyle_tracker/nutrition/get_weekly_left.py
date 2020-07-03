'''Displays the number of calories left to consume for the specified week.'''
import PySimpleGUI as sg
from adonis_lifestyle_tracker.config import Config
from adonis_lifestyle_tracker.confirmation.confirmation import get_confirmation
from adonis_lifestyle_tracker.nutrition.nutrition import (
    get_kcal_left_for_week, get_protein_left_for_week
)


sg.theme('Reddit')

layout = [
    [sg.Text('Which nutrient did you want to check?')],
    [sg.Listbox( ('Calories', 'Protein'), size=(15, 2), key='-CHOICE-' )],
    [
        sg.Text(Config.WEEK_LABEL),
        sg.Input( key=Config.WEEK_KEY, size=Config.WEEK_SIZE)
    ],
    [
        sg.Button('Get Weekly Left', button_color=Config.SUBMIT_BUTTON_COLOR),
        sg.Cancel(button_color=Config.CANCEL_BUTTON_COLOR)
    ]
]

window = sg.Window('Get Weekly Calories', layout)

while True:
    event, values = window.read()

    if event is None:
        break
    elif event == 'Cancel':

        if get_confirmation('close the Get Weekly Calories window'):
            break

    elif event == 'Get Weekly Left':
        choice = values['-CHOICE-'][0]

        if choice:
            try:
                week = int(values[Config.WEEK_KEY])
            except ValueError:
                sg.popup_error(
                    'You must enter a number for the week',
                    title='Error Message'
                )
                continue

            if choice == 'Calories':
                sg.popup(
                    f'You have {get_kcal_left_for_week(week)}kcal left for '
                    f'week {week}.',
                    title='Info Message'
                )
            elif choice == 'Protein':
                sg.popup(
                    f'You have {get_protein_left_for_week(week)} grams '
                    f'of protein left for week {week}.',
                    title='Info Message'
                )
            else:
                sg.popup(
                    'You must choose either calories or protein.',
                    title='Error Message'
                )

    else:
        continue

window.close()
