def add(a):
    a += 1
    print("Valeur à l'intérieur de la fonction :", a)
    if a < 23 :
        add(a)

add(5)
print("Valeur en dehors de la fonction :", 5)