import os
import json

# File to store contact data
FILE_NAME = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(FILE_NAME)
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone: ").strip()
    email = input("Enter Email: ").strip()
    if name and phone:
        contacts.append({"name": name, "phone": phone, "email": email})
        print(f"Contact '{name}' added successfully!")
    else:
        print("Error: Name and Phone are required.")

# Search for a contact
def search_contact(contacts):
    name = input("Enter Name to Search: ").strip()
    results = [c for c in contacts if c["name"].lower() == name.lower()]
    if results:
        for contact in results:
            print(contact)
    else:
        print("No contact found.")

# Update a contact
def update_contact(contacts):
    name = input("Enter Name to Update: ").strip()
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contact["phone"] = input("Enter New Phone: ").strip() or contact["phone"]
            contact["email"] = input("Enter New Email: ").strip() or contact["email"]
            print(f"Contact '{name}' updated successfully!")
            return
    print("No contact found.")

# Main menu
def main():
    contacts = load_contacts()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Display All Contacts")
        print("5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            for contact in contacts:
                print(contact)
        elif choice == "5":
            save_contacts(contacts)
            print("Exiting and saving contacts. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
