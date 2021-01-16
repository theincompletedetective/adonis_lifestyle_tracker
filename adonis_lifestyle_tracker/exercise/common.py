'''Contains the functions used by all modules in the exercise package.'''


def check_value(cursor, table, value=None):
    '''
    Checks to see whether or not the provided value is in the specified database table.
    '''
    if value:
        return cursor.execute(
            'SELECT * FROM ? WHERE id = ?', (table, value)
        ).fetchone()
    else:
        return cursor.execute(
            'SELECT * FROM ? WHERE id = ?', (table, table)
        ).fetchone()
