import random
"""
The users and credentials array are used to store all the users objecs and credentials
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
    used to store site name, username and password.
    """
    def __init__(self, site, username, password):
        self.site=site
        self.username=username
        self.password=password
    def new():
        print("\nSelect an option to continue")
        print("1.New credentials\n2.Existing credentials\n3.Vie credentials\n4.Delete credentials")
        option=input()
    
