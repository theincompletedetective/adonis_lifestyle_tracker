'''Updates the resistance for an exercise in a given week and rep range.'''
import PySimpleGUI as sg
from adonis_lifestyle_tracker.config import Config
from adonis_lifestyle_tracker.gui.confirmation_gui import get_confirmation
from adonis_lifestyle_tracker.exercise.exercise import (
    add_5_reps_resistance,
    add_8_reps_resistance,
    add_13_reps_resistance,
    add_21_reps_resistance
)

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
        choice = values['-CHOICE-'][0].strip()

        if not exercise:
            sg.popup_error('You must enter an exercise.', title='Error Message')
            continue

        if not resistance:
            sg.popup_error(
                'You must enter some resistance.', title='Error Message'
            )
            continue

        confirmation = get_confirmation(
            f'add {resistance} resistance to {exercise} exercise, '
            f'for week {week}'
        )

        if confirmation:
            if choice == '5 Reps':
                add_5_reps_resistance(resistance, week, exercise)
            elif choice == '8 Reps':
                add_8_reps_resistance(resistance, week, exercise)
            elif choice == '13 Reps':
                add_13_reps_resistance(resistance, week, exercise)
            elif choice == '21 Reps':
                add_21_reps_resistance(resistance, week, exercise)
            else:
                sg.popup('You must choose a rep range.', title='Error Message')
                continue

            sg.popup(
                f'{resistance} resistance has been successfully added '
                f'to {exercise} exercise, for week {week}!',
                title='Success Message'
            )

window.close()
