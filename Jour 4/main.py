from  utils import calculate_ttc
montantht = float(input("Entr le montant HT : "))
prixttc = calculate_ttc(montantht)
print("Le montant TTC est de : ", prixttc)
