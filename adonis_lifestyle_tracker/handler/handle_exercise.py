import PySimpleGUI as sg
from adonis_lifestyle_tracker.handler.common import get_sorted_tuple
from adonis_lifestyle_tracker.exercise.add_exercise import *
from adonis_lifestyle_tracker.exercise.get_exercise import *
from adonis_lifestyle_tracker.exercise.update_exercise import *
from adonis_lifestyle_tracker.exercise.delete_exercise import *


def handle_add_equipment(window, values, db_path):
    equipment = values['-EQUIPMENT-'].strip()

    if equipment:
        confirmation = sg.popup_yes_no(
            f"Are you sure you want to add the '{equipment}' equipment to the database?", title='Confirmation'
        )

        if confirmation == 'Yes':
            sg.popup(add_equipment(db_path, equipment), title='Message')
            window['-EQUIPMENT-'].update('')
            window['-EQUIPMENT-'].update(values=get_sorted_tuple(db_path, 'id', 'equipment'))

    else:
        sg.popup_error('You must provide some equipment!', title='Error')


def handle_add_exercise(window, values, db_path):
    exercise = values['-EXERCISE-'].strip()
    equipment = values['-EQUIPMENT-'].strip()

    if exercise and equipment:
        confirmation = sg.popup_yes_no(
            f"Are you sure you want to add the '{exercise}' exercise to the database, with the '{equipment}' equipment?",
            title='Confirmation'
        )

        if confirmation == 'Yes':
            sg.popup(add_exercise(db_path, exercise, equipment), title='Message')
            window['-EXERCISE-'].update('')
            window['-EQUIPMENT-'].update('')
            window['-EXERCISE-'].update(values=get_sorted_tuple(db_path, 'id', 'exercise'))

    else:
        sg.popup_error('You must provide an exercise and its equipment!', title='Error')


def handle_get_equipment_for_exercise(values, db_path):
    exercise = values['-EXERCISE-'].strip()

    if exercise:
        sg.popup(get_equipment(db_path, exercise), title='Message')
    else:
        sg.popup_error('You must provide an exercise!', title='Error')


def handle_get_resistance_for_exercise_and_reps(values, db_path):
    exercise = values['-EXERCISE-'].strip()

    try:
        reps = int(values['-REPS-'])
    except ValueError:
        sg.popup_error('You must choose a number for the reps!', title='Error')
    else:

        if exercise and reps:
            sg.popup(get_resistance(db_path, exercise, reps), title='Message')
        else:
            sg.popup_error('You must provide an exercise and number of reps!', title='Error')


def handle_update_equipment_for_exercise(window, values, db_path):
    exercise = values['-EXERCISE-'].strip()
    equipment = values['-EQUIPMENT-'].strip()

    if exercise and equipment:
        confirmation = sg.popup_yes_no(
            f"Are you sure you want to update the equipment for the '{exercise}' exercise to '{equipment}'?",
            title='Confirmation'
        )

        if confirmation == 'Yes':
            sg.popup(update_equipment(db_path, exercise, equipment), title='Message')
            window['-EXERCISE-'].update('')
            window['-EQUIPMENT-'].update('')

    else:
        sg.popup_error('You must provide an exercise and its equipment!', title='Error')


def handle_update_resistance_for_exercise(window, values, db_path):
    exercise = values['-EXERCISE-'].strip()

    try:
        reps = int(values['-REPS-'])
    except ValueError:
        sg.popup_error('You must choose a number for the reps!', title='Error')
    else:
        resistance = values['-RESISTANCE-'].strip()

        if exercise and resistance:
            confirmation = sg.popup_yes_no(
                f"Are you sure you want to update the resistance for {reps} reps of the '{exercise}' exercise to '{resistance}'?",
                title='Confirmation'
            )

            if confirmation == 'Yes':
                sg.popup(update_resistance(db_path, exercise, reps, resistance), title='Message')
                window['-EXERCISE-'].update('')
                window['-REPS-'].update('')
                window['-RESISTANCE-'].update('')

        else:
            sg.popup_error('You must provide an exercise and resistance!', title='Error')


def handle_delete_equipment(window, values, db_path):
    equipment = values['-EQUIPMENT-'].strip()

    if equipment:
        confirmation = sg.popup_yes_no(
            f"Are you sure you want to delete the '{equipment}' equipment from the database?", title='Confirmation'
        )

        if confirmation == 'Yes':
            sg.popup(delete_equipment(db_path, equipment), title='Message')
            window['-EQUIPMENT-'].update('')
            window['-EQUIPMENT-'].update(values=get_sorted_tuple(db_path, 'id', 'equipment'))

    else:
        sg.popup_error('You must provide some equipment!', title='Error')


def handle_delete_exercise(window, values, db_path):
    exercise = values['-EXERCISE-'].strip()

    if exercise:
        confirmation = sg.popup_yes_no(
            f"Are you sure you want to delete the '{exercise}' exercise from the database?", title='Confirmation'
        )

        if confirmation == 'Yes':
            sg.popup(delete_exercise(db_path, exercise), title='Message')
            window['-EXERCISE-'].update('')
            window['-EXERCISE-'].update(values=get_sorted_tuple(db_path, 'id', 'exercise'))

    else:
        sg.popup_error('You must enter an exercise!', title='Error')
