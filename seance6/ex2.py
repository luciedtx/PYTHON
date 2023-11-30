class Personne :
    def __init__(self, nom , prenom):
        self.nom = nom
        self.prenom = prenom

class Etudiant(Personne):
    def __init__(self, nom, prenom, niveau):
        super().__init__(nom, prenom)
        self.niveau= niveau

    def affichage(self):
        print(f"{self.nom} - {self.prenom}, niveau : {self.niveau}")

etudiant1= Etudiant("Dtx","Lucie","Gtech1")
etudiant1.affichage()