from ex6 import Calculatrice
from unittest import TestCase, main

class TestCalc(TestCase):
    def testaddition(self):
        self.assertEqual(Calculatrice.addition(2,8),10)

    def testsoustract(self):
        self.assertEqual(Calculatrice.soustraction(2,8),-6)
    def testmultip(self):
        self.assertEqual(Calculatrice.multiplication(2,5),10)
    def testdiv(self):
        self.assertEqual(Calculatrice.division(4,2),2)

main()