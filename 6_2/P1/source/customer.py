"""
customer.py

Defines the Customer class used in the reservation system.
"""

import re


class Customer:
    """
    Represents a customer entity.
    """

    def __init__(self, customer_id, name, email, phone=""):
        """
        Initialize a Customer instance.

        :param customer_id: Unique identifier
        :param name: Customer name
        :param email: Customer email
        :param phone: Customer phone
        """
        # Accept numeric IDs as well; normalize to string
        if not isinstance(customer_id, (str, int)):
            raise ValueError("customer_id must be a string or integer")

        customer_id = str(customer_id).strip()
        if not customer_id:
            raise ValueError("customer_id must be a non-empty string")

        if not isinstance(name, str) or not name.strip():
            raise ValueError("name must be a non-empty string")

        if not self._validate_email(email):
            raise ValueError("Invalid email format")

        # phone can be optional (default empty string)
        if phone is None:
            phone = ""

        if not isinstance(phone, str):
            raise ValueError("phone must be a string")

        self.customer_id = customer_id
        self.name = name
        self._email = email
        self.phone = phone

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not self._validate_email(value):
            raise ValueError("Invalid email format")
        self._email = value

    @staticmethod
    def _validate_email(email):
        """
        Validate email format.

        :param email: email string
        :return: bool
        """
        if not isinstance(email, str):
            return False

        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(pattern, email) is not None

    def update_information(self, name=None, email=None, phone=None):
        """
        Update customer information.

        :param name: New name (optional)
        :param email: New email (optional)
        :param phone: New phone (optional)
        """
        if name is not None:
            if not isinstance(name, str) or not name.strip():
                raise ValueError("name must be a non-empty string")
            self.name = name

        if email is not None:
            if not self._validate_email(email):
                raise ValueError("Invalid email format")
            self.email = email

        if phone is not None:
            if not isinstance(phone, str) or not phone.strip():
                raise ValueError("phone must be a non-empty string")
            self.phone = phone

    def to_dict(self):
        """
        Convert Customer instance to dictionary.

        :return: dict representation
        """
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create Customer instance from dictionary.

        :param data: dict
        :return: Customer instance
        """
        required_fields = {"customer_id", "name", "email"}

        if not required_fields.issubset(data.keys()):
            raise ValueError("Missing required customer fields")

        return cls(
            data["customer_id"],
            data["name"],
            data["email"],
            data.get("phone", ""),
        )

    def display(self):
        """
        Return formatted string with customer information.

        :return: str
        """
        return (
            f"Customer ID: {self.customer_id}\n"
            f"Name: {self.name}\n"
            f"Email: {self.email}\n"
            f"Phone: {self.phone}"
        )

    def delete_customer(self, customer_id):
        """
        Placeholder delete method used in tests: returns False
        when the customer to delete doesn't match this one.
        """
        if str(customer_id) == str(self.customer_id):
            # Not implemented: deletion would happen in persistence layer
            return True
        return False
