from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='adonis_lifestyle_tracker',
    version='1.0.0',
    description='Tracks my Adonis Lifestyle System food and exercise data for each week',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/esmith1412/adonis_lifestyle_tracker',
    author='Elijah Smith',
    license='GNU GPLv3',
    packages=find_packages(),
    include_package_data=True,
    entry_points='''
        [console_scripts]
        create_executable=adonis_lifestyle_tracker.create_executable:create_executable
    ''',
    classifiers=[
        "Programming Language :: Python :: 3.9",
        'Development Status :: 5 - Production/Stable',
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux"
    ],
    python_requires='~=3.9.2'
)
