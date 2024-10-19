# tests/test_event_manager.py

import unittest
import asyncio
from src.event_manager import EventManager

class TestEventManager(unittest.TestCase):
    def setUp(self):
        self.event_manager = EventManager()
        self.event_triggered = False

    async def sample_handler(self, *args, **kwargs):
        self.event_triggered = True

    def test_event_subscription_and_publish(self):
        self.event_manager.subscribe('test_event', self.sample_handler)
        loop = asyncio.new_event_loop()  # Исправляем создание цикла событий
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.event_manager.publish('test_event'))
        self.assertTrue(self.event_triggered)

if __name__ == '__main__':
    unittest.main()
