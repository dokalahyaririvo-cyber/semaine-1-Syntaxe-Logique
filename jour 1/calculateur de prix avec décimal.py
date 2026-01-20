def main ():
    # client qui demande le prix d'un produit
    demande = "combien vaut ce produit? "
    print(demande)
    # réponse vendeur
    reponse_vendeur_prix = 1250.75
    print(f"Le prix du produit est de: {reponse_vendeur_prix} Euros")
    print("Le prix du produit est de: ", str(reponse_vendeur_prix), "Euros")
    #quantité voulue par le client
    quantite_voulue_int = 10
    print("j'aimerai en prendre : ", int(quantite_voulue_int))
    print(f"j'aimerai en prendre : {quantite_voulue_int} euros")
    #calcul du prix total hors taxe
    prix_total_ht = reponse_vendeur_prix * int(quantite_voulue_int)
    print("Le prix total hors taxe est de: ", str(prix_total_ht), "Euros")
    print(f"Le prix total hors taxe est de: {prix_total_ht} Euros")
    #calcul de la TVA à 20%
    prix_total = prix_total_ht * 1.20
    print(f"Le prix total TTC est de: {prix_total} Euros")
    print(f"Le prix total TTC est de: {prix_total:.2f} Euros")  # affichage avec 2 décimales   


if __name__ == "__main__":
    main()