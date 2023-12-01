chemin= "seance7\ex1\donnees.txt"


def lire_fichier(chemin):

    # lire le contenu du fichier
    with open(chemin,"r") as f:
        content= f.read()
    # afficher le contenu du fichier
    print(content)

# ajouter du contenu au fichier
with open(chemin,"a") as f :
    f.write("\nVoici une nouvelle ligne de donnees\nEn voila une autre\n")



def ecrire_fichier(chemin, contenu):
    # prendre un contenu en parametre et l'ajouter au fichier    
    with open(chemin,"a", encoding="utf-8") as f: 
        f.write(contenu)

lire_fichier(chemin)
ecrire_fichier(chemin,"Un parametre pour ajouter des données")



