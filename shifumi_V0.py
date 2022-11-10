#Pierre-Feuille-Ciseaux

import random
import time

print ("Bienvenue dans le jeu Pierre-Feuille-Ciseaux")
time.sleep(2)
Nbrmanches = int(input("Veuillez indiquer le nombre de manches(s) gagnante(s) :\n>"))
print("Le nombre de manche(s) est " +str(Nbrmanches))
a = 0
while a < Nbrmanches:
    choix_joueur = int(input("Que voulez-vous jouer?\n 0.Pierre\n 1.Feuille\n 2.Ciseaux\n>"))
    print("Au tour de l'ordinateur de faire son choix")
    time.sleep(2)
    choix_ordi = random.randint(1,3)
    if choix_ordi==1:
        print("L'ordinateur joue la Pierre")
    elif choix_ordi==2:
        print("L'ordinateur joue la Feuille")
    elif choix_ordi==3:
        print("L'ordinateur joue les Ciseaux")

    j = choix_joueur
    o = choix_ordi
    if j==1 and o==1:
        print("Egalité")
    elif j==1 and o==2:
        print("Perdu")
    elif j==1 and o==3:
        print("Gagné")

    if j==2 and o==1:
        print("Gagné")
    elif j==2 and o==2:
        print("Egalité")
    elif j==2 and o==3:
        print("Perdu")

    if j==3 and o==1:
        print("Perdu")
    elif j==3 and o==2:
        print("Gagné")
    elif j==3 and o==3:
        print("Egalité")

    a = a+1

print("Merci d'avoir joué")

