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

