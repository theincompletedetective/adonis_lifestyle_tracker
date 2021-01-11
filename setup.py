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
        get_food=adonis_lifestyle_tracker.nutrition.nutrition:get_food
        add_week=adonis_lifestyle_tracker.nutrition.nutrition:add_week
        add_food_to_week=adonis_lifestyle_tracker.nutrition.nutrition:add_food_to_week
        get_weekly_calories=adonis_lifestyle_tracker.nutrition.nutrition:get_weekly_kcal
        get_weekly_protein=adonis_lifestyle_tracker.nutrition.nutrition:get_weekly_protein
    ''',
    classifiers=[
        "Programming Language :: Python :: 3.7",
        'Development Status :: 3 - Alpha',
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux"
    ],
    python_requires='~=3.7.3'
)
