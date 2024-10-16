from aiogram import Bot
from settings.bot_settings import get_bot_token

bot = Bot(token=get_bot_token())


async def notify_history_payments(user_id):
    await bot.send_message(user_id, "История взносов.")
