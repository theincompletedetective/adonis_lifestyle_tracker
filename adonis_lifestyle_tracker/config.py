'''
Contains the class that has all the configurations for each field in each GUI module.
'''


class Config:
    '''
    Contains all the configurations for each field in each GUI module.
    '''
    # Absolute paths to databases
    NUTRITION_DB_PATH = '/home/elijah/Programming/Python/projects/adonis_lifestyle_tracker/adonis_lifestyle_tracker/nutrition/nutrition.db'

    # Text Labels and Input Field Sizes
    LABEL_SIZE = (17, 1)
    FOOD_SIZE = (30, 1)
    NUMBER_SIZE = (10, 1)
    WEEK_SIZE = (5, 1)
    EXERCISE_SIZE = (35, 1)

    # Label Text
    FOOD_LABEL = 'Food Name'
    WEEK_LABEL = 'Week Number'
    KCAL_LABEL = 'Calories (kcal)'
    PROTEIN_LABEL = 'Protein (g)'
    EXERCISE_LABEL = 'Exercise Name'
    EQUIPMENT_LABEL = 'Equipment Name'
    REPS_5_LABEL = '5 Reps Resistance'
    REPS_8_LABEL = '8 Reps Resistance'
    REPS_13_LABEL = '13 Reps Resistance'
    REPS_21_LABEL = '21 Reps Resistance'

    # PySimpleGUI Keys
    FOOD_KEY = '-FOOD-'
    KCAL_KEY = '-CALORIES-'
    PROTEIN_KEY = '-PROTEIN-'
    WEEK_KEY = '-WEEK-'
    EXERCISE_KEY = '-EXERCISE-'
    EQUIPMENT_KEY = '-EQUIPMENT-'
    REPS_5_KEY = '-5_REPS-'
    REPS_8_KEY = '-8_REPS-'
    REPS_13_KEY = '-13_REPS-'
    REPS_21_KEY = '-21_REPS-'

    # Tooltips
    FOOD_TOOLTIP = (
        'The name of the food to view, add to, or remove from the database'
    )

    # Buttons
    SUBMIT_BUTTON_TEXT = 'Add Food'
    SUBMIT_BUTTON_COLOR = ('white', '#008000')
    CANCEL_BUTTON_COLOR = ('black', '#ff0000')
