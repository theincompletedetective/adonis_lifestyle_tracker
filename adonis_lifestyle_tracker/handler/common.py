import sqlite3


def get_sorted_tuple(db_path, column, table):
    db = sqlite3.connect(db_path)
    cursor = db.cursor()
    cursor.execute(f'SELECT {column} FROM {table}')

    elements_tuple = tuple(sorted({elem[0] for elem in cursor.fetchall()}))

    db.close()
    return elements_tuple
