'''
Contains the script that creates an executable file for the exercise and nutrition manager GUIs.
'''
import os
from pathlib import Path
from platform import system as platform_system
from pkg_resources import get_distribution as get_pkg_distribution
import click
import PySimpleGUI as sg
from PyInstaller.__main__ import run as run_pyinstaller


# To get the correct separator for the OS
OS_NAME = platform_system()

if OS_NAME == 'Windows':
    SEPARATOR = ';'
else:
    SEPARATOR = ':'


@click.command()
@click.option('-m', '--module', type=click.Choice(['nutrition', 'exercise'], case_sensitive=False) )
def create_executable(module):
    '''Creates an executable file for the exercise and nutrition manager GUIs.'''
    version_num = get_pkg_distribution('adonis_lifestyle_tracker').version

    license_path = sg.popup_get_file('Please select the license file:', title='File Selector')
    gui_path = sg.popup_get_file('Please select the GUI module:', title='Module Selector')

    if license_path and gui_path:
        run_pyinstaller([
            '--name=%s' % f'{module} manager gui ({version_num})',
            '--onefile',
            '--noconsole',
            '--specpath=%s' % os.path.dirname( os.path.abspath( os.path.dirname(__file__) ) ),
            '--add-data=%s' % f'{license_path}{SEPARATOR}.',
            gui_path,
        ])
