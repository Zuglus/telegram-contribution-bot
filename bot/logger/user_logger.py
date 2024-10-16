import logging

logging.basicConfig(filename='user_log.log', level=logging.INFO)

def log_user_registration(telegram_id, username):
    logging.info(f"Зарегистрирован новый пользователь. Telegram ID: {telegram_id}, Username: {username}")

def log_user_login(telegram_id, username):
    logging.info(f"Пользователь вошел в систему. Telegram ID: {telegram_id}, Username: {username}")
