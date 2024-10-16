import psycopg2
from settings.database_settings import get_database_url

def add_user(telegram_id, username, role):
    conn = psycopg2.connect(get_database_url())
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (telegram_id, username, role) VALUES (%s, %s, %s);",
        (telegram_id, username, role)
    )
    conn.commit()
    conn.close()

def get_user_by_id(user_id):
    conn = psycopg2.connect(get_database_url())
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s;", (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

def get_user_by_telegram_id(telegram_id):
    conn = psycopg2.connect(get_database_url())
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE telegram_id = %s;", (telegram_id,))
    user = cursor.fetchone()
    conn.close()
    return user
