'''
Contains all the functions to validate data entered into the
exercise GUIs.
'''
import re


def validate_resistance(reps_5=None, reps_8=None, reps_13=None, reps_21=None):
    '''
    Ensures the resistance entered for a given number of reps is
    in the correct format.
    '''
    resistance_regex = re.compile('\d+lbs')

    if reps_5 and not resistance_regex.match(reps_5):
        return False

    if reps_8 and not resistance_regex.match(reps_8):
        return False

    if reps_13 and not resistance_regex.match(reps_13):
        return False

    if reps_21 and not resistance_regex.match(reps_21):
        return False

    return True
