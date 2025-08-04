# list contains admins

admins=['wissam','ahmed','sara','khaled','abeer','yamen','leen']

#login
name=input("please enter your name:").strip()

#if name in admin
if name in admins:
    print(f"Hello {name} welcome back...")
    option=input('Do you want to (update) or (delete) your name?').strip().lower()
    #update option
    if option=="update" or option=="u":
        new_name=input("Please enter you new name:").strip()
        admins[admins.index(name)]=new_name
        print("The has been updated.")
        print(admins)
    #Delete option
    elif option == "delete" or option == "d":
        admins.remove(name)
        print(f"({name}) has been deleted.")
        print(admins)
    else:
        print("Wrong choice,please try again.")    
else:
    statu=input("you are not an admin,do you want to add yourself? Y/N?").strip().capitalize()
    if statu == "Y" or statu == "yes":
        x=input("Enter the name that you want to be added:").strip()
        if x in admins:
            print("This name already exists.")
        else:
            admins.append(x)
            print("You have been added")
            print(admins)
    elif statu == "N" or statu == "no":
        print("You are not added.")
                
       
         
    
        
    

