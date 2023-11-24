import random

mots= ["bonjour", "salut", "enchanté", "coucou", "hello", "hey"] #mettre des mots de meme longueur
guess= random.choice(mots)

# fonction pour afficher le mot caché
def hide(guess):
    hidden= ['-'] * len(guess)
    return hidden
hidden= hide(guess)
print(hidden)
totalTries = 6
for try_ in range(totalTries) :

    userguess=input(f"Devinez le mot du jour ({len(guess)}): ")

    for i in range(len(userguess)) :
        if userguess[i] in guess : #si lettre a l'indice i est dans le mot
            if userguess[i] == guess[i]: # si la lettre indice i == lettre indice i du mot
                hidden[i]=userguess[i] #on garde la lettre au bon emplacement
            else :
                print(f"Lettre correcte mais pas au bon (indice {i})")
        else : 
            print(f"La lettre n'est pas dans le mot.(indice {i})")
    print(hidden)

    # print(totalTries - try_ - 1)    
    # sinon on 'garde pas la lettre'


# ajt un truc pr arreter le programme quand on a trouver la bonne réponse!

# for char in userguess :
#     if char in guess :
#         result.append(char)
#         break
#         print(result,"\nLe mot était bien",guess," bien joué")
#     else :
#         print("La lettre est incorrecte !")
#         break












# def wordle(mots):
#     result=[]
    
    

#     for i in userguess :
#         if userguess[i]==guess[i] :
#             result.append[userguess[i]]
#         elif userguess[i] in guess :
#             print("La lettre est bonne mais mal positionnée")
#         else :
#             print("Lettre incorrecte")

#     return result

# print(wordle(mots))


