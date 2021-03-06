import random 
"""
users and credentials array are used to store all the user objects and credential respectively
"""
users=[] 
credentials=[]

class User:
    """
    used to create an object containing username and password
    """
    def __init__(self, username, password):
        self.username=username
        self.password=password

class Credentials:
    """
    used to store site name,username and password
    """ 
    def __init__(self, site ,username, password):
        self.site=site
        self.username=username
        self.password=password
    def new():
        print("\nSelect an option to continue")
        print("1.New credentials\n2.Existing credentials\n3.View credentials\n4.Delete credentials")
        option=input()

        if option=="1":
            print("\nAdd the new account to the password manager: ")
            site=input("Enter site name: ")
            username=input("Enter username: ")
            print("Do you want the application to generate you a password?\n1.Yes\n2.No")
            selection=input()
            if selection=="1":
                password=str(random.randint(1000000,9999999))

            elif selection=="2":
                password=input("Enter password: ")

            else:
                print("Invalid option")
            credential=Credentials(site, username, password)
            credentials.append(credential)
            print("Added successfully")
            Credentials.new()

        elif option=="2":
            print("\nAdd the existing account to the password manager:")
            site=input("Enter site name: ")
            username=input("Enter username: ")
            password=input("Enter password: ")
            credential=Credentials(site, username, password)
            credentials.append(credential)
            print("Added successfully")
            Credentials.new()

        elif option=="3":
            print("\nView accounts in password manager: ")
            for x in credentials:
                print("Site name: " + x.site)
                print("username: " + x.username)
                print("password: " + x.password)
            Credentials.new()

        elif option=="4":            
            print("\nEnter the name of the site you want to delete: ")
            name=input()            
            for i, o in enumerate(credentials):
                if o.site== name:
                    del credentials[i]
            Credentials.new()
        else:
            print("Invalid option")

class Main: 
    """
    authenticating user on the app
    """
    
    def register():
        print("\nCreate new account")
        username=input("Enter username: ")
        password=input("Enter new password: ")
        c_password=input("Confirm your password: ")
        if password==c_password:
            user=User(username,password)
            users.append(user)
            Main.login()
        else:
            print("passwords do not match")
            Main.register() 
        
            
    def login():
        print("\nLogin to your account")
        users.append(User("admin","admin"))
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        for x in users:
            if x.username==username and x.password==password:
                Credentials.new()
            else:
                print("Invalid login attempt")
                Main.login()
    """
    navigate user either to register or login
    """
            
    def navigate (x):
        if x=="1":
            Main.register()
        elif x=="2":
            Main.login()
        elif x=="3":
            exit()
        else:
            print ("invalid password")
        
print ("Welcome to Password Locker")
print ("Select an option to continue")
print ("1.Register\n2.Login\n3.Exit") 
option=input()
Main.navigate(option)