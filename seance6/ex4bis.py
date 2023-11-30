class Forme :
    def aire(self):
        pass
        

class Cercle(Forme) :
    def __init__(self, rayon):
        self.rayon= rayon
    def aire(self):
        return 3.14 * self.rayon**2

class Rectangle(Forme):
    def __init__(self, largeur, longueur):
        self.largeur= largeur
        self.longueur= longueur
    def aire(self) :
        return self.longueur * self.largeur

rect= Rectangle(12,14)
print(f"l'aire du rectangle est {rect.aire()}")

cercle= Cercle(5)
print(f"l'aire du cercle est {cercle.aire()}")
