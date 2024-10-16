from aiogram import Bot
from settings.bot_settings import get_bot_token

bot = Bot(token=get_bot_token())

async def notify_payment_start(user_id):
    await bot.send_message(user_id, "Процесс создания взноса начат.")

async def notify_payment_creation(user_id, amount, month, year):
    await bot.send_message(user_id, f"Ваш взнос на сумму {amount} руб. за {month}/{year} был создан.")

async def notify_payment_confirmation(user_id, payment_id):
    await bot.send_message(user_id, f"Ваш взнос с ID {payment_id} был подтвержден.")

async def notify_payment_rejection(user_id, payment_id):
    await bot.send_message(user_id, f"Ваш взнос с ID {payment_id} был отклонен.")
