'''Contains the absolute path to the nutrition and exercise databases.'''
import os


NUTRITION_DB_PATH = os.path.join(os.path.dirname(__file__), 'nutrition', 'nutrition.db')
EXERCISE_DB_PATH = os.path.join(os.path.dirname(__file__), 'exercise', 'exercise.db')
