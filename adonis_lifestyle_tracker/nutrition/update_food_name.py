''''Updates the calories or protein of a food in the nutrition database.'''

import PySimpleGUI as sg
from adonis_lifestyle_tracker.gui.confirmation_gui import get_confirmation
from adonis_lifestyle_tracker.nutrition.nutrition import update_food_name


TEXT_SIZE = (12, 1)
INPUT_SIZE = (10, 1)


sg.theme('Reddit')

layout = [
    [sg.Text( 'Old Food Name', size=(15, 1) ), sg.Input( key='-OLD_FOOD-', size=(30, 1) )],
    [sg.Text( 'New Food Name', size=(15, 1) ), sg.Input( key='-NEW_FOOD-', size=(30, 1) )],
    [
        sg.Button('Update Food Name', button_color=('white', '#008000')),
        sg.Cancel( button_color=('black', '#ff0000') )
    ]
]

window = sg.Window('Update Food GUI', layout)

while True:
    event, values = window.read()

    if event in (None, 'Cancel'):
        break
    elif event == 'Update Food Name':

        if values['-OLD_FOOD-'].strip():
            old_food = values['-OLD_FOOD-']
        else:
            sg.popup_error('You must enter the old name for the food.', title='Error')
            continue
        
        if values['-NEW_FOOD-'].strip():
            new_food = values['-NEW_FOOD-']
        else:
            sg.popup_error('You must enter a new name for the food.', title='Error')
            continue

        confirmation = get_confirmation(
            f'update food "{old_food}" with the name "{new_food}"'
        )

        if confirmation:
            update_food_name(old_food, new_food)
            sg.popup(
                f'The name for food "{old_food}" has been successfully updated!',
                title='Success Message'
            )

    else:
        continue
