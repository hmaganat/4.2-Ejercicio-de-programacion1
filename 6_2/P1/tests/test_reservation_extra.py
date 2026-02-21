import unittest
from source.reservation import Reservation
from source.hotel import Hotel
from source.customer import Customer


class TestReservationExtra(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel(hotel_id=1, name="Hilton", location="NY", total_rooms=5)
        self.customer = Customer(customer_id=1, name="Alice", email="alice@example.com")
        self.reservation = Reservation(self.customer, self.hotel, "2026-02-21")

    def test_cancel_reservation_success(self):
        self.reservation.cancel()
        self.assertFalse(self.hotel.available_rooms < self.hotel.total_rooms)

    def test_cancel_reservation_invalid(self):
        res = Reservation(self.customer, self.hotel, "invalid-date")
        with self.assertRaises(ValueError):
            res.cancel()

    def test_reservation_date_validation(self):
        with self.assertRaises(ValueError):
            Reservation(self.customer, self.hotel, "2026/02/21")


if __name__ == "__main__":
    unittest.main()