'''Contains the handler functions to manage the exercise information in the manager GUI.'''
import PySimpleGUI as sg
from adonis_lifestyle_tracker.common.common import get_sorted_tuple
from adonis_lifestyle_tracker.exercise.exercise import (
    add_equipment,
    add_exercise,
    add_exercise_to_week,
    get_equipment,
    get_resistance,
    change_resistance
)


def handle_add_equipment(db_path, window, values):
    '''Handles the event to add the specified equipment to the database.'''
    equipment = values['-EQUIPMENT-'].strip()

    if equipment:
        confirmation = sg.popup_yes_no(
            f"Are you sure you want to add the '{equipment}' equipment to the database?",
            title='Confirmation'
        )

        if confirmation == 'Yes':
            sg.popup(add_equipment(db_path, equipment), title='Message')
            window['-EQUIPMENT-'].update('')
            window['-EQUIPMENT-'].update( values=get_sorted_tuple(db_path, 'id', 'equipment') )
    else:
        sg.popup_error('You must provide equipment!', title='Error')


def handle_add_exercise(db_path, window, values):
    '''Handles the event to add the specified exercise to the database.'''
    exercise = values['-EXERCISE-'].strip()
    equipment = values['-EQUIPMENT-'].strip()

    if exercise and equipment:
        confirmation = sg.popup_yes_no(
            f"Are you sure you want to add the '{exercise}' exercise with "
            f"the '{equipment}' equipment to the database?",
            title='Confirmation'
        )

        if confirmation == 'Yes':
            sg.popup(add_exercise(db_path, exercise, equipment), title='Message')
            window['-EXERCISE-'].update('')
            window['-EQUIPMENT-'].update('')
            window['-EXERCISE-'].update( values=get_sorted_tuple(db_path, 'id', 'exercise') )
    else:
        sg.popup_error(
            'You must provide an exercise and its equipment!',
            title='Error'
        )


def handle_add_exercise_to_week(db_path, window, values):
    '''Handles the event to add the specified exercise, reps, and resistance to the given week.'''
    try:
        week = int(values['-EXERCISE_WEEK-'])
    except ValueError:
        sg.popup_error('You must choose a number for the week!', title='Error')
        return

    exercise = values['-EXERCISE-'].strip()

    try:
        reps = int(values['-REPS-'])
    except ValueError:
        sg.popup_error('You must choose a number for the reps!', title='Error')
        return

    resistance = values['-RESISTANCE-'].strip()

    if exercise and resistance:
        confirmation = sg.popup_yes_no(
            f"Are you sure you want to add the '{exercise}' exercise with "
            f"the '{reps}' reps and '{resistance}' resistance to week {week} in the database?",
            title='Confirmation'
        )

        if confirmation == 'Yes':
            sg.popup(
                add_exercise_to_week(db_path, week, exercise, reps, resistance),
                title='Message'
            )

            # To clear the input fields
            window['-EXERCISE_WEEK-'].update('')
            window['-EXERCISE-'].update('')
            window['-REPS-'].update('')
            window['-RESISTANCE-'].update('')

            # To add the new information to the dropdowns
            window['-EXERCISE_WEEK-'].update( values=get_sorted_tuple(db_path, 'week', 'week_exercise') )
            window['-REPS-'].update( values=get_sorted_tuple(db_path, 'reps', 'week_exercise') )
            window['-RESISTANCE-'].update( values=get_sorted_tuple(db_path, 'resistance', 'week_exercise') )
    else:
        sg.popup_error(
            'You must provide an exercise and resistance!', title='Error'
        )


def handle_get_equipment(db_path, values):
    '''Handles the event to display the equipment used for the given exercise.'''
    exercise = values['-EXERCISE-'].strip()

    if exercise:
        sg.popup( get_equipment(db_path, exercise), title='Message' )
    else:
        sg.popup_error('You must provide an exercise!', title='Error')


def handle_get_resistance(db_path, values):
    '''
    Handles the event to display the resistance used for a given rep range,
    in a given week.
    '''
    try:
        week = int(values['-EXERCISE_WEEK-'])
    except ValueError:
        sg.popup_error('You must choose a number for the week!', title='Error')
        return

    exercise = values['-EXERCISE-'].strip()

    try:
        reps = int(values['-REPS-'])
    except ValueError:
        sg.popup_error('You must choose a number for the reps!', title='Error')
        return

    if exercise and reps:
        sg.popup(
            get_resistance(db_path, week, exercise, reps),
            title='Message'
        )
    else:
        sg.popup_error(
            'You must provide an exercise and number of reps!', title='Error'
        )


def handle_change_resistance(db_path, window, values):
    '''Handles the event to update the resistance for a given exercise, in the specified week.'''
    try:
        week = int(values['-EXERCISE_WEEK-'])
    except ValueError:
        sg.popup_error('You must choose a number for the week!', title='Error')
        return

    exercise = values['-EXERCISE-'].strip()

    try:
        reps = int(values['-REPS-'])
    except ValueError:
        sg.popup_error('You must choose a number for the reps!', title='Error')
        return

    new_resistance = values['-RESISTANCE-'].strip()

    if exercise and new_resistance:
        confirmation = sg.popup_yes_no(
            f"Are you sure you want to update the resistance for week {week}, "
            f"the '{exercise}' exercise, and {reps} reps to '{new_resistance}' in the database?",
            title='Confirmation'
        )

        if confirmation == 'Yes':
            sg.popup(
                change_resistance(db_path, week, exercise, reps, new_resistance),
                title='Message'
            )

            # To clear the input fields
            window['-EXERCISE_WEEK-'].update('')
            window['-EXERCISE-'].update('')
            window['-REPS-'].update('')
            window['-RESISTANCE-'].update('')

            window['-RESISTANCE-'].update( values=get_sorted_tuple(db_path, 'resistance', 'week_exercise') )
    else:
        sg.popup_error(
            'You must provide an exercise and resistance!', title='Error'
        )
