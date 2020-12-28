'''Tests all the database CRUD operations for the exercise module functions.'''
import pytest
import sqlite3
from adonis_lifestyle_tracker.exercise.exercise import *


class TestExerciseFunctions:
    '''Tests all functions in the exercise module.'''
    def test_add_exercise(self):
        add_exercise(
            'Standing Dumbbell Curls',
            'PowerBlock Dumbbells',
            ":memory:"
        )
