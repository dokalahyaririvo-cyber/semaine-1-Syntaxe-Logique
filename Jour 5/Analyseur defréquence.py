texte = input("Entrez un texte : ")
frequency = {}

for caractere in texte.lower():
    if caractere.isalpha(): # On ne garde que les lettres
        # Astuce : .get(clé, 0) permet d'éviter l'erreur si la clé n'existe pas encore
        frequency[caractere] = frequency.get(caractere, 0) + 1

print("\n--- Analyse de Fréquence ---")
# On trie par ordre alphabétique des clés
for lettre, count in sorted(frequency.items()):
    # Astuce visuelle : on affiche des étoiles pour faire un graphique
    graphique = "*" * count 
    print(f"{lettre} : {count} {graphique}")