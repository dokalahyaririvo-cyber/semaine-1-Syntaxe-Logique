stock={
    "pommes": 50,
    "bananes": 30,
    "oranges": 20,
    "Mangues": 15,
    "Ananas": 10
}

print("Stock initial :", stock)

produit = input("Entrez le nom du produit à ajouter au stock : ")
quantite = int(input("Entrez la quantité à ajouter : "))

stock[produit] = stock.get(produit, 0) + quantite

print("Stock mis à jour :")
for produit, quantite in stock.items():
    print(f"{produit}: {quantite}")

for produit in list(stock.keys()):
    if produit == 'a voir':
        del stock[produit]

for produit, quantite in stock.items():
    print(f"{produit}: {quantite}")