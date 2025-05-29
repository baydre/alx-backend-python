# Python Decorators for Database Operations

This project focuses on mastering Python decorators to enhance database operations in Python applications. It includes decorators for logging queries, handling connections, managing transactions, retrying failed operations, and caching query results.

## Project Structure

```
python-decorators-0x01/
├── 0-log_queries.py
├── 1-with_db_connection.py
├── 2-transactional.py
├── 3-retry_on_failure.py
└── 4-cache_query.py
```

## Tasks

### 0. Logging Database Queries

- **File**: `0-log_queries.py`
- **Description**: Logs SQL queries executed by any function using a decorator.

### 1. Handle Database Connections with a Decorator

- **File**: `1-with_db_connection.py`
- **Description**: Automates database connection handling by opening and closing connections via a decorator.

### 2. Transaction Management Decorator

- **File**: `2-transactional.py`
- **Description**: Ensures database transactions are committed or rolled back based on function success or failure.

### 3. Retry Database Queries

- **File**: `3-retry_on_failure.py`
- **Description**: Retries database operations a set number of times if they fail due to transient errors.

### 4. Cache Database Queries

- **File**: `4-cache_query.py`
- **Description**: Caches query results based on the SQL query string to avoid redundant calls.

## Requirements

- Python 3.8 or higher
- SQLite3 database with a `users` table for testing
- Git & GitHub for version control

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/alx-backend-python.git
   cd alx-backend-python/python-decorators-0x01

2. Run the scripts:
    ```python
    python3 0-log_queries.py

### Author

[Yasir Musa](https://github.com/baydre) | ALX Pro-Dev Backend Track

---
