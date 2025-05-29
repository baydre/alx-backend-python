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

def transactional(func):
    """
    Decorator that wraps a function in a database transaction.
    Commits the transaction if the function succeeds, rolls back if an exception occurs.

    Args:
        func (callable): The function to decorate.

    Returns:
        callable: The wrapped transactional function.
    """
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()
            print("[LOG] Transaction committed.")
            return result
        except Exception as e:
            conn.rollback()
            print("[LOG] Transaction rolled back due to error:", e)
            raise
    return wrapper

@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    """
    Update a user's email address in the database.

    Args:
        conn (sqlite3.Connection): The database connection.
        user_id (int): The ID of the user to update.
        new_email (str): The new email address.

    Returns:
        None
    """
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))

# Test run
update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')