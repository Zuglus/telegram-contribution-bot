from aiogram import Bot
from notifier.history_notifier import notify_history_payments
from settings.bot_settings import get_bot_token

bot = Bot(token=get_bot_token())

# Обработчик события просмотра истории
async def handle_view_history(event_data):
    user_id = event_data.get("user_id")
    await notify_history_payments(user_id)
    # Логика получения истории взносов...
