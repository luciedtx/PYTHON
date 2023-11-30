import json
chemin="seance7/ex2/fichier.json"

# lit et affiche le contenu du fichier JSON.
def lirejson(chemin):
    with open(chemin,"r") as f:
        content=json.load(f)
    
    print(content)

# 3. Modifiez la fonction pour rechercher et afficher des informations
# spécifiques sur un produit.

# 4. Écrivez une fonction ajouter_produit_json(nom_fichier,
# nouveau_produit) qui ajoute un nouveau produit au fichier JSON.
def ajouter_produit_json(chemin,nouveau_produit):
    with open(chemin,"r") as f : 
        content=json.load(f) #on lit d'abord le fichier json
 
    content.append(nouveau_produit) #on ajoute le contenu

    with open(chemin,"w") as f :
        json.dump(content,f, indent=4) #on implemente le contenu au fichier

lirejson(chemin)    
ajouter_produit_json(chemin,{"nom":"Fromage", "prix": 3,"quantite": 2 })