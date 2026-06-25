class contact_book :
    def __init__ (self) :
        self.contact: dict = {}

    def add_contact(self , name: str , phone: str , email: str , address: str) :
        if name not in self.contact:
            self.contact[name] = {'phone' : phone , 'email' : email , 'address' : address}
            print("Contact added successfully!")
        else : 
            print("Contact already exists.")

    def view_contact(self) :

        for name , info in self.contact.items() :
            print('name :', name)
            print('phone :', info['phone'])
            print('email:' , info['email'])
            print('address :' , info['address'])
            print('-' * 50)

    def delete_contact (self , name:str) :

        if name in self.contact:
            del self.contact[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found")

    def update_contact(self , name: str , phone: str = None, email: str = None, address: str = None  ):
        
        if name in self.contact :
            if phone :
                self.contact[name]['phone'] = phone
            if email :
                self.contact[name]['email'] = email
            if address :
                self.contact[name]['address'] = address
            print('contact update successfully!')
            return
        print('contact not found')



if __name__ == '__main__' :
    book = contact_book()

    while True :
        print('\n--- Contact Book Application ---')
        print('1. Add contact')
        print('2. Edit Contact')
        print('3. View Contact')
        print('4. Delete Contact')
        print('5. Quite')
        user_choice = input('\n Please choose aption: ')

        if user_choice == '1' :
            name = input("\nEnter Contact name: ")
            phone = input("Enter Contact phone: ")
            email = input("Enter Contact email: ")
            address = input("Enter Contact address: ")
            book.add_contact(name , phone , email , address)
        
        elif user_choice == '2' :
            name = input("\nEnter name of the contact to edit: ")
            phone = input("Enter new/updated phone number or press Enter to keep unchanged: ")
            email = input("Enter new/updated email or press Enter to keep unchanged: ")
            address = input("Enter new/updated address or press Enter to keep unchanged: ")
            book.update_contact(name , phone or None , email or None , address or None)

        elif user_choice == '3' :
            print("\nList of Contacts:")
            book.view_contact()

        elif user_choice == '4' :
            name = input("\nEnter name of contact to delete: ")
            book.delete_contact(name)
        elif user_choice == '5':
           print("\nThank You for using Contact Book Application. Goodbye!")
           break
        else :
            print("\nInvalid choice! Please try again.")

