import unittest
from main import user,Credentials
users=[]
credentials=[]

class TestMain(unitest.TestCase):
    def setup(self):
        self.user=User("Cencious", "2022")
        self.cred=Credentials("facebook","dhonne","1989")    
    def test_user(self):
        self.assertEqual(self.user.username, "Cencious")
        self.assertEqual(self.user.password,"2022")

           