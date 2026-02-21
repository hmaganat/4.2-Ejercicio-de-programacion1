import unittest
from source.hotel import Hotel


class TestHotelExtra(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel(hotel_id=1, name="Hilton", location="NY", total_rooms=5)

    def test_reserve_room_success(self):
        result = self.hotel.reserve_room()
        self.assertTrue(result)
        self.assertEqual(self.hotel.available_rooms, 4)

    def test_reserve_room_fail(self):
        self.hotel.available_rooms = 0
        result = self.hotel.reserve_room()
        self.assertFalse(result)

    def test_cancel_reservation(self):
        self.hotel.reserve_room()
        result = self.hotel.cancel_reservation()
        self.assertTrue(result)
        self.assertEqual(self.hotel.available_rooms, 5)

    def test_cancel_reservation_fail(self):
        # No hay habitaciones reservadas
        result = self.hotel.cancel_reservation()
        self.assertFalse(result)

    def test_modify_hotel(self):
        self.hotel.name = "Marriott"
        self.hotel.total_rooms = 10
        self.assertEqual(self.hotel.name, "Marriott")
        self.assertEqual(self.hotel.total_rooms, 10)

    def test_display(self):
        display_str = self.hotel.display()
        self.assertIn("Hilton", display_str)


if __name__ == "__main__":
    unittest.main()