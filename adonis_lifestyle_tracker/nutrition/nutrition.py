import sqlite3

# To connect to nutrition database
conn = sqlite3.connect('nutrition.db')

# To update/modify the database
cursor = conn.cursor()


def add_food(name, kcal, protein):
    cursor.execute(
        f'''
        INSERT INTO food (food_name, kcal, protein)
            VALUES ({name}, {kcal}, {protein});
        '''
    )


def add_week(total_kcal, total_protein):
    cursor.execute(
        f'''
        INSERT INTO week (total_kcal, total_protein)
            VALUES ({total_kcal}, {total_protein});
        '''
    )


def add_food_to_week(food_id, week_id):
    cursor.execute(
        f'''
        INSERT INTO food_week (food_id, week_id)
            VALUES ({food_id}, {week_id});
        '''
    )


# To commit any changes
conn.commit()

# To close the connection
conn.close()
