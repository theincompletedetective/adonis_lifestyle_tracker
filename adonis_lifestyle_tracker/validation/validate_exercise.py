'''
Contains all the functions to validate data entered into the
exercise GUIs.
'''
import re


def validate_reps(reps):
    '''
    Ensures the resistance entered for a given number of reps is
    in the correct format.
    '''
    reps_regex = re.compile(r'\d+lbs')

    if not reps_regex.match(reps):
        return False

    return True
