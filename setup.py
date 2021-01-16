from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='adonis_lifestyle_tracker',
    version='1.0.0b1',
    description='Helps to manage my calories and food for each week, using the AGR nutrition calculator',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/esmith1412/adonis_lifestyle_tracker',
    author='Elijah Smith',
    license='GNU GPLv3',
    packages=find_packages(),
    include_package_data=True,
    entry_points='''
        [console_scripts]
        add_food=adonis_lifestyle_tracker.nutrition.nutrition:add_food
        add_totals_to_week=adonis_lifestyle_tracker.nutrition.nutrition:add_totals_to_week
        add_food_to_week=adonis_lifestyle_tracker.nutrition.nutrition:add_food_to_week
        get_food=adonis_lifestyle_tracker.nutrition.nutrition:get_food
        get_calories_left=adonis_lifestyle_tracker.nutrition.nutrition:get_calories_left
        get_protein_left=adonis_lifestyle_tracker.nutrition.nutrition:get_protein_left
        add_exercise=adonis_lifestyle_tracker.exercise.exercise:add_exercise
        add_exercise_to_week=adonis_lifestyle_tracker.exercise.exercise:add_exercise_to_week
        get_equipment=adonis_lifestyle_tracker.exercise.exercise:get_equipment
        get_resistance=adonis_lifestyle_tracker.exercise.exercise:get_resistance
        change_resistance=adonis_lifestyle_tracker.exercise.exercise:change_resistance
    ''',
    classifiers=[
        "Programming Language :: Python :: 3.7",
        'Development Status :: 4 - Beta',
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux"
    ],
    python_requires='~=3.7.3'
)
