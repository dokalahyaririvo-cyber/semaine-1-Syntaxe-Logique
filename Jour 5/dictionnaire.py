import json
# charger notre classe depuis un fichier
with open('eleve.json', 'r') as file:
    eleves =json.load(file)

chalenge=input("Qu'est ce que vous voulez faire : " \
"1- Afficher la note d’un éléve "
"2- Affiche toute les appréciations de la classe entière" \
"3- Ajouter un nouvel éléve avec une note et une appréciation " \
"4- Rétirer une eleve de la classe :")

if chalenge == "1" :
    name=input("Entrerlenom de l'élève:")
    print("La note de {} est : {}".format(name, eleves[name]["note"]))
elif chalenge == "2" :
    print("voici toute les appréciations de la classe entière :")
    for eleve in eleves:
        print("{} : {}".format(eleve, eleves[eleve]["appréciation"]))
elif chalenge == "3" :
    name=input("Entrer le nom de l'élève à ajouter:")
    note=int(input("Entrer la note de l'élève à ajouter : "))
    appreciation = input ("Entrer l'appréciation de l'élève à ajouter : ")
    eleves[name] = {'note': note, 'appréciation': appreciation}
    with open('eleve.json', 'w') as file:
        json.dump(eleves, file)
        print("{} a  été ajouté à la classe.".format(name))
elif chalenge == "4" :
    name =input("Entrer le nom de la personne à retirer : ")
    if name in eleves :
        del eleves[name]
        with open('eleve.json', 'w') as file:
            json.dump(eleves, file)
            print("{} a été retiré de la classe.".format(name))