import logging

logging.basicConfig(filename='payment_log.log', level=logging.INFO)

def log_payment_creation(user_id, payment_id):
    logging.info(f"Создан новый взнос. Пользователь: {user_id}, Взнос: {payment_id}")

def log_payment_confirmation(user_id, payment_id):
    logging.info(f"Подтвержден взнос. Пользователь: {user_id}, Взнос: {payment_id}")

def log_payment_rejection(user_id, payment_id):
    logging.info(f"Отклонен взнос. Пользователь: {user_id}, Взнос: {payment_id}")
