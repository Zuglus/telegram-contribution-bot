from aiogram import Bot
from settings.bot_settings import get_bot_token

bot = Bot(token=get_bot_token())

async def notify_user_registration(user_id):
    await bot.send_message(user_id, "Вы успешно зарегистрированы в системе.")

async def notify_user_login(user_id):
    await bot.send_message(user_id, "Вы вошли в систему.")
