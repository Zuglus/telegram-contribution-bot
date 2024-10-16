from aiogram import Bot
from settings.bot_settings import get_bot_token
from keyboard.main_menu_keyboard import main_menu_keyboard

bot = Bot(token=get_bot_token())

# Обработчик события для команды /start
async def handle_start_command(event_data):
    user_id = event_data.get("user_id")
    keyboard = main_menu_keyboard()
    await bot.send_message(user_id, "Начальное меню.", reply_markup=keyboard)
