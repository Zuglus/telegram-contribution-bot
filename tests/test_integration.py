import unittest
import asyncio
from unittest.mock import AsyncMock, MagicMock
from telegram import Update, User, Message
from telegram.ext import Application, ContextTypes
from src.bot import TelegramBot

class TestIntegration(unittest.TestCase):
    def setUp(self):
        # Создаем экземпляр бота
        self.bot = TelegramBot('TEST_TOKEN')

        # Создаем фиктивные объекты User и Message
        self.user = User(id=1, is_bot=False, first_name="TestUser")
        self.message = MagicMock(spec=Message)

        # Используем AsyncMock для reply_text, чтобы поддерживался await
        self.message.reply_text = AsyncMock()

        # Создаем фиктивный Update с сообщением
        self.update = Update(update_id=1, message=self.message)

        # Создаем контекст с приложением
        self.app = Application.builder().token('TEST_TOKEN').build()
        self.context = ContextTypes.DEFAULT_TYPE(application=self.app)

        # Регистрируем события
        self.bot.register_events()

    def test_start_command(self):
        """Проверка команды /start."""
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.bot.start_handler(self.update, self.context))

        # Проверяем, что обработчик вызвал reply_text с правильным сообщением
        self.message.reply_text.assert_called_once_with('Привет! Я функциональный бот.')

    def test_help_command(self):
        """Проверка команды /help."""
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.bot.help_handler(self.update, self.context))

        # Проверяем, что обработчик вызвал reply_text с правильным сообщением
        self.message.reply_text.assert_called_once_with(
            'Вот как ты можешь меня использовать:\n/start - Приветствие\n/help - Справка'
        )

if __name__ == '__main__':
    unittest.main()
