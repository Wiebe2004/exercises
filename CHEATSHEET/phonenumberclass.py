import re
from abc import ABC, abstractmethod

class PhoneNumber(ABC):
    def __init__(self, number):
        self._number = number
        if not self.validate():
            raise ValueError(f"Invalid phone number: {number}")

    @property
    def number(self):
        return self._number

    @abstractmethod
    def validate(self):
        pass

class MobilePhone(PhoneNumber):
    def validate(self):
        # Belgium mobile phone: starts with 04 followed by 8 digits or preceded by landcode (0032, +32)
        mobile_pattern = re.compile(r'^(04\d{8}|(0032|\+32)\d{9})$')
        return mobile_pattern.match(self._number) is not None

class FixedPhone(PhoneNumber):
    def validate(self):
        # Fixed phone: starts with 0 and has 9 digits in total
        fixed_pattern = re.compile(r'^0\d{8}$')
        return fixed_pattern.match(self._number) is not None

class Contact:
    def __init__(self, name, email, phone_numbers):
        if len(name) < 1:
            raise ValueError("Name must be at least 1 character long")
        if not self.validate_email(email):
            raise ValueError(f"Invalid email: {email}")
        if not phone_numbers:
            raise ValueError("At least one phone number is required")
        
        self.name = name
        self.email = email
        self._phone_numbers = phone_numbers

    @property
    def phone_numbers(self):
        return self._phone_numbers

    def validate_email(self, email):
        email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        return email_pattern.match(email) is not None

class ContactsManager:
    def __init__(self):
        self._contacts = []

    @property
    def contacts(self):
        return self._contacts

    def add_contact(self):
        name = input("Enter contact name: ")
        email = input("Enter contact email: ")
        
        phone_numbers = []
        while True:
            number = input("Enter phone number: ")
            phone_type = input("Is this a mobile or fixed number? (m/f): ")
            if phone_type.lower() == 'm':
                phone_numbers.append(MobilePhone(number))
            elif phone_type.lower() == 'f':
                phone_numbers.append(FixedPhone(number))
            else:
                print("Invalid phone type. Please enter 'm' for mobile or 'f' for fixed.")

            more = input("Do you want to add another phone number? (y/n): ")
            if more.lower() != 'y':
                break

        if any(contact.name == name for contact in self._contacts):
            print("Error: A contact with this name already exists.")
            return
        
        new_contact = Contact(name, email, phone_numbers)
        self._contacts.append(new_contact)
        print("Contact added successfully.")

    def delete_contact(self):
        name = input("Enter the name of the contact to delete: ")
        contact = next((contact for contact in self._contacts if contact.name == name), None)
        if contact:
            self._contacts.remove(contact)
            print("Contact deleted successfully.")
        else:
            print("Error: Contact not found.")

    def find_contact(self):
        query = input("Enter name, email, or phone number to search: ")
        results = [contact for contact in self._contacts if 
                   query in contact.name or
                   query in contact.email or
                   any(query in phone.number for phone in contact.phone_numbers)]
        if results:
            for contact in results:
                self.display_contact(contact)
        else:
            print("No contacts found.")

    def display_contact(self, contact):
        print(f"Name: {contact.name}, Email: {contact.email}")
        for phone in contact.phone_numbers:
            print(f"Phone: {phone.number} (Type: {'Mobile' if isinstance(phone, MobilePhone) else 'Fixed'})")

    def display_all_contacts(self, sort_by="name", order="asc"):
        key_func = {
            "name": lambda contact: contact.name,
            "email": lambda contact: contact.email,
            "number": lambda contact: contact.phone_numbers[0].number
        }[sort_by]

        sorted_contacts = sorted(self._contacts, key=key_func, reverse=(order == "desc"))

        for contact in sorted_contacts:
            self.display_contact(contact)

# Example usage:
manager = ContactsManager()

# Add contacts
manager.add_contact()

# Display all contacts
manager.display_all_contacts()

# Find a contact
manager.find_contact()

# Delete a contact
manager.delete_contact()

# Display all contacts after deletion
manager.display_all_contacts()
