'''
Gets all exercise data for the specified week from the database.
'''
import pprint
import PySimpleGUI as sg
from adonis_lifestyle_tracker.config import Config
from adonis_lifestyle_tracker.exercise.exercise import get_exercise_from_week

sg.theme('Reddit')

layout = [
    [
        sg.Text(Config.WEEK_LABEL, size=Config.LABEL_SIZE),
        sg.Input(key=Config.WEEK_KEY, size=Config.WEEK_SIZE),
    ],
    [
        sg.Text(Config.EXERCISE_LABEL, size=Config.LABEL_SIZE),
        sg.Input(key=Config.EXERCISE_KEY, size=Config.EXERCISE_SIZE)
    ],
    [
        sg.Button(
            'Get Exercise from Week', button_color=Config.SUBMIT_BUTTON_COLOR
        ),
        sg.Cancel(button_color=Config.CANCEL_BUTTON_COLOR)
    ]
]

window = sg.Window('Get Exercise GUI', layout)

while True:
    event, values = window.read()

    if event in (None, 'Cancel'):
        break
    elif event == 'Get Exercise from Week':
        try:
            week = int(values[Config.WEEK_KEY])
        except ValueError:
            sg.popup_error(
                'You must enter a number for the week.', title='Error Message'
            )
            continue

        exercise = values[Config.EXERCISE_KEY].strip()

        if not exercise:
            sg.popup_error('You must enter an exercise.', title='Error Message')
            continue

        week, exercise, equipment, reps_5, reps_8, reps_13, reps_21 = get_exercise_from_week(week, exercise)
        sg.popup(
            f'Week: {week}\n'
            f'Equipment: {equipment}\n'
            f'5 Reps Resistance: {reps_5}\n'
            f'8 Reps Resistance: {reps_8}\n'
            f'13 Reps Resistance: {reps_13}\n'
            f'21 Reps Resistance: {reps_21}',
            title=exercise
        )
    else:
        continue

window.close()
