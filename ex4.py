char=["lala","ok","oui"]

def charlenght(char):
    lenght=[]
    for i in char :
        lenght.append(len(i))
    return lenght

print(charlenght(char))