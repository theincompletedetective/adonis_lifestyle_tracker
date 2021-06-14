'''Contains the PySimpleGUI layout for the Adonis Lifestyle Tracker GUI.'''
import PySimpleGUI as sg


sg.theme('Reddit')

NUTRITION_LABEL_SIZE = (7, 1)
EXERCISE_LABEL_SIZE = (10, 1)
TEXT_INPUT_SIZE = (28, 1)
NUM_INPUT_SIZE = (6, 1)
BUTTON_SIZE = (16, 1)

ADD_BUTTON_COLOR = ('white', '#008000')
CHANGE_BUTTON_COLOR = ('black', '#ffd700')
DELETE_BUTTON_COLOR = ('black', '#ff4040')

nutrition_layout = [
    [
        sg.T('Week', size=NUTRITION_LABEL_SIZE),
        sg.InputCombo(tuple(), key='-WEEK-', size=NUM_INPUT_SIZE)
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
        sg.B(
            'Add Food',
            size=BUTTON_SIZE,
            button_color=ADD_BUTTON_COLOR,
            tooltip='Adds a new food to the database, with its calories and protein.'
        ),
        sg.B(
            'Add Week',
            size=BUTTON_SIZE,
            button_color=ADD_BUTTON_COLOR,
            tooltip='Adds a new week to the database, with its total calories and protein.'
        ),
        sg.B(
            'Add Food to Week',
            size=BUTTON_SIZE,
            button_color=ADD_BUTTON_COLOR,
            tooltip='Adds a food to a week in the database.'
        )
    ],
    [
        sg.B(
            'Get Food',
            size=BUTTON_SIZE,
            tooltip='Displays the calories and protein for a food in the database.'
        ),
        sg.B(
            'Get Calories Left',
            size=BUTTON_SIZE,
            tooltip='Displays the number of calories left to consume for a week in the database.'
        ),
        sg.B(
            'Get Protein Left',
            size=BUTTON_SIZE,
            tooltip='Displays the grams of protein left to consume for a week in the database.'
        )
    ],
    [
        sg.B(
            'Update Food',
            size=BUTTON_SIZE,
            button_color=CHANGE_BUTTON_COLOR,
            tooltip='Updates the calories and/or protein for the specified food.'
        ),
        sg.B(
            'Delete Food',
            size=BUTTON_SIZE,
            button_color=DELETE_BUTTON_COLOR,
            tooltip='Deletes the specified food from the database.'
        ),
        sg.B(
            'Delete Week',
            size=BUTTON_SIZE,
            button_color=DELETE_BUTTON_COLOR,
            tooltip='Deletes the specified week and all its food from the database.'
        )
    ]
]

exercise_layout = [
    [
        sg.T('Equipment', size=EXERCISE_LABEL_SIZE),
        sg.InputCombo(tuple(), key='-EQUIPMENT-', font=('Any', 9), size=TEXT_INPUT_SIZE)
    ],
    [
        sg.T('Exercise', size=EXERCISE_LABEL_SIZE),
        sg.InputCombo(tuple(), key='-EXERCISE-', font=('Any', 9), size=TEXT_INPUT_SIZE)
    ],
    [
        sg.T('Reps', size=EXERCISE_LABEL_SIZE),
        sg.I(key='-REPS-', size=NUM_INPUT_SIZE)
    ],
    [
        sg.T('Resistance', size=EXERCISE_LABEL_SIZE),
        sg.I(key='-RESISTANCE-', size=NUM_INPUT_SIZE)
    ],
    [
        sg.B(
            'Add Equipment',
            size=BUTTON_SIZE,
            button_color=ADD_BUTTON_COLOR,
            tooltip='Adds a new piece of workout equipment to the database.'
        ),
        sg.B(
            'Get Equipment',
            size=BUTTON_SIZE,
            tooltip='Display the equipment for the specified exercise.'
        ),
        sg.B(
            'Update Equipment',
            size=BUTTON_SIZE,
            button_color=CHANGE_BUTTON_COLOR,
            tooltip='Updates the equipment for the specified exercise.'
        )
    ],
    [
        sg.B(
            'Add Exercise',
            size=BUTTON_SIZE,
            button_color=ADD_BUTTON_COLOR,
            tooltip='Adds a new exercise to the database, and chooses its equipment.'
        ),
        sg.B(
            'Get Resistance',
            size=BUTTON_SIZE,
            tooltip='Displays the resistance for the specified exercise and rep range.'
        ),
        sg.B(
            'Update Resistance',
            size=BUTTON_SIZE,
            button_color=CHANGE_BUTTON_COLOR,
            tooltip='Updates the resistance for the specified exercise and rep range.'
        )
    ],
    [
        sg.B(
            'Delete Equipment',
            size=(27, 1),
            button_color=DELETE_BUTTON_COLOR,
            tooltip='Deletes the specified equipment from the database.',
            pad=(5, 0)
        ),
        sg.B(
            'Delete Exercise',
            size=(27, 1),
            button_color=DELETE_BUTTON_COLOR,
            tooltip='Deletes the specified exercise and its equipment from the database.',
            pad=(1, 0)
        ),
    ]
]

layout = [
    [
        sg.TabGroup([[
            sg.Tab('Nutrition', nutrition_layout),
            sg.Tab('Exercise', exercise_layout)
        ]])
    ]
]
