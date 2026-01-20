from statistics import mean
from random import shuffle
notes = [2, 8, 15, 12, 4, 10, 20, 45]
print("La liste des notes est : {}".format(notes))
shuffle(notes)
print("La liste des notes mélangée est : {}".format(notes))

moyenne = mean(notes)
print("La moyenne de la liste est : {}".format(moyenne))
