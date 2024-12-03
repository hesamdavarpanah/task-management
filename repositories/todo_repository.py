from uuid import UUID


class ToDoRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def find_todo_by_id(self, todo_id: UUID):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT * FROM todos WHERE user_id = ?", (todo_id,))
            return cursor.fetchone()
        except Exception as exception:
            return exception.__str__()

    def create_todo(self, todo):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute(
                "INSERT INTO todos (todo_id, title, description, remind_date, user_id) VALUES (?, ?, ?, ?, ?)",
                (todo.todo_id, todo.title, todo.description, todo.remind_date, str(todo.user_id))
            )
            self.db_connection.commit()
        except Exception as exception:
            return exception.__str__()

    def update_todo(self, todo):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("UPDATE todos SET title = ?, description = ?, remind_date = ? WHERE todo_id = ?",
                           (todo.title, todo.description, todo.remind_date, str(todo.user_id)))
            self.db_connection.commit()
        except Exception as exception:
            return exception.__str__()

    def delete_todo(self, todo_id):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("DELETE FROM todos WHERE todo_id = ?", (str(todo_id),))
            self.db_connection.commit()
        except Exception as exception:
            return exception.__str__()
