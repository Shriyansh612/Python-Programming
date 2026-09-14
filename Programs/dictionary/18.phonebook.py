contacts = {"Myself" : 7895459249,
            "Raghu" : 8077488432,
            "Mummy" : 6397743337,
            "Papa" : 9412534953,
            "Ravi" : 7893429424}
blocked = {}

op=-1

print('''PHONEBOOK
      
To end: 0 
Add Contact: 1
Search Contact: 2
Update Contact: 3
Delete Contact: 4
Display all contacts: 5
Count total no. of contacts: 6
Block a contact: 7
Unblock a contact: 8       
Display blocked contacts: 9\n''')

while(op!=0):
    op = input("Enter operation: ").strip()
    if(op.isdigit()):
        op = int(op)
        if(op<10):
            match op:
                case 1:     #to add a new contact
                    name = input("\nEnter name of contact: ").strip()
                    if (name in contacts):
                        print("A contact by this name is already present in contacts\n")
                    else:  
                        num = input("Enter phone number: ").strip() 
                        if(len(num)!=10 or num.isdigit()==False):
                            print("Invalid contact number\n")
                        elif(num in contacts.values()):
                            print("A contact by this phone number already exists\n")                            
                        else:
                            contacts.update({name:int(num)})
                            print("Contact Added\n")
                case 2:     #to search a contact
                    print('''
To search by name: 1
To search by number: 2
                                ''')
                    search = input("\n").strip()
                    if(search.isdigit()):
                        search = int(search)
                        if(search == 1):
                            name = input("Enter name of contact: ").strip()
                            if (name in contacts):
                                print("Contact Found\n")
                                print(name,":",contacts[name])
                            else:
                                print("Contact not found\n")    
                        elif(search == 2):
                            num = input("Enter phone number: ").strip()
                            if(len(num)!=10 or num.isdigit()==False):
                                print("Invalid phone number\n")
                            else:
                                num = int(num)
                                if(num not in contacts.values()):
                                    print("Contact not found\n")
                                else:        
                                    print("Contact Found\n")
                                    for name in contacts:
                                        if(contacts[name] == num):
                                            print(name,":",num)
                                            break
                        else:
                            print("Invalid Input\n")    
                    else:
                        print("Invalid Input\n") 
                case 3:         #to update contact
                    print("\nEnter contact name to be updated")
                    name = input("Enter contact name: ").strip()
                    if(name not in contacts):
                        print("Contact not found\n")
                    else:
                        print('''
To update contact name: 1
To update contact number: 2''') 
                        update = input().strip() 
                        if(update.isdigit()):
                            update = int(update)
                            if(update == 1):
                                new_name = input("Enter new contact name: ").strip()
                                if(new_name in contacts):
                                    print("A contact by this name already exists\n")
                                else:
                                    contacts.update({new_name : contacts[name]})
                                    contacts.pop(name)
                                    print("Contact name updated\n")
                            elif(update == 2):
                                new_num = input("Enter new phone number: ").strip()
                                if(len(new_num)!=10 or new_num.isdigit()==False):
                                    print("Invalid contact number\n")
                                else:
                                    new_num = int(new_num)
                                    contacts.update({name:new_num})
                                    print("Contact number updated\n") 
                            else:
                                print("invalid input\n")
                        else:
                            print("invalid input\n") 
                case 4:         #to delete contact
                    print('''
To delete by contact name: 1
To delete by contact number: 2 ''')  
                    delete = input().strip()
                    if(delete.isdigit()):
                        delete = int(delete)
                        if(delete == 1):
                            name = input("Enter contact name to be deleted: ").strip()
                            if(name not in contacts):
                                print("Contact not found\n")
                            else:
                                contacts.pop(name)
                                print("Contact deleted\n")
                        elif(delete == 2):
                            num = input("Enter contact number to be deleted: ").strip()
                            if(len(num)!=10 or num.isdigit()==False):
                                print ("invalid contact number\n")
                            else:
                                num = int(num)
                                if(num not in contacts.values()):
                                    print("Contact number not found\n")
                                else:
                                    for name in contacts:
                                        if(contacts[name] == num):
                                            contacts.pop(name)
                                            print("Contact deleted\n")
                                            break
                        else:
                            print("Invalid input\n")
                    else:        
                        print("invalid input\n")
                case 5:     #To display all contacts
                    print("\nContacts: ")
                    for key,value in contacts.items():
                        print(key,":",value)
                    print("\n")                        
                case 6:     #To count total number of contacts
                    print("\nTotal number of contacts are: ", len(contacts)+"\n")
                case 7:     #To block a contact
                    name = input("\nEnter contact name to be blocked: ")
                    if (name not in contacts):
                        print("Contact not found\n")
                    else:
                        blocked.update({name:contacts[name]}) 
                        print("Contact blocked\n")
                case 8:     #To unblock a contact
                    name = input("\nEnter contact name to be unblocked: ")
                    if (name not in blocked):
                        print("No such contact exists among blocked contacts\n")
                    else:
                        blocked.pop(name) 
                        print("Contact unblocked\n")
                case 9:
                    print("\nBlocked Contacts: ")
                    for key, value in blocked.items():
                        print(key,":",value)
                        print("\n")                                                      

