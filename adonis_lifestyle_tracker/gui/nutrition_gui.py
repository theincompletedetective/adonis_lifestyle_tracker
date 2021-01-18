'''
Contains the functions needed to add and update nutrition information in the database,
using a GUI.
'''
import PySimpleGUI as sg
from adonis_lifestyle_tracker.common import DB_PATH, get_sorted_tuple
from adonis_lifestyle_tracker.nutrition import (
    add_food,
    add_totals_to_week,
    add_food_to_week,
    get_food,
    get_calories_left,
    get_protein_left
)


sg.theme('Reddit')

LABEL_SIZE = (10, 1)
NUM_INPUT_SIZE = (6, 1)
BUTTON_SIZE = (18, 1)

ADD_BUTTON_COLOR = ('white', '#008000')

WEEKS = get_sorted_tuple(DB_PATH, 'id', 'week')
FOODS = get_sorted_tuple(DB_PATH, 'id', 'food')

layout = [
    [sg.T('Week', size=LABEL_SIZE), sg.InputCombo( WEEKS, key='-WEEK-', size=(5, 1) )],
    [sg.T('Calories', size=LABEL_SIZE), sg.I(key='-KCAL-', size=NUM_INPUT_SIZE)],
    [sg.T('Protein', size=LABEL_SIZE), sg.I(key='-PROTEIN-', size=NUM_INPUT_SIZE)],
    [sg.T('Food', size=LABEL_SIZE), sg.InputCombo( FOODS, key='-FOOD-', size=(30, 1) )],
    [
        sg.B('Add Food', size=BUTTON_SIZE, button_color=ADD_BUTTON_COLOR),
        sg.B('Add Totals to Week', size=BUTTON_SIZE, button_color=ADD_BUTTON_COLOR),
        sg.B('Add Food to Week', size=BUTTON_SIZE, button_color=ADD_BUTTON_COLOR),
    ],
    [
        sg.B('Get Food', size=BUTTON_SIZE),
        sg.B('Get Calories Left', size=BUTTON_SIZE),
        sg.B('Get Protein Left', size=BUTTON_SIZE)
    ],
    [sg.Cancel( size=BUTTON_SIZE, button_color=('black', '#ff4040') )]
]

window = sg.Window('Nutrition Manager', layout)

while True:
    event, values = window.read()

    if event in (None, 'Cancel'):
        break

    if event == 'Add Food':
        food = values['-FOOD-'].strip()

        try:
            calories = int( values['-KCAL-'].strip() )
        except ValueError:
            sg.popup_error(
                'You must provide a number for the calories!',
                title='Error'
            )
            continue

        try:
            protein = int( values['-PROTEIN-'].strip() )
        except ValueError:
            sg.popup_error(
                'You must provide a number for the grams of protein!',
                title='Error'
            )
            continue

        if food and calories and protein:
            sg.popup(
                add_food(DB_PATH, food, calories, protein), title='Message'
            )
        else:
            sg.popup_error(
                'You must provide a food name, calories, and protein!',
                title='Error'
            )

        window['-FOOD-'].update( values=get_sorted_tuple(DB_PATH, 'id', 'food') )
    elif event == 'Add Totals to Week':

        try:
            week = int( values['-WEEK-'].strip() )
        except ValueError:
            sg.popup_error(
                'You must provide a number for the week!',
                title='Error'
            )
            continue

        try:
            calories = int( values['-KCAL-'].strip() )
        except ValueError:
            sg.popup_error(
                'You must provide a number for the calories!',
                title='Error'
            )
            continue

        try:
            protein = int( values['-PROTEIN-'].strip() )
        except ValueError:
            sg.popup_error(
                'You must provide a number for the grams of protein!',
                title='Error'
            )
            continue

        sg.popup(
            add_totals_to_week(DB_PATH, week, calories, protein),
            title='Message'
        )
        window['-WEEK-'].update( values=get_sorted_tuple(DB_PATH, 'id', 'week') )
    elif event == 'Add Food to Week':
        food = values['-FOOD-'].strip()

        try:
            week = int( values['-WEEK-'].strip() )
        except ValueError:
            sg.popup_error(
                'You must provide a number for the week!',
                title='Error'
            )
            continue

        if food:
            sg.popup(
                add_food_to_week(DB_PATH, week, food),
                title='Message'
            )
        else:
            sg.popup_error('You must enter a food!', title='Error')

    elif event == 'Get Food':
        food = values['-FOOD-'].strip()

        if food:
            sg.popup(get_food(DB_PATH, food), title='Message')
        else:
            sg.popup_error('You must enter a food!', title='Error')

    elif event == 'Get Calories Left':
        try:
            week = int( values['-WEEK-'].strip() )
        except ValueError:
            sg.popup_error(
                'You must provide a number for the week!',
                title='Error'
            )
            continue

        sg.popup(get_calories_left(DB_PATH, week), title='Message')
    elif event == 'Get Protein Left':
        try:
            week = int( values['-WEEK-'].strip() )
        except ValueError:
            sg.popup_error(
                'You must provide a number for the week!',
                title='Error'
            )
            continue

        sg.popup(get_protein_left(DB_PATH, week), title='Message')
    else:
        continue

window.close()
