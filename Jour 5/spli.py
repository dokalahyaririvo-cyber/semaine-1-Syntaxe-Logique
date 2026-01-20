text = input("Enter a text sous cette forme (manger-tres-bien) : ").split("-")
print("The splitted text is :", text)
print("Salut {}".format(text[1]), "voici ton email : {}".format(text[0]), "et voici ton mot de passe : {}".format(text[2]))