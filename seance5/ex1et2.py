class Ville():
    def __init__(self, nom, dep, reg, nbhab,):
        self.nom= nom
        self.dep= dep
        self.reg= reg
        self.nbhab= nbhab
        print(f"la ville {nom} est dans le departement {dep} de la region {reg} et a {nbhab} habitants")
        
paris= Ville("Paris", 75, "Ile-de-France", 15000)

