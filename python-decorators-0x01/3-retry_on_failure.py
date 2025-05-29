import time
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

def retry_on_failure(retries=3, delay=2):
    """
    Decorator factory that retries a function if it raises an exception.

    Args:
        retries (int): Number of retry attempts.
        delay (int): Delay in seconds between retries.

    Returns:
        callable: The decorator.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"[LOG] Attempt {attempts} failed with error: {e}. Retrying...")
                    time.sleep(delay)
            print(f"[LOG] All {retries} attempts failed.")
            raise Exception(f"Operation failed after {retries} retries.")
        return wrapper
    return decorator

@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    """
    Fetch all users from the database, retrying on failure.

    Args:
        conn (sqlite3.Connection): The database connection.

    Returns:
        list: List of tuples containing user records.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

# Test run
users = fetch_users_with_retry()
print(users)