# classe mère
class Vehicule :
    def __init__(self, marque, modele) :
        self.marque = marque
        self.modele= modele
    def avancee(self): 
        print(f"la {self.modele} avance")

# classe fille 
class Voiture(Vehicule) :
    def __init__(self, marque, modele, couleur):
        # Vehicule.__init__(self, marque, modele,)
        super().__init__(marque, modele) #super n'a pas de self, autre facon de recuperer la classe mère
        self.couleur = couleur
    
    def info(self):
        print(f"{self.modele} est électrique et {self.couleur}")

    def avancee(self):
        print(f"{self.modele} roule ")

voit= Voiture("Renault","Zoé","noire ")
voit.avancee()
voit.info()

# classe fille
class Avion(Vehicule) :
    def __init__(self, marque, modele):
        Vehicule.__init__(self,marque,modele)
    def avancee(self): #surcharge de methode, on redefinit la meme methode dans deux classes differentes
        print(f"{self.modele} vole ")

avion= Avion("Airbus","A-320")
avion.avancee()