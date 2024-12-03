from uuid import uuid4


class User:
    def __init__(self, username: str, password: str, firstname: str, lastname: str, address: str, phone_number: str,
                 user_id=None):
        self.user_id = user_id or str(uuid4())
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.phone_number = phone_number

    def __str__(self):
        return (f"User(user_id={self.user_id}, username={self.username}, "
                f"firstname={self.firstname}, lastname={self.lastname}, "
                f"address={self.address}, phone_number={self.phone_number})")


class UserBuilder:
    def __init__(self):
        self._user_id = None
        self._username = None
        self._password = None
        self._firstname = None
        self._lastname = None
        self._address = None
        self._phone_number = None

    def set_user_id(self, user_id):
        if user_id and not isinstance(user_id, str):
            raise ValueError("Invalid ID type, the ID should be string")
        self._user_id = user_id
        return self

    def set_username(self, username):
        if not 3 < len(username) <= 64:
            raise ValueError("Invalid username, the username should be between 4 and 64 characters")
        self._username = username
        return self

    def set_password(self, password):
        if not 3 < len(password):
            raise ValueError("Invalid password, the password should be more than 4 characters")
        self._password = password
        return self

    def set_firstname(self, firstname):
        if not 3 < len(firstname) <= 64:
            raise ValueError("Invalid firstname, the firstname should be between 4 and 64 characters")
        self._firstname = firstname
        return self

    def set_lastname(self, lastname):
        if not 2 < len(lastname) <= 64:
            raise ValueError("Invalid lastname, the lastname should be between 4 and 64 characters")
        self._lastname = lastname
        return self

    def set_address(self, address):
        if not 16 < len(address) <= 256:
            raise ValueError("Invalid address, the address should be between 16 and 256 characters")
        self._address = address
        return self

    def set_phone_number(self, phone_number):
        if not len(phone_number) == 11 or not phone_number.startswith('09'):
            raise ValueError("Invalid phone number, the phone number should be 11 digits starting with '09'")
        self._phone_number = phone_number
        return self

    def build(self):
        if not all(
                [self._username, self._password, self._firstname, self._lastname, self._address, self._phone_number]):
            raise ValueError("All fields must be set before building the User object")

        return User(
            username=self._username,
            password=self._password,
            firstname=self._firstname,
            lastname=self._lastname,
            address=self._address,
            phone_number=self._phone_number,
            user_id=self._user_id
        )
