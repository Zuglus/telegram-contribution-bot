from aiogram import Bot, Dispatcher, executor
from settings.bot_settings import get_bot_token
from bot_logic.commands import register_commands
from bot_logic.callback_handlers import register_callback_handlers
from event_manager.event_subscriber import register_event_handlers

bot = Bot(token=get_bot_token())
dp = Dispatcher(bot)

# Регистрируем команды и инлайн-кнопки
register_commands(dp)
register_callback_handlers(dp)

# Регистрируем подписчиков на события
register_event_handlers()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
