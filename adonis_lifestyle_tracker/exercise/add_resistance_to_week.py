'''Updates the resistance for an exercise in a given week and rep range.'''
import PySimpleGUI as sg
from adonis_lifestyle_tracker.config import Config
from adonis_lifestyle_tracker.validation.validate_exercise import (
    validate_resistance
)
from adonis_lifestyle_tracker.confirmation.confirmation import get_confirmation
from adonis_lifestyle_tracker.exercise.exercise import add_resistance

sg.theme('Reddit')

layout = [
    [sg.Text('Which rep range did you want to update?')],
    [
        sg.Listbox(
            ('5 Reps', '8 Reps', '13 Reps', '21 Reps'),
            size=(15, 4),
            key='-CHOICE-'
        )
    ],
    [
        sg.Text(Config.WEEK_LABEL, size=Config.LABEL_SIZE),
        sg.Input(key=Config.WEEK_KEY, size=Config.WEEK_SIZE),
    ],
    [
        sg.Text(Config.EXERCISE_LABEL, size=Config.LABEL_SIZE),
        sg.Input(key=Config.EXERCISE_KEY, size=Config.EXERCISE_SIZE)
    ],
    [
        sg.Text('Resistance', size=Config.LABEL_SIZE),
        sg.Input(key='-RESISTANCE-', size=Config.EXERCISE_SIZE)
    ],
    [
        sg.Button(
            'Add Resistance', button_color=Config.SUBMIT_BUTTON_COLOR
        ),
        sg.Cancel(button_color=Config.CANCEL_BUTTON_COLOR)
    ]
]

window = sg.Window('Add Resistance GUI', layout)

while True:
    event, values = window.read()

    if event in (None, 'Cancel'):
        break
    elif event == 'Add Resistance':
        try:
            week = int(values[Config.WEEK_KEY])
        except ValueError:
            sg.popup_error(
                'You must enter a number for the week.', title='Error Message'
            )
            continue

        exercise = values[Config.EXERCISE_KEY].strip()
        resistance = values['-RESISTANCE-'].strip()

        try:
            choice = values['-CHOICE-'][0]
        except IndexError:
            choice = None

        if not exercise:
            sg.popup_error('You must enter an exercise.', title='Error Message')
            continue

        if not resistance or not validate_resistance(resistance):
            sg.popup_error(
                'You must enter some resistance in the correct format.',
                title='Error Message'
            )
            continue

        if not choice:
            sg.popup_error(
                'You must choose a rep range.', title='Error Message'
            )
            continue

        confirmation = get_confirmation(
            f'update the "{choice}" rep range of the {exercise} exercise '
            f'for week {week}, with {resistance} of resistance'
        )

        if confirmation:
            if choice == '5 Reps':
                add_resistance('reps_5', resistance, week, exercise)
            elif choice == '8 Reps':
                add_resistance('reps_8', resistance, week, exercise)
            elif choice == '13 Reps':
                add_resistance('reps_13', resistance, week, exercise)
            elif choice == '21 Reps':
                add_resistance('reps_21', resistance, week, exercise)

            sg.popup(
                f'{resistance} resistance has been successfully added '
                f'to {exercise} exercise, for week {week}!',
                title='Success Message'
            )

window.close()
