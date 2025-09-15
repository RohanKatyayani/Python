"""
🧠 Problem Statement:

You’re going to build a Contact Book that allows the user to:
	1.	Add a new contact with a name and phone number
	2.	Search for a contact by name
	3.	Delete a contact
	4.	View all saved contacts
	5.	Exit the app

"""

contacts = {}

def contact_book():
    while True:
        print("Welcome to the Contact Book")
        print("What would you like to do?")
        print("1. Add a new contact")
        print("2. Search for a contact")
        print("3. Delete a contact")
        print("4. View all saved contacts")
        print("5. Exit the app")
        choice = input("> ")

        # Todo 1: Add a new contact with a name and phone number
        if choice == "1":
            name = input("Enter a Name: ")
            number = input("Enter a Phone Number: ")
            contacts[name] = number
            print("Contact added")

        # Todo 2: Search for a contact by name
        elif choice == "2":
            name = input("Enter a Name: ")
            if name in contacts:
                print("Contact found", contacts[name])
            else:
                print("Contact not found")

        # Todo 3: Delete a contact
        elif choice == "3":
            name = input("Enter the Name of the contact you wanna delete: ")
            if name in contacts:
                del contacts[name]
                print("Contact deleted")
            else:
                print("Contact not found")

        # Todo 4: View all saved contacts
        elif choice == "4":
            print("Contacts: ", contacts)

        # Todo 5: Exit the App
        elif choice == "5":
            print("Exiting the app")
            exit()
            break

contact_book()



