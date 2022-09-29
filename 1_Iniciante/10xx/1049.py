palavra1 = input()
palavra2 = input()
palavra3 = input()
classif = ""

if(palavra1 == "vertebrado"):
    if(palavra2 == "ave"):
        if(palavra3 == "carnivoro"):
            classif = "aguia"
        elif(palavra3 == "onivoro"):
            classif = "pomba"
    elif(palavra2 == "mamifero"):
        if(palavra3 == "onivoro"):
            classif = "homem"
        elif(palavra3 == "herbivoro"):
            classif = "vaca"
elif(palavra1 == "invertebrado"):
    if(palavra2 == "inseto"):
        if(palavra3 == "hematofago"):
            classif = "pulga"
        elif(palavra3 == "herbivoro"):
            classif = "lagarta"
    elif(palavra2 == "anelideo"):
        if(palavra3 == "hematofago"):
            classif = "sanguessuga"
        elif(palavra3 == "onivoro"):
            classif = "minhoca"
            
print(classif)