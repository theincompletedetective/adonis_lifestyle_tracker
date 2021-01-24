'''
Contains the absolute path to the database, for the nutrition
and exercise scripts.
'''
import os
from pathlib import Path


root_package_path = Path( os.path.abspath( os.path.dirname(__file__) ) ).parent
DB_PATH = os.path.join(root_package_path, 'database.db')
