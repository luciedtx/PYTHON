from main import Francais

fr1= Francais("albert", "Jean-Marc", 123456789)
print(fr1._nom)

print(fr1.get_nom()) #recupere et renvoie le nom 
print(fr1.set_nom("Julien")) #modifie le nom