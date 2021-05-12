#kd oqnbgzhm ehbghdq ztqz tm bncd ozq rtarshstshnm zkogzadshptd: bgzptd kdssqd drs qdlokzbdd ozq tmd ztsqd. tshkhrdq kz eqdptdmbd cdr kdssqdr ontq cdbncdq kd ldrrzfd.

text = input("Votre phrase = ")
tot_of_letters = 0
alphabet = []


for c in text:
    if (c>='a' and c<='z') or (c>='A' and c<='Z'):
        tot_of_letters += 1
"""Compte le total des lettres"""

for x in set(text):
    if (x>='a' and x<='x') or (x>='A' and x<='Z'):
        pourcentage = (text.count(x)/tot_of_letters)*100
        print(x,'=', round(pourcentage,2),'%')
        if x not in alphabet:
            alphabet.append([x,round(pourcentage,2)])
"""Compte le total de lettres différentes et remplit l'alphabet"""

print("\n")    
print("Total de lettres :", tot_of_letters)
print("Total de lettres différentes :",len(alphabet),"\n")
"""Affiche les résultats"""

def twist(text):
    for i in range(len(alphabet)):
        print("Ancienne lettre à remplacer",alphabet[i],"%")
        print(alphabet[i])
        lettre_avant = input()
        print("Nouvelle lettre remplacante")
        lettre_apres = input()
        print(text.replace(lettre_avant,lettre_apres))
        text = (text.replace(lettre_avant,lettre_apres))
"""En comparant avec la fréquence d'aparition des letters en français , remplacer les lettres par celles qu'on pense avoir trouvé EN MAJUSCULES!/ sinon par '?' """
print(text)

twist(text)
"""Mélange les lettres de l'alphabet avec le texte"""