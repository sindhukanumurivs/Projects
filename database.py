import logging
import sqlite3
logging.basicConfig(level=logging.DEBUG)
def create_connection():
    conn = sqlite3.connect('user_data.db')
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_info (
            user_id INTEGER,
            age INTEGER,
            height REAL,
            weight REAL,
            gender TEXT,
            activity TEXT,
            weight_loss_option TEXT,
            meals_calories_perc TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    conn.commit()
    conn.close()
def get_all_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return users

def add_user(username, password):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    logging.debug(f"Added user {username} with password {password}")
    conn.close()

def get_user(username, password):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    conn.close()
    return user

def add_user_info(user_id, age, height, weight, gender, activity, weight_loss_option, meals_calories_perc):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO user_info (user_id, age, height, weight, gender, activity, weight_loss_option, meals_calories_perc)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (user_id, age, height, weight, gender, activity, weight_loss_option, meals_calories_perc))
    conn.commit()
    logging.debug(f"Added user info for user_id {user_id}")
    conn.close()

def get_user_info(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM user_info WHERE user_id = ?', (user_id,))
    user_info = cursor.fetchone()
    conn.close()
    return user_info

# Run this to create the tables
create_table()
