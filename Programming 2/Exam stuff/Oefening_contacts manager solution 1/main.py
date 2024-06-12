from ContactsManager import *
from Contact import *

contacts = [Contact("Jashan", "jashan@gmail.com", ["0483715621"]),
            Contact("John", "johnD@icloud.com", ["0488231134", "987524212"]),
            Contact("Sarah", "sarah@icloud.com", ["0123456789"]),
            Contact("Mark", "mark@hotmail.com", ["9876543210"]),
            Contact("Emma", "emma@gmail.com", ["1234567890"])
            ]

contactManager = ContactsManager()

for contact in contacts:
    contactManager.add(contact)

print(contactManager.contacts)

# Deleting
# contactManager.delete(Contact("Jashan", "jashan@gmail.com", ["0483715621"]))
# contactManager.delete(Contact("John", "johnD@icloud.com", ["0488231134", "987524212"]))


# Finding
# print(contactManager.find("jashan@gmail.com"))

# Sorting
# print(contactManager.display_contacts("ascending"))
# print(contactManager.display_contacts("descending"))
# print(contactManager.display_contacts("name"))
# print(contactManager.display_contacts("email"))
# print(contactManager.display_contacts("number"))
