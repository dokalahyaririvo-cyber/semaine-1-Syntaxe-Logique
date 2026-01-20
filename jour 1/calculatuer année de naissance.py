def main():
    #demander à l'utilisateur l'année actuelle
    année_actuelle_str = (input("Entrez l'année actuelle: "))
    année_actuelle = int(année_actuelle_str)
    # demander à l'utilisateurson age
    age_str =(input("Entrez votre âge: "))
    age = int(age_str)
    #calculer l'année de naissance
    année_de_naissance = année_actuelle - age
    #afficher l'année de naissance
    print("Votre année de naissance est:", année_de_naissance)

if __name__== "__main__":
    main()

