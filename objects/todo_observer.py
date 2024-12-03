from objects.observer import Observer


class TodoObserver(Observer):
    def update(self, message):
        print(f"Notification: {message}")
