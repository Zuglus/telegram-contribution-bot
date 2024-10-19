"""
test_functional_handlers.py — модуль тестирования для функциональных обработчиков.

Цель: Убедиться, что фабрика обработчиков create_message_handler корректно создает функции-обработчики.
"""

import unittest
from unittest.mock import AsyncMock, MagicMock
from telegram import Update, Message, User
from src.functional_handlers import create_message_handler

class TestFunctionalHandlers(unittest.TestCase):
    async def mock_send_message(self, text):
        self.text = text

    def setUp(self):
        # Создаем фиктивные объекты User и Message
        self.user = User(id=1, is_bot=False, first_name="TestUser")
        self.message = MagicMock(spec=Message)
        self.message.reply_text = AsyncMock()

        # Создаем фиктивный Update с сообщением
        self.update = Update(update_id=1, message=self.message)

    def test_create_message_handler(self):
        """Тестирование создания обработчика сообщений."""
        handler = create_message_handler('Привет, мир!')

        # Проверяем, что обработчик отправляет правильное сообщение
        asyncio.run(handler(self.update, None))
        self.message.reply_text.assert_called_once_with('Привет, мир!')

if __name__ == '__main__':
    unittest.main()
