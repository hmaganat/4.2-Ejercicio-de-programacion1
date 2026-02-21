import unittest
from source.hotel import Hotel


class TestHotel(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel(
            hotel_id="H001",
            name="Hotel Test",
            location="City",
            total_rooms=10
        )

    def test_initial_state(self):
        self.assertEqual(self.hotel.total_rooms, 10)
        self.assertEqual(self.hotel.available_rooms, 10)

    def test_reserve_room(self):
        self.hotel.reserve_room()
        self.assertEqual(self.hotel.available_rooms, 9)

    def test_cancel_reservation(self):
        self.hotel.reserve_room()
        self.hotel.cancel_reservation()
        self.assertEqual(self.hotel.available_rooms, 10)

    def test_display(self):
        info = self.hotel.display()
        self.assertIn("Hotel ID: H001", info)


if __name__ == "__main__":
    unittest.main()