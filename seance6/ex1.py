# classe mère
class Vehicule :
    def __init__(self, marque, modele) :
        self.marque = marque
        self.modele= modele
    def avancee(self): 
        print(f"la {self.modele} avance")

# classe fille 
class Voiture(Vehicule) :
    def __init__(self, marque, modele, couleur, carburant):
        # Vehicule.__init__(self, marque, modele,) #recuperer la classe mère
        super().__init__(marque, modele) #super n'a pas de self, autre facon de recuperer la classe mère
        self.couleur = couleur
        self.carburant= carburant
    
    def info(self):
        print(f"{self.modele} est électrique et {self.couleur}")

    def avancee(self):
        print(f"{self.modele} roule ")
    
    def demarrer(self):
        if self.carburant<=5 :
            print(f"il ne reste plus que {self.carburant}L de carburant vous ne pouvez pas demarrer")
        else :
            print(f"il reste {self.carburant}L de carburant vous pouvez demarrer")

voit= Voiture("Renault","Zoé","noire",9)
voit.avancee()
voit.info()
voit.demarrer()
