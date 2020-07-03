'''Adds an exercise and its equipment to the specified week in the database.'''
import PySimpleGUI as sg
from adonis_lifestyle_tracker.config import Config
from adonis_lifestyle_tracker.gui.confirmation_gui import get_confirmation
from adonis_lifestyle_tracker.exercise.exercise import add_exercise_to_week

sg.theme('Reddit')

layout = [
    [
        sg.Text(Config.WEEK_LABEL, size=Config.LABEL_SIZE),
        sg.Input(key=Config.WEEK_KEY, size=Config.WEEK_SIZE)
    ],
    [
        sg.Text(Config.EXERCISE_LABEL, size=Config.LABEL_SIZE),
        sg.Input(key=Config.EXERCISE_KEY, size=Config.EXERCISE_SIZE)
    ],
    [
        sg.Text(Config.EQUIPMENT_LABEL, size=Config.LABEL_SIZE),
        sg.Input(key=Config.EQUIPMENT_KEY, size=Config.EXERCISE_SIZE)
    ],
    [
        sg.Button(
            'Add Exercise to Week', button_color=Config.SUBMIT_BUTTON_COLOR
        ),
        sg.Cancel(button_color=Config.CANCEL_BUTTON_COLOR)
    ]
]

window = sg.Window('Add Exercise GUI', layout)

while True:
    event, values = window.read()

    if event in (None, 'Cancel'):
        break
    elif event == 'Add Exercise to Week':
        try:
            week = int(values[Config.WEEK_KEY])
        except ValueError:
            sg.popup_error(
                'You must enter a number for the week.', title='Error Message'
            )
            continue

        exercise = values[Config.EXERCISE_KEY].strip()
        equipment = values[Config.EQUIPMENT_KEY].strip()

        if not exercise:
            sg.popup_error('You must enter an exercise.', title='Error Message')
            continue

        if not equipment:
            sg.popup_error(
                'You must enter exercise equipment.', title='Error Message'
            )
            continue

        confirmation = get_confirmation(
            f'add the "{exercise}" exercise and "{equipment}" equipment '
            f'to week {week} in the database'
        )

        if confirmation:
            add_exercise(week, exercise, equipment)
            sg.popup(
                f'The "{exercise}" exercise and "{equipment}" equipment have '
                f'been successfully added to week {week} in the database.',
                title='Success Message'
            )

    else:
        continue

window.close()
