import sqlite3
import functools

query_cache = {}

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            result = func(conn, *args, **kwargs)
            return result
        finally:
            conn.close()
    return wrapper

def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn, query, *args, **kwargs):
        if query in query_cache:
            print("[LOG] Returning cached result for query.")
            return query_cache[query]
        result = func(conn, query, *args, **kwargs)
        query_cache[query] = result
        print("[LOG] Caching result for query.")
        return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# Test run
users = fetch_users_with_cache(query="SELECT * FROM users")
users_again = fetch_users_with_cache(query="SELECT * FROM users")