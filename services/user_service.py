from repositories.user_repository import UserRepository


class UserService:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self._user_repo = UserRepository(self.db_connection)

    def create_user_table(self):
        cursor = self.db_connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id TEXT PRIMARY KEY,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                firstname TEXT NOT NULL,
                lastname TEXT NOT NULL,
                address TEXT NOT NULL,
                phone_number TEXT NOT NULL
            )
        """)
        self.db_connection.commit()

    def find_user_by_username(self, username):
        return self._user_repo.find_by_username(username)

    def create_user(self, user) -> None | str:
        try:
            self._user_repo.create_user(user)
            print(f"the {user.user_id} user has been saved successfully")
        except Exception as exception:
            return exception.__str__()
