from objects.observable import Observable


class TodoList(Observable):
    def __init__(self):
        super().__init__()
        self.todos = []

    def add_todo(self, todo):
        self.todos.append(todo)
        self.notify_observers(f"Added TODO: {todo}")

    def remove_todo(self, todo):
        if todo in self.todos:
            self.todos.remove(todo)
            self.notify_observers(f"Removed TODO: {todo}")
        else:
            print("TODO not found!")

    def __str__(self):
        return "\n".join(self.todos)
