from random import shuffle
chaine = input("Entrez une chaîne de mot séparér pas des espaces comme ceci (Je suis heureux) : ").split(" ")
print(chaine)
shuffle(chaine)
print(chaine)
if len(chaine) < 10  :
    print("Voici les deux premiers mots de la chaine mélangé : {} {}".format(chaine[0], chaine[1]))
elif len(chaine) >= 10 :
    print("Voici les trois derniers mots de la chaine mélangé : {} {} {}".format(chaine[-3], chaine[-2], chaine[-1]))