import sqlite3
import functools
from datetime import datetime

def log_queries(func):
    """
    Decorator that logs the date, time, and SQL query being executed.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The wrapped function with logging.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query') or (args[0] if args else None)
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if query:
            print(f"[{now}] [LOG] Executing SQL Query: {query}")
        else:
            print(f"[{now}] [LOG] No SQL query provided.")
        return func(*args, **kwargs)
    return wrapper

@log_queries
def fetch_all_users(query):
    """
    Fetch all users from the database using the provided SQL query.

    Args:
        query (str): The SQL query to execute.

    Returns:
        list: List of tuples containing the query results.
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Test run
users = fetch_all_users(query="SELECT * FROM users")
print(users)