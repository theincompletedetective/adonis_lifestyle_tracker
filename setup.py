from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='adonis_lifestyle_tracker',
    version='1.0.0.dev1',
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
        add_weekly_totals=adonis_lifestyle_tracker.nutrition.nutrition:add_weekly_totals
        add_food_to_week=adonis_lifestyle_tracker.nutrition.nutrition:add_food_to_week
        get_food=adonis_lifestyle_tracker.nutrition.nutrition:get_food
        get_weekly_calories_left=adonis_lifestyle_tracker.nutrition.nutrition:get_weekly_kcal_left
        get_weekly_protein_left=adonis_lifestyle_tracker.nutrition.nutrition:get_weekly_protein_left

        add_week=adonis_lifestyle_tracker.exercise.exercise:add_week
        add_equipment=adonis_lifestyle_tracker.exercise.exercise:add_equipment
        add_exercise=adonis_lifestyle_tracker.exercise.exercise:add_exercise
        add_reps=adonis_lifestyle_tracker.exercise.exercise:add_reps
        add_resistance=adonis_lifestyle_tracker.exercise.exercise:add_resistance

        add_exercise_info_to_week=adonis_lifestyle_tracker.exercise.exercise:add_exercise_info_to_week

        get_equipment=adonis_lifestyle_tracker.exercise.exercise:get_equipment
        get_resistance=adonis_lifestyle_tracker.exercise.exercise:get_resistance
        update_resistance=adonis_lifestyle_tracker.exercise.exercise:update_resistance
    ''',
    classifiers=[
        "Programming Language :: Python :: 3.7",
        'Development Status :: 3 - Alpha',
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux"
    ],
    python_requires='~=3.7.3'
)
