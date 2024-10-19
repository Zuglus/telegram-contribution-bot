"""
bot.py — основной модуль Telegram-бота.

Цель: Обеспечить реактивную и событийно-ориентированную архитектуру
для простого расширения и взаимодействия между компонентами.
"""

import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler
from src.event_manager import EventManager
from src.functional_handlers import create_message_handler

# Загружаем переменные окружения из .env
load_dotenv()

class TelegramBot:
    """Класс Telegram-бота с событийной архитектурой."""

    def __init__(self):
        """Инициализация бота и настройка приложения."""
        self.token = os.getenv("TELEGRAM_TOKEN")  # Загружаем токен из .env
        if not self.token:
            raise ValueError("TELEGRAM_TOKEN не найден в переменных окружения")

        self.event_manager = EventManager()  # Создаем менеджер событий
        self.app = ApplicationBuilder().token(self.token).build()  # Инициализация приложения

    def register_events(self):
        """Регистрация событий и привязка к обработчикам."""
        self.event_manager.subscribe('start', create_message_handler('Привет! Я бот.'))
        self.event_manager.subscribe('help', create_message_handler('Помощь: /start /help'))

    def add_handlers(self):
        """Добавление обработчиков команд."""
        self.app.add_handler(CommandHandler('start', self.start_handler))
        self.app.add_handler(CommandHandler('help', self.help_handler))

    async def start_handler(self, update, context):
        """Обработчик команды /start."""
        await self.event_manager.publish('start', update, context)

    async def help_handler(self, update, context):
        """Обработчик команды /help."""
        await self.event_manager.publish('help', update, context)

    def run(self):
        """Запуск бота с регистрацией событий и обработчиков."""
        self.register_events()
        self.add_handlers()
        self.app.run_polling()  # Запуск процесса опроса Telegram

if __name__ == '__main__':
    # Создаем экземпляр Telegram-бота и запускаем его
    bot = TelegramBot()
    bot.run()
