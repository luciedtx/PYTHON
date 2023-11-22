# 1. Ajouter un élément à la liste de courses 
# 2. Retirer un élément de la liste de courses 
# 3. Afficher les éléments de la liste de courses 
# 4. Vider la liste de courses 
# 5. Quitter le programme 

courses=[]

while True:
    print("\nMenu :")
    print("1. Ajouter un élément à la liste de courses")
    print("2. Retirer un élément de la liste de courses")
    print("3. Afficher les éléments de la liste de courses")
    print("4. Vider la liste de courses")
    print("5. Quitter le programme")

    try :
        choice=int(input("Quel est votre choix ?\n"))
    except ValueError:
        print("Veuillez entrer un nombre entier.")
        continue  # Revenir au début de la boucle
    if choice==1 :
        ajt=str(input("Que souhaitez vous ajouter à la liste de courses : "))
        courses.append(ajt) 
        print(courses)
    elif choice==2 :
        retirer=str(input("Quel élément souhaitez vous retirer : "))
        courses.remove(retirer)
        print(courses)
    elif choice==3 :
        print("Voici votre liste de courses :")
        for i in courses:
            print(i)
    elif choice==4 :
        print("La liste de course est désormais vide.")
        courses.clear()
        print(courses)
    elif choice==5 :
        print("Au revoir !")
        break
    





