
# Modifiez la classe Personne pour inclure un objet Adresse.(ex2)
class Personne :
    def __init__(self, nom , prenom, adresse):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
    def affichepersonne(self) :
        print(f" Nom: {self.nom} Prenom: {self.prenom}, et adresse : {self.adresse}")

class Adresse :
    def __init__(self,rue,ville,codep):
        self.rue= rue
        self.ville= ville
        self.codep= codep
    def afficheadresse(self) :
        print(f"L'adresse est : {self.rue} - {self.ville} - {self.codep}")

    

adr1= Adresse("5 allee du tour du lac","Clamart",92140)
pers1= Personne("dtx","lucie", adr1)
print(f"{adr1.afficheadresse()} - {pers1.affichepersonne()}")