'''Contains the PySimpleGUI layout for the Adonis Lifestyle System nutrition tracker GUI.'''
import PySimpleGUI as sg
from adonis_lifestyle_tracker.layout.common import *


sg.theme('Reddit')

layout = [
    [
        sg.T('Week', size=NUTRITION_LABEL_SIZE),
        sg.InputCombo(tuple(), key='-NUTRITION_WEEK-', size=NUM_INPUT_SIZE)
    ],
    [
        sg.T('Food', size=NUTRITION_LABEL_SIZE),
        sg.InputCombo(tuple(), key='-FOOD-', font=('Any', 9), size=TEXT_INPUT_SIZE)
    ],
    [
        sg.T('Calories', size=NUTRITION_LABEL_SIZE),
        sg.I(key='-KCAL-', size=NUM_INPUT_SIZE)
    ],
    [
        sg.T('Protein', size=NUTRITION_LABEL_SIZE),
        sg.I(key='-PROTEIN-', size=NUM_INPUT_SIZE)
    ],
    [
        sg.B('Add Food', size=BUTTON_SIZE, button_color=ADD_BUTTON_COLOR),
        sg.B(
            'Add Totals to Week',
            size=BUTTON_SIZE,
            button_color=ADD_BUTTON_COLOR,
            tooltip='Adds the total calories and total protein for the specified week.'
        ),
        sg.B('Add Food to Week', size=BUTTON_SIZE, button_color=ADD_BUTTON_COLOR)
    ],
    [
        sg.B(
            'Get Food',
            size=BUTTON_SIZE,
            tooltip='Displays the calories and protein for the specified food.'
        ),
        sg.B(
            'Get Calories Left',
            size=BUTTON_SIZE,
            tooltip='Displays the number of calories left to consume for the specified week.'
        ),
        sg.B(
            'Get Protein Left',
            size=BUTTON_SIZE,
            tooltip='Displays the grams of protein left to consume for the specified week.'
        )
    ],
    [
        sg.B(
            'Get Week Totals',
            size=BUTTON_SIZE,
            tooltip='Displays the total calories and protein for the specified week.'
        ),
        sg.B(
            'Update Food',
            size=BUTTON_SIZE,
            button_color=CHANGE_BUTTON_COLOR,
            tooltip='Updates the calories and protein for the specified food.'
        ),
        sg.B(
            'Delete Food',
            size=BUTTON_SIZE,
            button_color=DELETE_BUTTON_COLOR,
            tooltip='Deletes the specified food from the database.'
        ),
    ],
    [sg.I( key='-PATH-', size=(80, 1), tooltip='Enter the absolute path to the database.' ), sg.FileBrowse()]
]
