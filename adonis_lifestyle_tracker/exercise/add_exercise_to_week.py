'''Adds an exercise and its equipment to the specified week in the database.'''
from sqlite3 import IntegrityError
import PySimpleGUI as sg
from adonis_lifestyle_tracker.config import Config
from adonis_lifestyle_tracker.confirmation.confirmation import get_confirmation
from adonis_lifestyle_tracker.validation.validate_exercise import (
    validate_resistance
)
from adonis_lifestyle_tracker.exercise.exercise import add_exercise_to_week

sg.theme('Reddit')

required_layout = [
    [
        sg.Frame('Week', layout=[
            [sg.Input(key=Config.WEEK_KEY, size=Config.WEEK_SIZE)],
        ]),
    ],
    [
        sg.Frame('Exercise', layout=[
            [sg.Input(key=Config.EXERCISE_KEY, size=Config.EXERCISE_SIZE)],
        ]),
    ]
]

optional_layout = [
    [
        sg.Text(Config.REPS_5_LABEL, size=Config.LABEL_SIZE),
        sg.Input(key=Config.REPS_5_KEY, size=Config.NUMBER_SIZE)
    ],
    [
        sg.Text(Config.REPS_8_LABEL, size=Config.LABEL_SIZE),
        sg.Input(key=Config.REPS_8_KEY, size=Config.NUMBER_SIZE)
    ],
    [
        sg.Text(Config.REPS_13_LABEL, size=Config.LABEL_SIZE),
        sg.Input(key=Config.REPS_13_KEY, size=Config.NUMBER_SIZE)
    ],
    [
        sg.Text(Config.REPS_21_LABEL, size=Config.LABEL_SIZE),
        sg.Input(key=Config.REPS_21_KEY, size=Config.NUMBER_SIZE)
    ]
]

layout = [
    [
        sg.TabGroup(
            [
                [
                    sg.Tab('Required', required_layout),
                    sg.Tab('Optional', optional_layout)
                ]
            ]
        )
    ],
    [
        sg.Button(
            'Add Exercise to Week', button_color=Config.SUBMIT_BUTTON_COLOR
        ),
        sg.Cancel(button_color=Config.CANCEL_BUTTON_COLOR)
    ]
]

window = sg.Window('Add Exercise to Week GUI', layout)

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

        # Required Fields
        exercise = values[Config.EXERCISE_KEY].strip()

        if not exercise:
            sg.popup_error('You must enter an exercise.', title='Error Message')
            continue

        # Optional Fields
        reps_5 = values[Config.REPS_5_KEY].strip()
        reps_8 = values[Config.REPS_8_KEY].strip()
        reps_13 = values[Config.REPS_13_KEY].strip()
        reps_21 = values[Config.REPS_21_KEY].strip()

        if not validate_resistance(reps_5, reps_8, reps_13, reps_21):
            sg.popup(
                'You have entered an invalid value for one of the rep ranges.',
                title='Error Message'
            )
            continue

        confirmation = get_confirmation(
            f'add the "{exercise}" exercise to week {week}'
        )

        if confirmation:
            try:
                add_exercise_to_week(
                    week, exercise, reps_5=reps_5, reps_8=reps_8,
                    reps_13=reps_13, reps_21=reps_21
                )
                sg.popup(
                    f"The '{exercise}' exercise has been successfully added "
                    f"to week {week}.",
                    title='Success Message'
                )
            except IntegrityError:
                sg.popup_error(
                    f"The '{exercise}' exercise has already been added "
                    "to the database.",
                    title='Error Message'
                )

    else:
        continue

window.close()
