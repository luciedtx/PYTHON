# Les exceptions
var1= 10
var2= 0
try :
    print(var1/var2)
except ZeroDivisionError :
    print("division par zero impossible")
except TypeError :
    print("Votre variable n'est pas un nombre")
except Exception as e:
    print(e) #renvoie l'erreur exacte
else :
    print(var1/var2)
finally :
    print("Division terminée.")

# Les listes
list= [1,2,3,4]
print(list[0],len(list)) #len renvoie la longueur de la liste
list.append("bonjour") #ajoute un element en fin de liste
print(list)
list.insert(2,"coucou") #ajoute un element a l'index donné
print(list)
list.pop() #retire le dernier element de la liste
del list[2] #retire l'element a l'index donné
print(list)
list.remove(4) #enleve l'element donné 
print(list)
list.reverse()    #inverse la liste
# reversed(list)  #autre maniere sans modifier la liste
# list[::-1]       #autre maniere sans modifier la liste
print(list)
for i in list : # affiche chaque element de la liste
    print(i)
if 2 in list:   #verifier qu'un element est dans la liste
    print("2 est dans la liste")
if "coucou" in list:  
    print("coucou est dans la liste")
else :
    print("coucou n'est pas dans la liste")

#  Les tuples : on ne peut pas modifier la taille
tuple_name= ("Joel","Francis","Louis","Francis","Guillaume")

# Les sets
set_name= {"Joel","Francis","Louis","Guillaume"}

# Les dictionnaires
dictionnaire = {"Joel":18,
                "Francis": 20,
                "Louis": 25,
                "Guillaume": 30 }
print(len(dictionnaire))
print(dictionnaire["Joel"]) #affiche la valeur de la clé
del dictionnaire["Guillaume"] #supprime un element du dictionaire
dictionnaire["Francis"]= 45
dictionnaire["Michelle"]=60 #nouvelle valeur ajoutée 
for i in dictionnaire.values():
    print(i)
for i in dictionnaire.keys(): #
    print(i, dictionnaire[i])
for key, value in dictionnaire.items(): #afficher les clés et leurs valeurs
    print(key, value)