chemin= "seance7/ex1/donnees.txt"


def lire_fichier(nom_fichier):

    # lire le contenu du fichier
    with open(chemin,"r") as f:
        content= f.read()
    # afficher le contenu du fichier
    print(content)

# ajouter du contenu au fichier
with open(chemin,"a") as f :
    f.write("\nVoici une nouvelle ligne de donnees\nEn voila une autre\n")



def ecrire_fichier(nom_fichier, contenu):
    contenu="Un parametre pour ajouter des donnees"
    # prendre un contenu en parametre et l'ajouter au fichier    
    with open(chemin,"a") as f:
        f.write(contenu)