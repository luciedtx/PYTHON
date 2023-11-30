class Personne :
    def __init__(self, nom , prenom, adresse):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
    def affichepersonne(self) :
        print(f"{self.nom} - {self.prenom}, {self.adresse}")

class Adresse :
    def __init__(self,rue,ville,codep):
        self.rue= rue
        self.ville= ville
        self.codep= codep
    def afficheadresse(self) :
        print(f"{self.rue} - {self.ville} - {self.codep}")
        
        
class Employe(Personne, Adresse) :
    def __init__(self, nom, prenom, adresse, post, salaire):
        super().__init__(nom, prenom, adresse)
        self.post= post
        self.salaire= salaire

employe1= Employe("Theo", 26, "5 allee du tr du lac","clamart",92140,"directeur RH",2000)
print(f"{employe1.affichepersonne}, {employe1.afficheadresse}, il travail en tant que {employe1.post} et son salaire est de {employe1.salaire}")