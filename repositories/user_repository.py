class UserRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def find_by_id(self, user_id: str):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
            return cursor.fetchone()
        except Exception as exception:
            return exception.__str__()

    def find_by_username(self, username: str):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
            return cursor.fetchone()
        except Exception as exception:
            return exception.__str__()

    def create_user(self, user):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute(
                "INSERT INTO users (user_id, username, password, firstname, lastname, address, phone_number) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (user.user_id, user.username, user.password, user.firstname, user.lastname, user.address,
                 user.phone_number)
            )
            self.db_connection.commit()
        except Exception as exception:
            return exception.__str__()
