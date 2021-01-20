'''Contains the variables and functions needed by both the exercise and nutrition scripts.'''
from os.path import (
    join as os_path_join,
    abspath as os_path_abspath,
    dirname as os_path_dirname
)
from pathlib import Path


DB_PATH = os_path_join(
    os_path_abspath(Path( os_path_dirname(__file__) ).parent), # the adonis_lifestyle_tracker directory
    'database',
    'tracker.db'
)
