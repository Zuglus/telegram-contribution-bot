import psycopg2
from settings.database_settings import get_database_url

def add_history_entry(payment_id, user_id, action, timestamp):
    conn = psycopg2.connect(get_database_url())
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO payment_history (payment_id, user_id, action, timestamp) VALUES (%s, %s, %s, %s);",
        (payment_id, user_id, action, timestamp)
    )
    conn.commit()
    conn.close()

def get_history_by_payment(payment_id):
    conn = psycopg2.connect(get_database_url())
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM payment_history WHERE payment_id = %s;", (payment_id,))
    history = cursor.fetchall()
    conn.close()
    return history

def get_history_by_user(user_id):
    conn = psycopg2.connect(get_database_url())
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM payment_history WHERE user_id = %s;", (user_id,))
    history = cursor.fetchall()
    conn.close()
    return history
