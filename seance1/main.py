# EX1
# nom=str("Lucie,")
# age=int(18)
# taille=float(1.68)
# print(nom,age,"ans",taille,"cm")

# EX2
# givenumber=float(input("Entrez un nombre :"))
# if givenumber==0 :
#     print("Nombre Nul")
# elif givenumber<0 :
#     print("Nombre négatif")
# else :
#     print("Nombre positif")

# EX3 donne la nature du triangle selon la longueur de ses cotés
# longueur1=float(input("donner une longueur d'un cote du triangle : "))
# longueur2=float(input("donner une deuxieme longueur d'un cote du triangle : "))
# longueur3=float(input("donner une toisieme longueur d'un cote du triangle : "))

# if longueur1 == longueur2 and longueur2 == longueur3 :
#     print("Le triangle est équilatéral.")
# elif longueur1==longueur2 or longueur1==longueur3 or longueur2==longueur3 :
#     print("Le triangle est isocèle.")
# else :
#     print("Le triangle est scalène.")

# EX4 convertisseur de cm vers pouces et de pouces vers cm
# ask=str(input("Convertir de pouces vers cm ou cm vers pouces ?"))
# if ask=="pouces vers cm":
#     pouce=int(input("entrez la valeur en pouce : "))
#     print(pouce,"pouces font",pouce*2.54,"cm")
# elif ask=="cm vers pouces":
#     cm=float(input("entrez la valeur en cm :"))
#     print(cm,"cm font",cm/2.54,"pouces")
# else :
#     print("veuillez répondre au formulaire.")

# Boucle while
# chiffre=0 
# while chiffre<10:
#     chiffre +=1
#     if chiffre==5:
#         continue #saute la condition et continue la boucle
#        #break #sort de la boucle
#     print(chiffre)
# print("fin de la boucle")

# # Boucle for
# # Cas ou on a 1 argument
# for i in range(11):
#     print(i)
# #Cas ou on a 2 arguments
# for i in range(1,11):
#     print(i)
# #Cas ou on a 3 arguments
# for i in range(2,11,2):  #for i in(debut,fin non inclue,pas):
#     print(i)

# EX6 pyramide de symboles centrés
# symbole=" $ "
# taille=10
# for i in range(0,taille,2):
#     for j in range(-11, -i):
#         print("", end=" ")
#     for k in range(i+1):
#         print(symbole, end="")
#     print()

# EX7
import random

quiz=int(input("participer au quiz?\n Oui : tapez 1\n Non : tapez 2\n"))
if quiz==2:
    print("Au revoir !")
else :
    score=0
    for i in range(6) :
        nb1=random.randint(0,100)
        nb2=random.randint(0,100)
        list=["+","-","*"]
        ope=random.choice(list)
        calcul=nb1, ope, nb2
        print(f"{calcul[0]} {calcul[1]} {calcul[2]}")
        reponse = int(input("Quel est le résultat de ce calcul ? "))
        
        if ope == "+":
            resultat_attendu = calcul[0] + calcul[2]
        elif ope == "-":
            resultat_attendu = calcul[0] - calcul[2]
        elif ope == "*":
            resultat_attendu = calcul[0] * calcul[2]
        if reponse == resultat_attendu:
            print("Bonne réponse")
            score += 1
        else:
            print("Mauvaise réponse")

    # Ajoutez un if pour les appréciations par rapport au score final
    if score<=4 :
        print("Votre score est de", score, "/6. C'est pas un tres bon score. Courage ")
    elif score>=5 and score<8 :
        print("Votre score est de", score, "/6. C'est un bon score. Continuez comme ça ")
    else :
        print("Votre score est de", score, "/6. C'est un tres bon score ! Bravo ")
        



