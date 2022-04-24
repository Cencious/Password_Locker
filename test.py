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
    def test_credential(self):
        self.assertEqual(self.cred.site,"facebook")
        self.assertEqual(self.cred.username,"cencious")
        self.assertEqual(self.cred.password,"1989")

   

           