from operator import itemgetter


class ContactsManager:
    """
    Manages a list of contacts with functionality to add, remove, and search contacts.
    """
    def __init__(self):
        self.__contacts = []

    @property
    def contacts(self):
        return self.__contacts

    def contact_existence_check(self, contact_name):
        contact_names = [contact.name for contact in self.__contacts]
        return contact_name in contact_names

    def add(self, contact):
        if self.contact_existence_check(contact.name):
            raise ValueError("The contact already exists!")
        else:
            self.__contacts.append(contact)

    def delete(self, contact):
        if not self.contact_existence_check(contact.name):
            raise ValueError("The contact doesn't exists!")

        for i in range(len(self.__contacts)):
            if self.__contacts[i].name == contact.name:
                self.__contacts.pop(i)
                break

    def find(self, contact_info):
        for i in range(len(self.__contacts)):
            if (self.__contacts[i].name == contact_info) or (self.__contacts[i].email == contact_info) or (contact_info in self.__contacts[i].numbers):
                return self.__contacts[i]

    def display_contacts(self, sorting_method):

        sorting_method = sorting_method.lower()

        if sorting_method == "ascending":
            return sorted(self.__contacts, key=lambda c: c.name)
        elif sorting_method == "descending":
            return sorted(self.__contacts, key=lambda c: c.name, reverse=True)
        elif sorting_method == "name":
            return sorted(self.__contacts, key=lambda c: c.name)
        elif sorting_method == "email":
            return sorted(self.__contacts, key=lambda c: c.email)
        elif sorting_method == "number":
            return sorted(self.__contacts, key=lambda c: c.numbers[0] if c.numbers else "")
        else:
            raise ValueError(f"Unsupported sorting method: {sorting_method}")

