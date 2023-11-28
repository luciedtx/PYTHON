from abc import ABC, abstractmethod
class Animal(ABC) : #abc : abstract base class
    @abstractmethod
    def parler(self):
        pass

class Chien(Animal):
    def parler(self):
        print("aboie")