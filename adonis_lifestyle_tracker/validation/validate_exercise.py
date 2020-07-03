'''
Contains all the functions to validate data entered into the
exercise GUIs.
'''
import re


def validate_resistance(*args):
    '''
    Ensures the resistance entered for a given number of reps is
    in the correct format.
    '''
    resistance_regex = re.compile('\d+lbs')

    for rep_range in args:
        if rep_range and not resistance_regex.match(rep_range):
            return False

    return True
