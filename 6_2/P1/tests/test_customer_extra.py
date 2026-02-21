import unittest
from source.customer import Customer


class TestCustomerExtra(unittest.TestCase):
    def setUp(self):
        self.customer = Customer(customer_id=1, name="Alice", email="alice@example.com")

    def test_modify_customer(self):
        self.customer.name = "Bob"
        self.customer.email = "bob@example.com"
        self.assertEqual(self.customer.name, "Bob")
        self.assertEqual(self.customer.email, "bob@example.com")

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            self.customer.email = "invalid_email"

    def test_delete_nonexistent_customer(self):
        # Simula intento de eliminar un cliente que no existe
        result = self.customer.delete_customer("nonexistent_id")
        self.assertFalse(result)

    def test_display(self):
        display_str = self.customer.display()
        self.assertIn("Alice", display_str)


if __name__ == "__main__":
    unittest.main()
    