class Personne :
    def __init__(self, nom , prenom):
        self.nom = nom
        self.prenom = prenom

    def presentation(self):
        print(f"{self.nom} - {self.prenom}")

class Employe :
    def __init__(self, code) :
        self.code = code

    def code_employe(self):
        print(f"{self.code}")

# Multihéritage ; classe qui herite des deux classes précédentes
class Formateur(Personne, Employe) :
    def __init__(self, nom, prenom, code, matiere): #constructeur ou on recupere les attributs des classes parentes
        self.matiere= matiere
        Personne.__init__(self, nom, prenom)
        Employe.__init__(self, code)
    
    def presentationemploye(self):
        print(f"Le formateur est {self.nom} {self.prenom}, son code est {self.code} et il enseigne la matiere: {self.matiere}")
        
formateur= Formateur("Yele","Randy", 1234, "Informatique")
formateur.presentation()
formateur.presentationemploye()