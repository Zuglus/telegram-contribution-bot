import unittest
from database.payment_repository import add_payment, get_payments_by_user, get_payment_by_id

class TestPaymentRepository(unittest.TestCase):

    def test_add_payment(self):
        payment_id = add_payment(1, 1000, 10, 2024)
        self.assertIsNotNone(payment_id)

    def test_get_payments_by_user(self):
        add_payment(1, 1000, 10, 2024)
        payments = get_payments_by_user(1)
        self.assertGreater(len(payments), 0)

    def test_get_payment_by_id(self):
        payment_id = add_payment(2, 500, 11, 2024)
        payment = get_payment_by_id(payment_id)
        self.assertEqual(payment[2], 500)

if __name__ == '__main__':
    unittest.main()
