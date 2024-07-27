import pickle

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone_number}, Email: {self.email}, Address: {self.address}"

def load_contacts():
    try:
        with open('contacts.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    with open('contacts.pkl', 'wb') as f:
        pickle.dump(contacts, f)

def add_contact(contacts):
    name = input("Enter the store name: ")
    phone_number = input("Enter the phone number: ")
    email = input("Enter the email: ")
    address = input("Enter the address: ")
    contacts[name] = Contact(name, phone_number, email, address)
    print("Contact added successfully!")

def view_contact_list(contacts):
    if contacts:
        for name, contact in contacts.items():
            print(contact)
    else:
        print("No contacts found.")

def search_contact(contacts):
    search_term = input("Enter the name or phone number to search: ")
    found = False
    for contact in contacts.values():
        if search_term in contact.name or search_term in contact.phone_number:
            print(contact)
            found = True
    if not found:
        print("No contact found.")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone_number = input("Enter the new phone number: ")
        email = input("Enter the new email: ")
        address = input("Enter the new address: ")
        contacts[name] = Contact(name, phone_number, email, address)
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def main():
    contacts = load_contacts()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contact_list(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            save_contacts(contacts)
            print("Contacts saved. Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
