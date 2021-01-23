'''Contains the PySimpleGUI layout for the Adonis Lifestyle Tracker GUI.'''
import PySimpleGUI as sg


sg.theme('Reddit')

NUTRITION_LABEL_SIZE = (7, 1)
EXERCISE_LABEL_SIZE = (10, 1)
TEXT_INPUT_SIZE = (28, 1)
NUM_INPUT_SIZE = (6, 1)
BUTTON_SIZE = (26, 1)

ADD_BUTTON_COLOR = ('white', '#008000')
CHANGE_BUTTON_COLOR = ('black', '#ffd700')
DELETE_BUTTON_COLOR = ('black', '#ff4040')

nutrition_layout = [
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
    ]
]

exercise_layout = [
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
    ]
]

layout = [
    [
        sg.TabGroup([[
            sg.Tab('Nutrition', nutrition_layout),
            sg.Tab('Exercise', exercise_layout)
        ]])
    ],
    [sg.Frame('Database', layout=[
        [sg.I( key='-PATH-', enable_events=True, size=(80, 1) ), sg.FileBrowse()]
    ])]
]
