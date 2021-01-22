'''Contains the PySimpleGUI layout for the Adonis Lifestyle System exercise tracker GUI.'''
import PySimpleGUI as sg
from adonis_lifestyle_tracker.layout.common import *


sg.theme('Reddit')

layout = [
    [
        sg.T('Week', size=EXERCISE_LABEL_SIZE),
        sg.InputCombo(tuple(), key='-EXERCISE_WEEK-', size=NUM_INPUT_SIZE)
    ],
    [
        sg.T('Exercise', size=EXERCISE_LABEL_SIZE),
        sg.InputCombo(tuple(), key='-EXERCISE-', font=('Any', 9), size=TEXT_INPUT_SIZE),
        sg.T('Equipment'),
        sg.InputCombo( tuple(), key='-EQUIPMENT-', font=('Any', 9), size=TEXT_INPUT_SIZE)
    ],
    [
        sg.T('Reps', size=EXERCISE_LABEL_SIZE),
        sg.InputCombo(tuple(), key='-REPS-', size=NUM_INPUT_SIZE)
    ],
    [
        sg.T('Resistance', size=EXERCISE_LABEL_SIZE),
        sg.InputCombo(tuple(), key='-RESISTANCE-', size=NUM_INPUT_SIZE)
    ],
    [
        sg.B('Add Equipment', size=BUTTON_SIZE, button_color=ADD_BUTTON_COLOR),
        sg.B(
            'Add Exercise',
            size=BUTTON_SIZE,
            button_color=ADD_BUTTON_COLOR,
            tooltip='Adds the specified exercise and its equipment to the database.'
        ),
        sg.B(
            'Add Exercise to Week',
            size=BUTTON_SIZE,
            button_color=ADD_BUTTON_COLOR,
            tooltip='Adds the specified exercise to the provided week, '
            'with its number of reps and resistance.'
        )
    ],
    [
        sg.B('Get Equipment', size=BUTTON_SIZE),
        sg.B(
            'Get Resistance',
            size=BUTTON_SIZE,
            tooltip='Displays the resistance used for the specified exercise, '
            'in the provided week, with the given rep range.'
        ),
        sg.B(
            'Update Resistance',
            size=BUTTON_SIZE,
            button_color=CHANGE_BUTTON_COLOR,
            tooltip='Updates the resistance used for the specified exercise '
            'in the provided week, with the given rep range.'
        )
    ],
    [
        sg.B(
            'Update Exercise',
            size=BUTTON_SIZE,
            button_color=CHANGE_BUTTON_COLOR,
            tooltip='Updates the equipment used for the specified exercise.'
        ),
        sg.B(
            'Delete Exercise',
            size=BUTTON_SIZE,
            button_color=DELETE_BUTTON_COLOR,
            tooltip='Deletes the specified exercise and its equipment from the database.'
        ),
        sg.B(
            'Delete Week',
            size=BUTTON_SIZE,
            button_color=DELETE_BUTTON_COLOR,
            tooltip='Deletes the week with the specified exercise, reps, and resistance.'
        )
    ]
]
