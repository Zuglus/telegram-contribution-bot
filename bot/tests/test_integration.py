import unittest
from database.user_repository import add_user
from database.payment_repository import add_payment, get_payments_by_user
from event_manager.event_publisher import publish_event
from event_manager.event_subscriber import subscribe_event

class TestIntegration(unittest.TestCase):

    def test_user_payment_integration(self):
        # Добавляем пользователя
        user_id = add_user(123456789, 'integrationuser', 'user')

        # Добавляем взнос для этого пользователя
        payment_id = add_payment(user_id, 1000, 10, 2024)

        # Проверяем, что взнос добавлен
        payments = get_payments_by_user(user_id)
        self.assertGreater(len(payments), 0)

    def test_event_integration(self):
        events_handled = []

        def event_handler(data):
            events_handled.append(data)

        subscribe_event("payment_created", event_handler)
        
        # Публикуем событие создания взноса
        publish_event("payment_created", {"user_id": 1, "payment_id": 100})

        # Проверяем, что событие обработано
        self.assertEqual(len(events_handled), 1)
        self.assertEqual(events_handled[0]['payment_id'], 100)

if __name__ == '__main__':
    unittest.main()
