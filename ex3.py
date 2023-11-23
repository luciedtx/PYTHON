def checkmail(mail):
    if "@" in mail and "." in mail :
        return "mail valide"
    else :
        return "mail invalide"
mail="lalatestming.ech"
print(checkmail(mail))
