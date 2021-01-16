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
        add_weekly_food=adonis_lifestyle_tracker.nutrition.nutrition:add_weekly_food
        get_food=adonis_lifestyle_tracker.nutrition.nutrition:get_food
        get_weekly_kcal_left=adonis_lifestyle_tracker.nutrition.nutrition:get_weekly_kcal_left
        get_weekly_protein_left=adonis_lifestyle_tracker.nutrition.nutrition:get_weekly_protein_left
        add_weekly_exercise=adonis_lifestyle_tracker.exercise.create:add_weekly_exercise
        add_exercise=adonis_lifestyle_tracker.exercise.create:add_exercise
        add_equipment=adonis_lifestyle_tracker.exercise.create:add_equipment
        add_reps=adonis_lifestyle_tracker.exercise.create:add_reps
        add_resistance=adonis_lifestyle_tracker.exercise.create:add_resistance
        add_exercise_reps_resistance_to_week=adonis_lifestyle_tracker.exercise.create:add_exercise_reps_resistance_to_week
        get_equipment=adonis_lifestyle_tracker.exercise.read:get_equipment
        get_resistance=adonis_lifestyle_tracker.exercise.read:get_resistance
        update_equipment=adonis_lifestyle_tracker.exercise.update:update_equipment
        update_exercise=adonis_lifestyle_tracker.exercise.update:update_exercise
        update_resistance=adonis_lifestyle_tracker.exercise.update:update_resistance
        delete_week=adonis_lifestyle_tracker.exercise.delete:delete_week
        delete_equipment=adonis_lifestyle_tracker.exercise.delete:delete_equipment
        delete_exercise=adonis_lifestyle_tracker.exercise.delete:delete_exercise
        delete_reps=adonis_lifestyle_tracker.exercise.delete:delete_reps
        delete_resistance=adonis_lifestyle_tracker.exercise.delete:delete_resistance
    ''',
    classifiers=[
        "Programming Language :: Python :: 3.7",
        'Development Status :: 3 - Alpha',
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux"
    ],
    python_requires='~=3.7.3'
)
