import sqlite3
from database.sql_queries import INSERT_USER_TABLE

def add_user(user_id, username, first_name, last_name):
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()
    cursor.execute(INSERT_USER_TABLE, (None, user_id, username, first_name, last_name))
    connection.commit()
    connection.close()

def user_exists(user_id):
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()
    cursor.execute('''SELECT FIRST_NAME FROM telegram_users WHERE TELEGRAM_ID = ?''', (user_id,))
    exists = cursor.fetchone() is not None
    connection.close()
    return exists
