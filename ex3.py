def checkmail(mail):
    if "@" in mail and "." in mail :
        return "mail valide"
    else :
        return "mail invalide"
mail="lalatest@gaming.ech"
print(checkmail(mail))
