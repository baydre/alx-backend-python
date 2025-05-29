import sqlite3
import functools

def with_db_connection(func):
    """
    Decorator that provides a SQLite database connection to the decorated function.
    The connection is automatically closed after the function executes.

    Args:
        func (callable): The function to decorate.

    Returns:
        callable: The wrapped function with a database connection as the first argument.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            result = func(conn, *args, **kwargs)
            return result
        finally:
            conn.close()
    return wrapper

@with_db_connection
def get_user_by_id(conn, user_id):
    """
    Fetch a user from the database by their ID.

    Args:
        conn (sqlite3.Connection): The database connection.
        user_id (int): The ID of the user to fetch.

    Returns:
        tuple or None: The user record as a tuple, or None if not found.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

# Test run
user = get_user_by_id(user_id=1)
print(user)