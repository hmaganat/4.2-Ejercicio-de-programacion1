import unittest
from source.reservation import Reservation
from datetime import date


class TestReservation(unittest.TestCase):
    def setUp(self):
        self.reservation = Reservation(
            reservation_id="R001",
            customer_id="C001",
            hotel_id="H001",
            check_in="2026-02-21",
            check_out="2026-02-25"
        )

    def test_dates(self):
        self.assertEqual(self.reservation.check_in, date(2026, 2, 21))
        self.assertEqual(self.reservation.check_out, date(2026, 2, 25))

    def test_to_dict(self):
        data = self.reservation.to_dict()
        self.assertEqual(data["reservation_id"], "R001")

    def test_from_dict(self):
        data = self.reservation.to_dict()
        r2 = Reservation.from_dict(data)
        self.assertEqual(r2.hotel_id, "H001")

    def test_display(self):
        info = self.reservation.display()
        self.assertIn("Reservation ID: R001", info)


if __name__ == "__main__":
    unittest.main()