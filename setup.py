from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ccs_reporting',
    version='1.0.0.dev1',
    description='Manages my calories and food for each week',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/esmith1412/adonis_lifestyle_tracker',
    author='Elijah Smith',
    license='GNU GPLv3',
    packages=find_packages(),
    include_package_data=True,
    entry_points='''
        [console_scripts]
        create_executable=ccs_reporting.create_executable:create_executable
    ''',
    classifiers=[
        "Programming Language :: Python :: 3.7",
        'Development Status :: 3 - Alpha',
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux"
    ],
    python_requires='~=3.7.3'
)
