'''Contains the absolute path to the database, for the exercise and nutrition scripts.'''
import os.path


DB_PATH = os.path.join(os.path.abspath( os.path.dirname(__file__) ), 'tracker.db')
