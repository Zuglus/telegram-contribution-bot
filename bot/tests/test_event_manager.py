import unittest
from event_manager.event_publisher import publish_event
from event_manager.event_subscriber import subscribe_event

class TestEventManager(unittest.TestCase):

    def setUp(self):
        self.events_handled = []

    def test_event_subscription(self):
        def event_handler(data):
            self.events_handled.append(data)

        subscribe_event("test_event", event_handler)
        publish_event("test_event", {"message": "hello"})
        
        # Проверяем, что обработчик сработал и записал событие
        self.assertEqual(len(self.events_handled), 1)
        self.assertEqual(self.events_handled[0]['message'], "hello")

if __name__ == '__main__':
    unittest.main()
