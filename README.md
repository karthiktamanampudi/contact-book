# Contact Book Application

This is a simple Contact Book application written in Python. It allows users to add, remove, search, and view contacts. The contact information is stored in a JSON file for persistence.

## Features

- Add a new contact with a name, phone number, and email address.
- Remove an existing contact by name.
- Search for a contact by name and view their details.
- View all contacts in the contact book.
- Contacts are stored in a JSON file for data persistence.

## Prerequisites

- Python 3.x

## How to Run

1. **Clone the repository or download the script:**

    ```sh
    git clone <repository-url>
    cd <repository-folder>
    ```

2. **Run the script:**

    ```sh
    python contact_book.py
    ```

3. **Follow the on-screen menu:**

    ```
    Contact Book Menu
    1. Add Contact
    2. Remove Contact
    3. Search Contact
    4. View All Contacts
    5. Exit
    Enter your choice:
    ```

## Code Overview

- **load_contacts()**: Loads contacts from a JSON file. If the file doesn't exist, it returns an empty dictionary.
- **save_contacts(contacts)**: Saves the contacts dictionary to a JSON file.
- **add_contact(contacts)**: Prompts the user for contact details and adds the contact to the dictionary.
- **remove_contact(contacts)**: Prompts the user for the contact name to remove and deletes it from the dictionary if it exists.
- **search_contact(contacts)**: Prompts the user for a contact name to search and displays the contact details if found.
- **view_contacts(contacts)**: Displays all the contacts in the dictionary.
- **main()**: Provides a menu for the user to choose an operation and executes the corresponding function.

## Example Usage

1. **Add a Contact**:
    ```
    Enter name: John Doe
    Enter phone number: 123-456-7890
    Enter email: john.doe@example.com
    Contact added.
    ```

2. **Remove a Contact**:
    ```
    Enter name of the contact to remove: John Doe
    Contact removed.
    ```

3. **Search a Contact**:
    ```
    Enter name of the contact to search: John Doe
    Name: John Doe
    Phone: 123-456-7890
    Email: john.doe@example.com
    ```

4. **View All Contacts**:
    ```
    Name: Jane Smith, Phone: 987-654-3210, Email: jane.smith@example.com
    ```

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss changes.

## Acknowledgements

This project was created as a beginner-friendly exercise for learning Python.
