# class Eleve:

    # nom = "Jean"
    # age = 20
    # note = 12
    # def __str__(self):
    #     return "voici ma classe Eleve"
    # def __init__(self, nom, age, note): #initialise les valeurs par défaut
    #     self.nom= nom
    #     self.age= age
    #     self.note= note
    
    # def __del__(self): #detruit les données (auto en python car il y a le garbage collector)
    #     print("je suis le destructeur")
        
    # def moyenne(self):
    #     return f"la note de {self.nom} est {self.note}"
    

# eleve1= Eleve()
# eleve1.nom= "john"
# eleve1.age= 18

# eleve2= Eleve("Henri",10,13)
# print(f"{eleve2.nom} a {eleve2.age}ans et a une note de {eleve2.note}")

# print(Eleve())
class Telephone :
    def __init__(self, marque, modele):
        self.marque= marque
        self.modele= modele
    stock=50
    @classmethod #decorateur permet de cumuler en precisant que vente_tel est une methode de classes et non d'instances
    def vente_tel(cls, vente):
        cls.stock -= vente
        print(f"il reste {cls.stock} telephones en stock")
    # vente_telephone= classmethod(vente_tel) #autre methode pour cumuler
    @staticmethod #independante de la classe et de l'instance
    def bestseller(vente):
        if vente >=5 :
            print("C'est un best seller")
        else :
            print("Encouragement")
tel1= Telephone("Apple","Iphone 12")
tel1.vente_tel(2)
tel1.bestseller(2)

tel2= Telephone("Samsung","Galaxy S22")
tel2.vente_tel(5)
tel2.bestseller(5)

# encapsulation : droit d'acces a un attribut; public private protected
class Francais():
    def __init__(self, _nom, _prenom, _secusociale) : # _x =privé
        self._nom= _nom
        self._prenom= _prenom 
        self._secusociale= _secusociale 
    # Accesseurs
    def get_nom(self): #getter : recupere le nom 
        return self._nom
    def set_nom(self,_nom): #setter : modifie le nom
        self._nom = _nom
        return self._nom