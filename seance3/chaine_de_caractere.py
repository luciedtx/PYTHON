chaine_de_caractere1= "j'aime \n le python" 
chaine_de_caractere2= "le python c'est cool" #\t pour tabulation \n saut de ligne \b backspace

# print(chaine_de_caractere1, chaine_de_caractere2)

# for i in chaine_de_caractere1 :
#     print(i)

print(chaine_de_caractere1[8:10])
print(chaine_de_caractere2[3:9].upper()) # .upper = maj .lower = min

print(chaine_de_caractere2.replace("python","javascript"))
print(chaine_de_caractere1.split()) #str en list

list=["le","php","est","génial"]

chaine= " ".join(list) #list en str

print(chaine)
print(chaine_de_caractere2.partition("c'est"))
print(chaine_de_caractere1.index("e")) #afficher l'index
print(chaine_de_caractere1.find("le"))

list1=[1,2,3,4]
list2= list1
print(list1 is list2)

nom= "Hypolite"
prenom= "Jean-Sébastien"
age= 20
chaine2= f"je m'appelle {nom} {prenom} et j'ai {age}ans"
print(chaine2)
chaine3= "je m'appelle {0} {1} et j'ai {2}ans".format(nom,prenom,age)
print(chaine3)

def presentation(nom):
    print(f"je m'appelle {nom}")

presentation("Jean")

def presentation2(nom,age):
    return f"je m'appelle {nom} et j'ai {age}ans"

print(presentation2("Lucie",18))

def addition(*args):
    somme=0
    for arg in args:
        somme+=arg
    return somme
print(addition(1,5,8,4,2,4))

def nom_d(*noms):
     for nom in noms:
        print(f"je m'appelle {nom}")
nom_d("alfred","william","jack","joe")

def semaine(**kwargs):
    print(kwargs)
semaine(jour1="lundi",jour2="mardi")

# def carre(x):
#     return x*x
carre= lambda x: x*x
print(carre(3))