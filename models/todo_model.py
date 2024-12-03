from datetime import datetime
from sqlite3 import connect, Error


class ToDo:
    def __init__(self):
        self._todo_id = None
        self._title = None
        self._description = None
        self._remind_date = None
        self._user_id = None

    def set_todo_id(self, todo_id: str):
        self._todo_id = todo_id
        return self

    def set_title(self, title: str):
        if not 4 <= len(title) <= 16:
            raise ValueError("Invalid title, the title should be should be between 4 and 16 characters")
        self._title = title
        return self

    def set_description(self, description: str):
        if not 8 < len(description) < 128:
            raise ValueError("Invalid description, the description should be should be between 8 and 128 characters")
        self._description = description
        return self

    def set_remind_date(self, remind_date: datetime):
        if remind_date < datetime.now():
            raise ValueError("Invalid remind date, the remind date should be after now")
        self._remind_date = remind_date
        return self

    def set_user_id(self, user_id: str, db_path: str):
        try:
            conn = connect(db_path)
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
            user = cursor.fetchone()

            if not user:
                raise ValueError("Invalid user ID, the user not found")
            self._user_id = user_id
            return self
        except Error as sql_lite_error:
            raise sql_lite_error

    def __str__(self):
        return f'todo_id: {self._todo_id}, todo_title: {self._title}, todo_description: {self._description} '
