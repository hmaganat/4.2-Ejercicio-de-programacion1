import unittest
from source.customer import Customer


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer(
            customer_id="C001",
            name="Alice",
            email="alice@test.com",
            phone="1234567890"
        )

    def test_update_information(self):
        self.customer.update_information(name="Bob")
        self.assertEqual(self.customer.name, "Bob")

    def test_to_dict(self):
        data = self.customer.to_dict()
        self.assertEqual(data["email"], "alice@test.com")

    def test_from_dict(self):
        data = {
            "customer_id": "C002",
            "name": "Charlie",
            "email": "charlie@test.com",
            "phone": "0987654321"
        }
        customer = Customer.from_dict(data)
        self.assertEqual(customer.name, "Charlie")


if __name__ == "__main__":
    unittest.main()