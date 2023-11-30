import math 
from abc import ABC, abstractclassmethod

class Forme :
    @abstractclassmethod
    def aire(self):
        pass

class Rectangle(Forme):
    def __init__(self, largeur, longueur):
        self.largeur= largeur
        self.longueur= longueur
    def aire(self) :
        return self.longueur * self.largeur

class Cercle(Forme) :
    def __init__(self, rayon):
        self.rayon= rayon
    def aire(self):
        return math.pi* self.rayon**2
    
class Triangle(Forme):
    def __init__(self, base, hauteur):
        super().__init__()
        self.base= base
        self.hauteur= hauteur
    def aire(self):
        return self.base* self.hauteur/2
    
rect= Rectangle(5,8)
