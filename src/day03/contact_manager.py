# Day 3 - Mini Project: Contact Manager
# Combines lists, dictionaries, and comprehensions into one project!

contacts = []


def add_contact(name, phone, email):
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    print(f"Added {name}")


def list_contacts():
    if not contacts:
        print("No contacts yet")
        return

    print("\n=== All Contacts ===")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']} - {contact['email']}")


def search_contact(name):
    results = []

    if results:
        print(f"\nFound {len(results)} contact(s):")
        for contact in results:
            print(f"  {contact['name']} - {contact['phone']} - {contact['email']}")
    else:
        print(f"No contacts found with name: {name}")


def delete_contact(name):
    original_count = len(contacts)

    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            break

    if len(contacts) < original_count:
        print(f"Deleted {name}")
    else:
        print(f"Contact '{name}' not found")


# Main program loop
print("=== Contact Manager ===")

while True:
    print("\n--- Menu ---")
    print("1. Add contact")
    print("2. List contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")

    choice = input("\nEnter choice (1-5): ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        add_contact(name, phone, email)

    elif choice == "2":
        list_contacts()

    elif choice == "3":
        name = input("Search name: ")
        search_contact(name)

    elif choice == "4":
        name = input("Delete name: ")
        delete_contact(name)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
