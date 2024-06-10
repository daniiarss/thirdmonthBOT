import aiosqlite

def add_user(user_id, username, first_name, last_name):
    connection = aiosqlite.connect('bot.db')
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO users (user_id, username, first_name, last_name)
        VALUES (?, ?, ?, ?)
    ''', (user_id, username, first_name, last_name))
    connection.commit()
    connection.close()

def user_exists(user_id):
    connection = aiosqlite.connect('bot.db')
    cursor = connection.cursor()
    cursor.execute('SELECT 1 FROM users WHERE user_id = ?', (user_id,))
    exists = cursor.fetchone() is not None
    connection.close()
    return exists
