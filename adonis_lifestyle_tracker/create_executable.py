"""
Creates the bundled version of the Adonis Lifestyle Tracker nutrition or exercise app
"""

from os.path import join as os_path_join, abspath as os_path_abspath
from platform import system as platform_system

import click
from pkg_resources import get_distribution as get_pkg_distribution
from PyInstaller.__main__ import run as run_pyinstaller

# To get the correct separator for the OS
OS_NAME = platform_system()

if OS_NAME == 'Windows':
    SEPARATOR = ';'
else:
    SEPARATOR = ':'

# To get the correct version number for each executable
VERSION = get_pkg_distribution('adonis_lifestyle_tracker').version

# To get all the correct paths for each required file
WORK_PATH = os_path_join(os_path_abspath('.'), 'build')
DIST_PATH = os_path_join(os_path_abspath('.'), 'dist')
SPEC_PATH = os_path_join(os_path_abspath('.'), 'spec')
LICENSE_PATH = os_path_join(os_path_abspath('.'), f'LICENSE.txt{SEPARATOR}.')
ICON_PATH = os_path_join(os_path_abspath('.'), f'adonis_lifestyle_tracker_logo.ico')


@click.option('-t',
              '--tracker',
              type=click.Choice(['nutrition', 'exercise']),
              required=True,
              help='The exercise or nutrition tracker program')
@click.command()
def create_executable(tracker):
    gui_path = os_path_join(os_path_abspath('.'), 'adonis_lifestyle_tracker', tracker, f'{tracker}.py')
    run_pyinstaller([
        '--name=%s' % 'adonis_lifestyle_tracker',
        '--onefile',
        '--noconsole',
        '--workpath=%s' % WORK_PATH,
        '--distpath=%s' % DIST_PATH,
        '--specpath=%s' % SPEC_PATH,
        '--add-data=%s' % LICENSE_PATH,
        '--icon=%s' % ICON_PATH,
        gui_path
    ])
