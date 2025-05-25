
## 🌀 Python Generators Project

Welcome to the **Python Generators** project!
This repository demonstrates the practical use of Python generators for efficient data streaming, batch processing, and lazy pagination in a **MySQL database** environment.

---

### 🚀 Project Features

✅ **Database Setup & Seeding**

✅ **Data Streaming with Generators**

✅ **Batch Processing**

✅ **Lazy Loading Pagination**

---

### 📂 Project Structure

```
.
├── seed.py                # Create database, tables, and seed data
├── 0-stream_users.py      # Stream user data row by row
├── 1-batch_processing.py  # Process user data in batches
├── 2-lazy_paginate.py     # Implement lazy loading pagination
├── user_data.csv          # CSV file for seeding database
├── 0-main.py              # Test script for streaming users
├── 1-main.py              # Test script for batch processing
├── 2-main.py              # Test script for lazy pagination
├── 3-main.py              # Additional test for lazy pagination
└── README.md              # Project documentation
```

---

### 📊 Requirements

* **Python 3.x**
* **MySQL Server**
* Python Libraries:

  * `mysql-connector-python`
  * `csv`
  * `uuid`

Install dependencies with:

```bash
pip install mysql-connector-python
```

---

### 🛠️ Setup Instructions

1️⃣ **Clone the Repository**

```bash
git clone https://github.com/YOUR_USERNAME/alx-backend-python.git
cd python-generators-0x00
```

2️⃣ **Prepare the Database**

* Update `seed.py` with your MySQL credentials:

```python
connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password"
)
```

* Run `0-main.py` to create the database, table, and seed data.

```bash
python3 0-main.py
```

---

### 🌀 Project Scripts Overview

| File                    | Description                           | How to Run          |
| ----------------------- | ------------------------------------- | ------------------- |
| `0-stream_users.py`     | Stream all user data row by row       | `python3 1-main.py` |
| `1-batch_processing.py` | Process user data in batches          | `python3 2-main.py` |
| `2-lazy_paginate.py`    | Load user data lazily with pagination | `python3 3-main.py` |
| `seed.py`               | Setup database and seed data from CSV | `python3 0-main.py` |

---

### 📊 Example Outputs

#### Streaming Users:

```bash
{'user_id': '...', 'name': 'John Doe', 'email': 'john@example.com', 'age': 30}
{'user_id': '...', 'name': 'Jane Doe', 'email': 'jane@example.com', 'age': 25}
...
```

#### Batch Processing:

```bash
{'user_id': '...', 'name': 'John Doe', 'email': 'john@example.com', 'age': 30}
{'user_id': '...', 'name': 'Alice', 'email': 'alice@example.com', 'age': 45}
...
```

#### Lazy Pagination:

```bash
Page 1:
{'user_id': '...', 'name': 'John Doe', ...}
...
```

---

### 🌟 Author

👨‍💻 [Yasir Musa](https://github.com/baydre) | ALX Pro-Dev Backend Track

---
