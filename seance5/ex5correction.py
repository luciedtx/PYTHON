class Personne():
    nom= "Lucie"
    age= 18
    def details(self):
        print(f"Bonjour je suis {self.nom} et j'ai {self.age}")


    def get_nom(self): 
        return self._nom
    
    def set_nom(self,_nom): 
        self._nom = _nom
    
    def get_age(self): 
        return self._nom
    
    def set_age(self,_age): 
        self._age = _age
    
    @classmethod
    def implemente(cls, _chaine):
        nom,age = _chaine.split("-")
        return(cls(nom,(int(age))))
    
    
    # exo 7 correction de antoine
    # @staticmethod
    # def genereID(longueurID : int) -> str:
    #     return "".join(rdm.choices(string.ascii_letters,k=longueurID))
    
    # def __str__(self) -> str:
    #     return f"{self.nom} a {self.age} ans"
    
    # def __eq__(self, other: Self) -> bool:
    #     return other.nom == self.nom and other.age == self.age