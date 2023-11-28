from unittest import TestCase, main
from addition import*

class Testaddition(TestCase):
    
    def testaddition2nb(self):
        # self.assertIn(1, [0,1,2,3]) #verifie si le 1 est dans la liste 
        # self.assertEqual(1, 1)
        self.assertEqual(addition(1,1),2) #on test notre fonction addition

main()