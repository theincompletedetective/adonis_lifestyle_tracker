"""Contains the PySimpleGUI layout for the Adonis Lifestyle Tracker nutrition GUI."""
import PySimpleGUI as sg


sg.theme('Reddit')

NUTRITION_LABEL_SIZE = (8, 1)
EXERCISE_LABEL_SIZE = (10, 1)
TEXT_INPUT_SIZE = (42, 1)
NUM_INPUT_SIZE = (6, 1)
BUTTON_SIZE = (25, 1)

ADD_BUTTON_COLOR = ('white', '#008000')
CHANGE_BUTTON_COLOR = ('black', '#ffd700')
DELETE_BUTTON_COLOR = ('black', '#ff4040')

layout = [
    [
        sg.T('Week', size=NUTRITION_LABEL_SIZE),
        sg.InputCombo(tuple(), key='-WEEK-', size=NUM_INPUT_SIZE)
    ],
    [
        sg.T('Weekday', size=NUTRITION_LABEL_SIZE),
        sg.I(key='-DATE-', size=(10, 1), disabled=True),
        sg.CalendarButton(
            'Choose Date', close_when_date_chosen=True,  target='-DATE-', no_titlebar=False, format="%m-%d-%Y"
        )
    ],
    [
        sg.T('Food', size=NUTRITION_LABEL_SIZE),
        sg.InputCombo(tuple(), key='-FOOD-', font=('Any', 9), size=(55, 1)),
        sg.T('Quantity'),
        sg.InputCombo([x + 1 for x in range(20)], key='-QUANTITY-', font=('Any', 9), size=(3, 1), default_value=1),
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
            'Add Food to Day',
            size=BUTTON_SIZE,
            button_color=ADD_BUTTON_COLOR,
            tooltip='Adds a food to a day of the week in the database.'
        )
    ],
    [
        sg.B(
            "Get Food's Calories and Protein",
            size=BUTTON_SIZE,
            tooltip='Displays the calories and protein for a food in the database.'
        ),
        sg.B(
            'Get Total Calories for Week',
            size=BUTTON_SIZE,
            tooltip='Displays the total number of calories to consume for a week in the database.'
        ),
        sg.B(
            'Get Total Protein for Week',
            size=BUTTON_SIZE,
            tooltip='Displays the total grams of protein to consume for a week in the database.'
        )
    ],
    [
        sg.B(
            'Get Calories Eaten for Day',
            size=BUTTON_SIZE,
            tooltip='Displays the number of calories eaten on the given day of the given week.'
        ),
        sg.B(
            'Get Protein Eaten for Day',
            size=BUTTON_SIZE,
            tooltip='Displays the number of grams of protein eaten on the given day of the given week.'
        ),
        sg.B(
            'Get Calories Left for Week',
            size=BUTTON_SIZE,
            tooltip='Displays the number of calories left to consume for a week in the database.'
        ),
        sg.B(
            'Get Protein Left for Week',
            size=BUTTON_SIZE,
            tooltip='Displays the grams of protein left to consume for a week in the database.'
        )
    ],
    [
        sg.B(
            'Update Calories',
            size=(18, 1),
            button_color=CHANGE_BUTTON_COLOR,
            tooltip='Updates the calories for the specified food.'
        ),
        sg.B(
            'Update Protein',
            size=(17, 1),
            button_color=CHANGE_BUTTON_COLOR,
            tooltip='Updates the protein for the specified food.'
        ),
        sg.B(
            'Delete Food',
            size=(17, 1),
            button_color=DELETE_BUTTON_COLOR,
            tooltip='Deletes the specified food from the database.'
        ),
        sg.B(
            'Delete Week',
            size=(17, 1),
            button_color=DELETE_BUTTON_COLOR,
            tooltip='Deletes the specified week and all its food from the database.'
        )
    ],
    [sg.Frame('Database Path', layout=[
        [
            sg.I(key='-PATH-', disabled=True, enable_events=True, size=(58, 1)),
            sg.FileBrowse(),
            sg.Button('Load Database', button_color=('white', '#8a2be2'))
        ]
    ])]
]
