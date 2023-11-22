fruits=["pomme","banane","orange"]
for i in fruits :
    print(i)
print(len(fruits))
if "pomme" in fruits :
    print("la pomme est dans la liste")
    del fruits[0]
else :
    print("la pomme n'est pas dans la liste")
    
tuple_primarycolors= ("rouge","vert","bleu")
for i in tuple_primarycolors: 
    print(i)
# print (tuple_primarycolors.index("bleu"))
rouge=0
if "rouge" in tuple_primarycolors :
    rouge+=1
    print("il y a ",rouge,"fois rouge dans le tuple")
        
tuple_primarycolors= set(tuple_primarycolors)
print(type(tuple_prymarycolors))

finalfruits=[]
finalfruits.extend(fruits)
for i in finalfruits :
    print(i)
