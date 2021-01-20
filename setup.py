from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='adonis_lifestyle_tracker',
    version='1.0.0',
    description='Tracks my Adonis Lifestyle System food and exercise data',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/esmith1412/adonis_lifestyle_tracker',
    author='Elijah Smith',
    license='GNU GPLv3',
    packages=find_packages(),
    include_package_data=True,
    entry_points='''
        [console_scripts]
        add_food=adonis_lifestyle_tracker.script.nutrition_script:add_food_script
        add_totals_to_week=adonis_lifestyle_tracker.script.nutrition_script:add_totals_to_week_script
        add_food_to_week=adonis_lifestyle_tracker.script.nutrition_script:add_food_to_week_script
        get_food=adonis_lifestyle_tracker.script.nutrition_script:get_food_script
        get_calories_left=adonis_lifestyle_tracker.script.nutrition_script:get_calories_left_script
        get_protein_left=adonis_lifestyle_tracker.script.nutrition_script:get_protein_left_script
        delete_food=adonis_lifestyle_tracker.script.nutrition_script:delete_food
        add_equipment=adonis_lifestyle_tracker.script.exercise_script:add_equipment
        add_exercise=adonis_lifestyle_tracker.script.exercise_script:add_exercise_script
        add_exercise_to_week=adonis_lifestyle_tracker.script.exercise_script:add_exercise_to_week_script
        get_equipment=adonis_lifestyle_tracker.script.exercise_script:get_equipment_script
        get_resistance=adonis_lifestyle_tracker.script.exercise_script:get_resistance_script
        change_resistance=adonis_lifestyle_tracker.script.exercise_script:change_resistance_script
    ''',
    classifiers=[
        "Programming Language :: Python :: 3.7",
        'Development Status :: 5 - Production/Stable',
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux"
    ],
    python_requires='~=3.7.3'
)
