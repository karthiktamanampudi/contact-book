import json
import os

CONTACTS_FILE = 'contacts.json'


def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return {}


def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts[name] = {'phone': phone, 'email': email}
    save_contacts(contacts)
    print("Contact added.")


def remove_contact(contacts):
    name = input("Enter name of the contact to remove: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact removed.")
    else:
        print("Contact not found.")


def search_contact(contacts):
    name = input("Enter name of the contact to search: ")
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print("Contact not found.")


def view_contacts(contacts):
    if contacts:
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("No contacts found.")


def main():
    contacts = load_contacts()
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Search Contact")
        print("4. View All Contacts")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            remove_contact(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            view_contacts(contacts)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
