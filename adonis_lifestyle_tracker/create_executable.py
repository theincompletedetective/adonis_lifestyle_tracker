'''
Creates the bundled version of the Adonis Lifestyle Tracker app
'''

from os.path import join as os_path_join, abspath as os_path_abspath
from platform import system as platform_system
from pkg_resources import get_distribution as get_pkg_distribution
from click import (
    command as click_command,
    option as click_option,
    Choice as ClickChoice
)
from PyInstaller.__main__ import run as run_pyinstaller


# To get the correct separator for the OS
OS_NAME = platform_system()

if OS_NAME == 'Windows':
    SEPARATOR = ';'
elif OS_NAME == 'Linux':
    SEPARATOR = ':'

# To get the correct version number for each executable
VERSION = get_pkg_distribution('adonis_lifestyle_tracker').version

# To get all the correct paths for each required file
GUI_PATH = os_path_join(os_path_abspath('.'), 'adonis_lifestyle_tracker')
WORK_PATH = os_path_join(os_path_abspath('.'), 'build')
DIST_PATH = os_path_join(os_path_abspath('.'), 'dist')
SPEC_PATH = os_path_join(os_path_abspath('.'), 'spec')
LICENSE_PATH = os_path_join(os_path_abspath('.'), f'LICENSE.txt{SEPARATOR}.')
DB_PATH = os_path_join(os_path_abspath('.'), 'adonis_lifestyle_tracker', f'app.db{SEPARATOR}.')


@click_command()
def create_executable():
    package_name = f'adonis_lifestyle_tracker_{VERSION}'

    run_pyinstaller([
        '--name=%s' % package_name,
        '--noconsole',
        '--workpath=%s' % WORK_PATH,
        '--distpath=%s' % DIST_PATH,
        '--specpath=%s' % SPEC_PATH,
        '--add-data=%s' % LICENSE_PATH,
        '--add-binary=%s' % DB_PATH,
        os_path_join(GUI_PATH, 'app.py'),
    ])
