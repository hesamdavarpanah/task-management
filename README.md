# Python Task Management Program

![This Program could manage users and tasks.](./algorithm.png "Python Task Management Program")
### Description

This program consists of two separate tasks implemented in different files. Each task performs a specific functionality:

1. **Task 1-1: TwoSum Algorithm**
2. **Task 1-2: User and ToDo Management**

---

### Task 1-1: TwoSum Algorithm

#### Overview:

The `TwoSum` algorithm is a classic programming problem where the goal is to find two numbers in an array whose sum equals a given target. This algorithm is implemented in the file `task_1_1.py` and uses a class called `TwoSum`.

#### Execution Code:

```python
from two_sum import TwoSum

if __name__ == '__main__':
    print("Task 1-1:\n")
    summ = TwoSum([2, 7, 11, 15], 9)
    print(summ.summary)
```

#### Time Complexity Analysis:

- **Worst Case (O(n))**: When the algorithm needs to check all elements in the array (e.g., if no pair is found or the pair is at the end of the array).
- **Best Case (O(1))**: When the first pair of numbers is found at the beginning of the array.

---

### Task 1-2: User and ToDo Management

#### Overview:

This task is a user and task (ToDo) management program designed using SQLite for data storage. The program includes the following features:

1. **Create a new user**
2. **Create a ToDo for a user**
3. **Edit a ToDo**
4. **Delete a ToDo**
5. **View ToDos**

#### File Structure:

- **`models/user_model.py`**: Contains the `User` model and the `UserBuilder` class for managing user data.
- **`models/todo_model.py`**: Contains the `ToDo` model for managing task data.
- **`services/user_service.py`**: Service for managing users (creating tables, adding users, etc.).
- **`services/todo_service.py`**: Service for managing tasks (creating, updating, deleting, and viewing tasks).

#### Execution Code:

```python
import sqlite3
from datetime import datetime, timedelta

from models.todo_model import ToDo
from models.user_model import UserBuilder
from services.todo_service import ToDoService
from services.user_service import UserService

if __name__ == '__main__':
    # create database
    db_connection = sqlite3.connect('todo.db')

    # create users table
    user_service = UserService(db_connection)
    user_service.create_user_table()

    # create user
    user_builder = UserBuilder()
    user = (user_builder
            .set_user_id("1")
            .set_username("john_doe")
            .set_password("SecurePas$1")
            .set_firstname("John")
            .set_lastname("Doe")
            .set_address("Iran, Tehran, Tehran, Tehran,Tehran,Tehran,Tehran,")
            .set_phone_number("09123456789")
            .build())

    user_service.create_user(user)

    # create a task for user 1
    todo_service = ToDoService(db_connection, "john_doe")
    todo_model = ToDo()
    nine_hours = datetime.now() + timedelta(hours=9)
    todo = (todo_model.set_todo_id("1").set_title("task_1").set_description("this_is_test").set_remind_date(
        nine_hours).set_user_id("1", "todo.db"))
    todo_service.create_todo(todo)

    # to update task uncomment below
    # new_todo = (todo_model.set_todo_id("1").set_title("task_2").set_description("this_is_test2").set_remind_date(
    #     nine_hours).set_user_id("1", "todo.db"))
    # todo_service.update_todo(new_todo)

    # to delete task uncomment below
    # todo_service.delete_todo("1")
```

#### Features:

1. **Create User:**
   - A new user is created using the `UserBuilder` class.
   - User information is stored in the `users` table in the SQLite database.

2. **Create ToDo:**
   - New tasks (ToDo) can be created for users.
   - ToDo information is stored in the `todos` table in the SQLite database.

3. **Edit ToDo:**
   - By changing the `title` or `description` of a ToDo and calling the `update_todo` method, the task is updated.

4. **Delete ToDo:**
   - By calling the `delete_todo` method, a task is removed from the database.

#### Notes:

- **Database Path**: The SQLite database file is created with the name `todo.db`.
- **Date and Time Format**: Tasks (ToDo) include a reminder date (`remind_date`) which must be in the future.

---

### Installation and Execution

1. **Prerequisites:**
   - Python 3.8 or higher
   - SQLite (built-in with Python)

2. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

3. **Install Dependencies (if any):**
   - This program does not require external libraries, but if additional libraries are added, you can install them using:
     ```bash
     pip install -r requirements.txt
     ```

4. **Run the Program:**
   - To execute Task 1-1:
     ```bash
     python task_1_1.py
     ```
   - To execute Task 1-2:
     ```bash
     python task_1_2.py
     ```

---

### Database Structure

#### `users` Table:

| Column          | Type      | Description                  |
|------------------|-----------|------------------------------|
| `user_id`        | TEXT      | Unique identifier for users  |
| `username`       | TEXT      | Username                    |
| `password`       | TEXT      | Password                    |
| `firstname`      | TEXT      | First name                  |
| `lastname`       | TEXT      | Last name                   |
| `address`        | TEXT      | Address                     |
| `phone_number`   | TEXT      | Phone number                |

#### `todos` Table:

| Column          | Type      | Description                  |
|------------------|-----------|------------------------------|
| `todo_id`        | TEXT      | Unique identifier for tasks  |
| `title`          | TEXT      | Task title                  |
| `description`    | TEXT      | Task description            |
| `remind_date`    | DATETIME  | Reminder date               |
| `user_id`        | TEXT      | User ID associated with task |

---

### Program Analysis

- **Task 1-1**:
  - The TwoSum algorithm is implemented with high efficiency and has a time complexity of `O(n)` in the worst case.

- **Task 1-2**:
  - A user and task management system is implemented with features to add, edit, delete, and view tasks.
  - SQLite is used for data storage.
  - Builder Pattern, Repository Pattern and Observer/Observable Pattern implemented.
  - The program architecture includes models, services, and database handling, ensuring separation of concerns.

---

### Author

This program was designed and implemented by **HesamDavarpanah**.

---