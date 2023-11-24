
def nombrevoy(phrase):
    compteur=0
    for char in phrase :
        if char in "AEIOUYaeiouy" :
            compteur+=1
    return compteur
phrase = "bonjour hello"
result = nombrevoy(phrase)
print(f"la phrase {phrase} contient {result} voyelles")



