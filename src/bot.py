import os
from dotenv import load_dotenv

load_dotenv()

from telegram.ext import ApplicationBuilder, CommandHandler
from src.event_manager import EventManager
from src.functional_handlers import create_message_handler

class TelegramBot:
    def __init__(self):
        self.token = os.getenv("TELEGRAM_TOKEN")
        if not self.token:
            raise ValueError("TELEGRAM_TOKEN не найден в переменных окружения")

        self.event_manager = EventManager()
        self.app = ApplicationBuilder().token(self.token).build()

    def register_events(self):
        """Регистрация событий."""
        self.event_manager.subscribe('start', create_message_handler('Привет! Я бот.'))
        self.event_manager.subscribe('help', create_message_handler('Помощь: /start /help'))

    def add_handlers(self):
        """Добавление обработчиков команд."""
        self.app.add_handler(CommandHandler('start', self.start_handler))
        self.app.add_handler(CommandHandler('help', self.help_handler))

    async def start_handler(self, update, context):
        await self.event_manager.publish('start', update, context)

    async def help_handler(self, update, context):
        await self.event_manager.publish('help', update, context)

    def run(self):
        """Запуск бота."""
        self.register_events()
        self.add_handlers()
        self.app.run_polling()

if __name__ == '__main__':
    bot = TelegramBot()
    bot.run()
