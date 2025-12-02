class phonebook:
    directory_data = []
    
    def __init__(self, name, numbers):
        self.name = name
        self.number = numbers
        phonebook.directory_data.append(self)

    @classmethod
    def show_contacts(cls):
        print("* These are all the the contact that are stored in your directory -->   ")
        for user_contact in cls.directory_data:
            print(f"1. Name: {user_contact.name}\n2. Number: {user_contact.number}")

    @classmethod
    def search_contact(cls, search_name):
        for user_contact in cls.directory_data:
            if user_contact.name == search_name:   
                print(f"Found contact → Name: {user_contact.name}, Number: {user_contact.number}")
                return
        print(f"Contact not found similar to {search_name}")
    @staticmethod
    def vaild_phone_number(number):
        if len(number) >= 8 and number.isdigit():
            return True
        else:
            return False

no_contact = int(input("Enter the number of contact that you want to add:  "))

for i in range(no_contact):
    name = input("Enter the name of the contact: ")
    contact = input("Enter the number: ")
    if phonebook.vaild_phone_number(contact):
        phonebook(name,contact)
    else: 
        print (f"INVALID phone number for name: {name}\nThe phone number should be atleast of 8 Digit.")


phonebook.show_contacts()