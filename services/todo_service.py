from xml.dom import NotFoundErr

from objects.todo_observable import TodoList
from objects.todo_observer import TodoObserver
from repositories.todo_repository import ToDoRepository


class ToDoService:
    def __init__(self, db_connection, username: str):
        self.db_connection = db_connection
        self._todo_repository = ToDoRepository(self.db_connection)
        self._cursor = self.db_connection.cursor()
        self._cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        self._user = self._cursor.fetchone()
        if not self._user:
            raise NotFoundErr("user not found")
        self._todo_list = TodoList()
        self.observer_todo = TodoObserver()

    def create_todo_table(self):
        cursor = self.db_connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS todos (
                todo_id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                remind_date DATETIME NOT NULL,
                user_id TEXT NOT NULL
            )
        """)
        self.db_connection.commit()

    def find_todo(self, todo_id):
        try:
            return self._todo_repository.find_todo_by_id(todo_id)
        except Exception as exception:
            return exception.__str__()

    def create_todo(self, todo) -> None | str:
        try:
            self._todo_list.add_observer(self.observer_todo)
            self._todo_repository.create_todo(todo)
            self._todo_list.add_todo(str(todo.todo_id))
            print(f"the {todo.todo_id} todo has been saved")
        except Exception as exception:
            return exception.__str__()

    def update_todo(self, todo) -> None | str:
        try:
            self._todo_repository.update_todo(todo)
            self._todo_list.remove_todo(str(todo.todo_id))
            self._todo_list.add_todo(str(todo.todo_id))
            print(f"the {todo.todo_id} todo has been updated")
        except Exception as exception:
            return exception.__str__()

    def delete_todo(self, todo_id) -> None | str:
        try:
            self._todo_list.add_observer(self.observer_todo)
            self._todo_list.remove_todo(todo_id)
            self._todo_repository.delete_todo(todo_id)
            print(f"the {todo_id} todo has been deleted")
        except Exception as exception:
            return exception.__str__()
