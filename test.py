import unittest
from main import user,Credentials
users=[]
credentials=[]

class TestMain(unitest.TestCase):
     """
        Test class that defines test cases for the main class behavious.
        Args:
        unitest.TestCase: Testcase class that helps in creating test cases.
        """
def setup(self):

        """
        Set up method to run before each test cases, to help define instructions to be executed.
        """
        self.user=User("Cencious", "2022")
        self.cred=Credentials("facebook","dhonne","1989")    
def test_user(self):
        """
        test_user test case to test if the object is initialized properly
        """
        self.assertEqual(self.user.username, "Cencious")
        self.assertEqual(self.user.password,"2022")
def test_credential(self):
        self.assertEqual(self.cred.site,"facebook")
        self.assertEqual(self.cred.username,"cencious")
        self.assertEqual(self.cred.password,"1989")
def test_register(self):
        user=User("cencious","2022")
        users.append(user)
        self.assertEqual(len(users),1)

    
if __name__=="__main__":
        unitest.main()  
        """
        confirms that anything inside the if block should run only if this is the file that is currently being run
        """         