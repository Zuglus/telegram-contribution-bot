from aiogram import Bot
from notifier.payment_notifier import notify_payment_start
from settings.bot_settings import get_bot_token

bot = Bot(token=get_bot_token())

# Обработчик события создания взноса
async def handle_create_payment(event_data):
    user_id = event_data.get("user_id")
    await notify_payment_start(user_id)
    # Логика создания взноса...
