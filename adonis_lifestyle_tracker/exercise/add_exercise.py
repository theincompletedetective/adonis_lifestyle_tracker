'''Adds an exercise and its equipment to the  exercise table in the database.'''
from sqlite3 import IntegrityError
import PySimpleGUI as sg
from adonis_lifestyle_tracker.config import Config
from adonis_lifestyle_tracker.confirmation.confirmation import get_confirmation
from adonis_lifestyle_tracker.exercise.exercise import add_exercise

sg.theme('Reddit')

layout = [
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
            'Add Exercise', button_color=Config.SUBMIT_BUTTON_COLOR
        ),
        sg.Cancel(button_color=Config.CANCEL_BUTTON_COLOR)
    ]
]

window = sg.Window('Add Exercise GUI', layout)

while True:
    event, values = window.read()

    if event in (None, 'Cancel'):
        break
    elif event == 'Add Exercise':
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
            f"add the '{exercise}' exercise with equipment '{equipment}' "
            "to the database"
        )

        if confirmation:
            try:
                add_exercise(exercise, equipment)

                # To clear the input fields
                window[Config.EXERCISE_KEY].update('')
                window[Config.EQUIPMENT_KEY].update('')

                # To display a success message
                sg.popup(
                    f"The '{exercise}' exercise with equipment '{equipment}' "
                    "has been successfully added to the database",
                    title='Success Message'
                )
            except IntegrityError:
                sg.popup_error(
                    f"The exercise '{exercise}' has already been added "
                    "to the database.",
                    title='Error Message'
                )

    else:
        continue

window.close()
