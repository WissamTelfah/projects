# list contains admins

admins=['wissam','ahmed','sara','khaled','abeer','yamen','leen']

#login
name=input("please enter your name:").strip()

#if name in admin
if name in admins:
    print(f"Hello {name} wellcome back...")
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
    if statu=="Yes" or "Y":
        x=input("Enter the name that you want to be added:").strip()
        print("You have been added")
        admins.append(x)
        print(admins.capitalize())
    else:
        print("You are not added.")    
print("fuck you")        
        
    
        
    
