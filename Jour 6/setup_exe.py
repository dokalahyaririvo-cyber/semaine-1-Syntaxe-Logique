"""
Script pour créer un fichier .exe de l'Organisateur de Fichiers
Utilise PyInstaller pour compiler l'application en un exécutable Windows
"""

import PyInstaller.__main__
import os

# Chemin du script principal
script_path = 'Organisateur_GUI.py'

# Configuration de PyInstaller
PyInstaller.__main__.run([
    script_path,
    '--name=OrganisateurFichiersPro',
    '--onefile',  # Un seul fichier exe
    '--windowed',  # Pas de console (GUI uniquement)
    '--icon=NONE',  # Pas d'icône pour l'instant (vous pouvez en ajouter une)
    '--add-data=config_organisateur.json;.' if os.path.exists('config_organisateur.json') else '',
    '--clean',  # Nettoyer le cache avant de compiler
    '--noconfirm',  # Remplacer sans demander
])

print("\n" + "="*60)
print("✅ Fichier .exe créé avec succès!")
print("📁 Emplacement: dist/OrganisateurFichiersPro.exe")
print("="*60)
