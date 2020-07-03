''''Adds a week's total calories and protein to the nutrition database.'''
import PySimpleGUI as sg
from adonis_lifestyle_tracker.config import Config
from adonis_lifestyle_tracker.confirmation.confirmation import get_confirmation
from adonis_lifestyle_tracker.nutrition.nutrition import add_week


sg.theme('Reddit')

layout = [
    [
        sg.Text(Config.WEEK_LABEL, size=Config.LABEL_SIZE),
        sg.Input(key=Config.WEEK_KEY, size=Config.NUMBER_SIZE)
    ],
    [
        sg.Text(f'Total {Config.KCAL_LABEL}', size=Config.LABEL_SIZE),
        sg.Input(key=Config.KCAL_KEY, size=Config.NUMBER_SIZE)
    ],
    [
        sg.Text(f'Total {Config.PROTEIN_LABEL}', size=Config.LABEL_SIZE),
        sg.Input(key=Config.PROTEIN_KEY, size=Config.NUMBER_SIZE)
    ],
    [
        sg.Button('Add Week', button_color=Config.SUBMIT_BUTTON_COLOR),
        sg.Cancel(button_color=Config.CANCEL_BUTTON_COLOR)
    ]
]

window = sg.Window('Add Week GUI', layout)

while True:
    event, values = window.read()

    if event in (None, 'Cancel'):
        break
    elif event == 'Add Week':
        try:
            week = int(values[Config.WEEK_KEY])
        except ValueError:
            sg.popup_error(
                'You must select a number for the week.',
                title='Error Message'
            )
            continue

        try:
            total_kcal = int(values[Config.KCAL_KEY])
        except ValueError:
            sg.popup_error(
                'You must select a number for the calories.',
                title='Error Message'
            )
            continue

        try:
            total_protein = int(values[Config.PROTEIN_KEY])
        except ValueError:
            sg.popup_error(
                'You must select a number for the protein.',
                title='Error Message'
            )
            continue

        confirmation = get_confirmation(
            f'add the following total calories and total grams of protein '
            f'to week {week}?\nCalories: {total_kcal}\nProtein: {total_protein}'
        )

        if confirmation:
            add_week(week, total_kcal, total_protein)
            sg.popup(
                f'Week {week} has been added to the database, with '
                f'{total_kcal} total calories and {total_protein} total grams '
                'of protein.',
                title='Success Message'
            )

    else:
        continue

window.close()
