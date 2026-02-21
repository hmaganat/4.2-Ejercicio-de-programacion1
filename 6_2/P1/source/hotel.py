"""
hotel.py

Defines the Hotel class used in the reservation system.
"""


class Hotel:
    """
    Represents a hotel entity.
    """

    def __init__(self, hotel_id, name, location, total_rooms):
        """
        Initialize a Hotel instance.

        :param hotel_id: Unique identifier for the hotel
        :param name: Name of the hotel
        :param location: Location of the hotel
        :param total_rooms: Total number of rooms
        """
        # Accept numeric IDs as well; normalize to string
        if not isinstance(hotel_id, (str, int)):
            raise ValueError("hotel_id must be a string or integer")

        hotel_id = str(hotel_id).strip()
        if not hotel_id:
            raise ValueError("hotel_id must be a non-empty string")

        if not isinstance(name, str) or not name.strip():
            raise ValueError("name must be a non-empty string")

        if not isinstance(location, str) or not location.strip():
            raise ValueError("location must be a non-empty string")

        if not isinstance(total_rooms, int) or total_rooms < 0:
            raise ValueError("total_rooms must be a non-negative integer")

        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.total_rooms = total_rooms
        self.available_rooms = total_rooms

    def reserve_room(self):
        """
        Reserve one room if available.

        :return: True if successful, False otherwise
        """
        if self.available_rooms > 0:
            self.available_rooms -= 1
            return True
        return False

    def cancel_reservation(self):
        """
        Cancel a reservation and free one room.

        :return: True if successful, False otherwise
        """
        if self.available_rooms < self.total_rooms:
            self.available_rooms += 1
            return True
        return False

    def update_information(self, name=None, location=None, total_rooms=None):
        """
        Update hotel information.

        :param name: New name (optional)
        :param location: New location (optional)
        :param total_rooms: New total rooms (optional)
        """
        if name is not None:
            if not isinstance(name, str) or not name.strip():
                raise ValueError("name must be a non-empty string")
            self.name = name

        if location is not None:
            if not isinstance(location, str) or not location.strip():
                raise ValueError("location must be a non-empty string")
            self.location = location

        if total_rooms is not None:
            if not isinstance(total_rooms, int) or total_rooms < 0:
                raise ValueError(
                    "total_rooms must be a non-negative integer"
                )

            occupied_rooms = self.total_rooms - self.available_rooms

            if total_rooms < occupied_rooms:
                raise ValueError(
                    "Cannot reduce total_rooms below occupied rooms"
                )

            self.total_rooms = total_rooms
            self.available_rooms = total_rooms - occupied_rooms

    def to_dict(self):
        """
        Convert Hotel instance to dictionary.

        :return: dict representation
        """
        return {
            "hotel_id": self.hotel_id,
            "name": self.name,
            "location": self.location,
            "total_rooms": self.total_rooms,
            "available_rooms": self.available_rooms,
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create Hotel instance from dictionary.

        :param data: dict
        :return: Hotel instance
        """
        required_fields = {
            "hotel_id",
            "name",
            "location",
            "total_rooms",
            "available_rooms",
        }

        if not required_fields.issubset(data.keys()):
            raise ValueError("Missing required hotel fields")

        hotel = cls(
            data["hotel_id"],
            data["name"],
            data["location"],
            data["total_rooms"],
        )

        hotel.available_rooms = data["available_rooms"]
        return hotel

    def display(self):
        """
        Return formatted string with hotel information.

        :return: str
        """
        return (
            f"Hotel ID: {self.hotel_id}\n"
            f"Name: {self.name}\n"
            f"Location: {self.location}\n"
            f"Total Rooms: {self.total_rooms}\n"
            f"Available Rooms: {self.available_rooms}"
        )
      
