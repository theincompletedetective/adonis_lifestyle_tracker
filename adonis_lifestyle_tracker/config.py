'''
Contains the class that has all the configurations for each field in each GUI module.
'''


class Config:
    '''
    Contains all the configurations for each field in each GUI module.
    '''
    # Text Labels and Input Field Sizes
    LABEL_SIZE = (17, 1)
    FOOD_SIZE = (30, 1)
    NUMBER_SIZE = (10, 1)
    WEEK_SIZE = (5, 1)

    # Label Text
    FOOD_LABEL = 'Food Name'
    WEEK_LABEL = 'Week Number'
    KCAL_LABEL = 'Calories (kcal)'
    PROTEIN_LABEL = 'Protein (g)'

    # PySimpleGUI Keys
    FOOD_KEY = '-FOOD-'
    KCAL_KEY = '-CALORIES-'
    PROTEIN_KEY = '-PROTEIN-'
    WEEK_KEY = '-WEEK-'

    # Tooltips
    FOOD_TOOLTIP = (
        'The name of the food to view, add to, or remove from the database'
    )

    # Buttons
    SUBMIT_BUTTON_TEXT = 'Add Food'
    SUBMIT_BUTTON_COLOR = ('white', '#008000')
    CANCEL_BUTTON_COLOR = ('black', '#ff0000')
