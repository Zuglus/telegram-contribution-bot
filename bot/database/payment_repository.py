import psycopg2
from settings.database_settings import get_database_url

def add_payment(user_id, amount, month, year):
    conn = psycopg2.connect(get_database_url())
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO payments (user_id, amount, month, year) VALUES (%s, %s, %s, %s) RETURNING id;",
        (user_id, amount, month, year)
    )
    payment_id = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    return payment_id

def get_payments_by_user(user_id):
    conn = psycopg2.connect(get_database_url())
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM payments WHERE user_id = %s;", (user_id,))
    payments = cursor.fetchall()
    conn.close()
    return payments

def get_payment_by_id(payment_id):
    conn = psycopg2.connect(get_database_url())
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM payments WHERE id = %s;", (payment_id,))
    payment = cursor.fetchone()
    conn.close()
    return payment
