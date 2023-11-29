class Adresse :
    def __init__(self,rue,ville,codep):
        self.rue= rue
        self.ville= ville
        self.codep= codep
        print(f"{self.rue} - {self.ville} - {self.codep}")

        def get(self):
            return self._type
        def set_type(self, _type):
            self._type= _type

adr1= Adresse("5 allee du tour du lac","Clamart",92140)

# Modifiez la classe Personne pour inclure un objet Adresse.(ex2)