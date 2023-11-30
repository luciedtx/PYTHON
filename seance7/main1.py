import json

# chemin_absolu= "C:/Users/ldoutriaux/Documents/PYTHON-2/seance7/fichier1.txt"
# chemin_relatif= "seance7/fichier1.txt"
# f= open(chemin_relatif, "r") # open(fichier,droits), ici r = read
# lire= f.read()
# print(lire)
# f.close() # si on utilise pas la methode with car elle ferme automatiquement le fichier
# with open(chemin_relatif, "r") as f :
    # contenu= f.read() #lis le fichier 
    # contenu= repr(f.read()) #ajoute des \n
    # contenu= f.readlines() #met en liste avc des \n
    # contenu= f.read().splitlines() #met en liste sans les \n 

# print(contenu)

#  ajt des elements dans un fichier
# with open(chemin_relatif,"a") as f : #ouvrir en append
#     f.write("\nJe confirme que le python est cool\n") 

# with open(chemin_relatif,"r") as f :
#     lecture= f.read() #lire les 10 premier caracteres

#     print(lecture)
#     f.seek(0) #repete deux fois car curseur à 0
#     lecture2= f.read()
#     print(lecture2)
cheminjson1="seance7/fichier1.json"
cheminjson= "seance7/fichier2.json"
with open(cheminjson,"w") as f : #ouvrir en write
    json.dump([10,20,30,40],f, indent= 4) # .dump(ce qu'on ajoute, le fichier)
    
with open(cheminjson1,"r") as f : #ouvrir en read
    content=json.load(f) #lire un fichier json

    
print(content)

content.append({"nom":"Laroche", "prenom":"Alice","age":19})

with open(cheminjson1,"w") as f :
    json.dump(content,f, indent=4)

