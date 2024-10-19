import unittest
from src.bot import TelegramBot

class TestTelegramBot(unittest.TestCase):
    def setUp(self):
        self.bot = TelegramBot('TEST_TOKEN')

    def test_event_registration(self):
        self.bot.register_events()
        self.assertIn('start', self.bot.event_manager._subscribers)
        self.assertIn('help', self.bot.event_manager._subscribers)

if __name__ == '__main__':
    unittest.main()
