# src/bot.py

from telegram.ext import ApplicationBuilder, CommandHandler
from event_manager import EventManager
from functional_handlers import create_message_handler

class TelegramBot:
    def __init__(self, token):
        self.token = token
        self.event_manager = EventManager()
        self.app = ApplicationBuilder().token(self.token).build()

    def register_events(self):
        """Регистрация обработчиков как событий."""
        self.event_manager.subscribe('start', create_message_handler('Привет! Я функциональный бот.'))
        self.event_manager.subscribe('help', create_message_handler('Вот как ты можешь меня использовать:\n/start - Приветствие\n/help - Справка'))

    def add_handlers(self):
        """Добавляем команды и их обработчики."""
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
    # Вставьте сюда свой токен
    bot = TelegramBot('6334905594:AAHHM6ui10VxzTXWi3ugFPtjMa6oyAlH4yw')
    bot.run()
