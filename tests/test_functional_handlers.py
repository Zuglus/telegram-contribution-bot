import unittest
import asyncio
from unittest.mock import MagicMock
from telegram import Update, Message, User
from telegram.ext import ContextTypes, Application
from src.functional_handlers import create_message_handler

class TestFunctionalHandlers(unittest.TestCase):
    async def mock_send_message(self, text):
        self.text = text

    def setUp(self):
        # Создаем приложение
        self.app = Application.builder().token('TEST_TOKEN').build()
        # Создаем контекст с приложением
        self.context = ContextTypes.DEFAULT_TYPE(application=self.app)

        # Создаем фиктивные объекты User и Message
        self.user = User(id=1, is_bot=False, first_name="TestUser")
        self.message = MagicMock(spec=Message)
        self.message.reply_text = self.mock_send_message

        # Создаем фиктивный Update с имитацией сообщения
        self.update = Update(update_id=1, message=self.message)

    def test_create_message_handler(self):
        handler = create_message_handler('Hello, World!')

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(handler(self.update, self.context))
        self.assertEqual(self.text, 'Hello, World!')

if __name__ == '__main__':
    unittest.main()
