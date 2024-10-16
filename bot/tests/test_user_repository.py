import unittest
from database.user_repository import add_user, get_user_by_id, get_user_by_telegram_id

class TestUserRepository(unittest.TestCase):

    def test_add_user(self):
        user_id = add_user(123456789, 'testuser', 'user')
        self.assertIsNotNone(user_id)

    def test_get_user_by_id(self):
        add_user(987654321, 'anotheruser', 'admin')
        user = get_user_by_id(1)  # предполагается, что это ID первого пользователя
        self.assertEqual(user[1], 'testuser')

    def test_get_user_by_telegram_id(self):
        add_user(111222333, 'telegramuser', 'user')
        user = get_user_by_telegram_id(111222333)
        self.assertEqual(user[1], 'telegramuser')

if __name__ == '__main__':
    unittest.main()
