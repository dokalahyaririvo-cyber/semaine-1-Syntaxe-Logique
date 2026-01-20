# fichier: organisateur_fichiers_simulation.py

import os
import shutil

# définir le dossier à trier
dossier = "C:\\Users\\27dok\\Downloads"
# C:\Users\27dok\Downloads
# créer le journal pour enregistrer les déplacements de fichiers
journal = os.path.join(dossier, "journal.txt")


extensions_mapping = {
	".pdf": "Documents",
	".docx": "Documents",
    ".txt": "Documents",
	".xlsx": "Tableurs",
    ".xlsm": "Tableurs",
	".xls": "Tableurs",
    ".mp4": "Vidéos",
    ".mkv": "Vidéos",
    ".avi": "Vidéos",
	".jpg": "Images",
    ".exe": "logiciels",
	".html": "html",
    ".zip": "Archives",
    ".rar": "Archives",
	".json": "JSON",
	".png": "Images"
}

with open(journal, 'a', encoding='UTF-8') as log:
    log.write("Journal des dépplacemnt de fichiers {} ".format(dossier))
    for nom in os.listdir(dossier):
        chemin_complet = os.path.join(dossier, nom)
        if os.path.isfile(chemin_complet) and nom != "journal.txt":
            _, extension = os.path.splitext(nom)
            dossier_cible = extensions_mapping.get(extension.lower(), "Autres")  # ici j'obtiens le dossier cible par exemple Vidéos ou Documents
            dossier_destination = os.path.join(dossier, dossier_cible) # ici je créer le chemin complet du dossier cible par exemple : F://Dossier/Trié/Vidéos
            # ici je vérifie si le dossier existe sinon je le crée
            os.makedirs(dossier_destination, exist_ok=True) # soit je créer le dossier soit je passe sil il existe déjà. Pour chaque dossie_destination, le makedirs soit il créer via le chemin crée via os.path.join(dossier, dossier_cible), soit il existe déjà via exist_ok =true
            #créer le nouveau chemin de mon fichier
            nouveau_chemin = os.path.join(dossier_destination, nom)
            # déplacer le fichier vers le dossier cible
            shutil.move(chemin_complet, nouveau_chemin)
            log.write("Déplacé : ""{} --> {}\n".format(nom, dossier_cible))
print("Tri terminé. Voir le journal de tri dans 'journal_de_tri.txt'.")
