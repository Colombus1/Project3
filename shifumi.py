#!/usr/bin/python
# coding: utf-8


# Le premier vrai code en Python
# Jeu python Shifumi

#On importe la librairie
import random

#On défini la fonction permettant de savoir le nombre de manches sans se tromper
def manches(reponse_manche, NbrManches):
    # print(reponse_manche)
    while reponse_manche == 'n':
       NbrManches = input("\nCombien de manches voulez-vous jouer ?\n")
       reponse_manche = input('Le nombre de manches est de ' + NbrManches + ' êtes-vous sur ? (y/n)')
    
    else :
       print('Le premier en ' + NbrManches + ' manches gagnées, gagne la partie !')

# DEBUT
print ("\n Bonjour et bienvenue dans le Shifumi !")
print ("\n Voulez-vous jouez à 2 (1) ou contre l'ordi (2) ?")

x = input()
if int(x) == 1:
    print ("\nVous avez décidé de jouer contre quelqu'un d'autre !")
    Joueur1 = input("\nQuel est le nom du premier joueur ?\n")
    Joueur2 = input("\nQuel est le nom du deuxième joueur ?\n")
    print ("ok c'est un match entre " + Joueur1 + " et " + Joueur2)
    
    #On choisis le nombre de manches
    NbrManches = input("\nCombien de manches voulez-vous jouer ?\n")
    reponse_manche = input('Le nombre de manches est de ' + NbrManches + ' êtes-vous sur ? (y/n)\n')
    #On appelle la fonction manche
    
    manches(reponse_manche, NbrManches)

    #score des joueurs mis a 0 à chaque nouvelle partie
    score_joueur1 = 0
    score_joueur2 = 0

    # i permettant de dire si les manches ont été toutes faites
    i = 0
    while i < int(NbrManches):
        print(Joueur1 + " 1: pierre 2: papier 3: ciseau ")
        choix_joueur1 = input()
        print(Joueur2 + " 1: pierre 2: papier 3: ciseau ")
        choix_joueur2 = input()

        if int(choix_joueur1) == 1 and int(choix_joueur2) == 2:
            print(choix_joueur1)
            print('En effet le papier gagne contre la pierre ' + Joueur2 + ' vous avez gagné !')
            score_joueur2 += 1
            print('Le score de ' + Joueur2 + ' est de ' + str(score_joueur2) + '\n' + Joueur1 + ' votre score est de ' + str(score_joueur1))
        elif int(choix_joueur1) == 2 and int(choix_joueur2) == 1:
            print('En effet le papier gagne contre la pierre ' + Joueur1 + ' vous avez gagné ')
            score_joueur1 += 1
            print('Le score de ' + Joueur1 + ' est de ' + str(score_joueur1) + '\n' + Joueur2 + ' votre score est de ' + str(score_joueur2))
       
        if int(choix_joueur1) == 1 and int(choix_joueur2) == 3:
            print('En effet la pierre gagne contre le ciseau ' + Joueur1 + ' vous avez gagné ')
            score_joueur1 += 1
            print('Le score de ' + Joueur1 + ' est de ' + str(score_joueur1) + '\n' + Joueur2 + ' votre score est de ' + str(score_joueur2))
        elif int(choix_joueur1) == 3 and int(choix_joueur2) == 1:
            print('En effet la pierre gagne contre le ciseau ' + Joueur2 + ' vous avez gagné ')
            score_joueur2 += 1
            print('Le score de ' + Joueur2 + ' est de ' + str(score_joueur2) + '\n' + Joueur1 + ' votre score est de ' + str(score_joueur1))
        
        if int(choix_joueur1) == 2 and int(choix_joueur2) == 3:
            print('En effet le ciseau gagne contre le papier ' + Joueur2 + ' vous avez gagné ')
            score_joueur2 += 1
            print('Le score de ' + Joueur2 + ' est de ' + str(score_joueur2) + '\n' + Joueur1 + ' votre score est de ' + str(score_joueur1))
        elif int(choix_joueur1) == 3 and int(choix_joueur2) == 2:
            print('En effet le ciseau gagne contre le papier ' + Joueur1 + ' vous avez gagné ')
            score_joueur1 += 1
            print('Le score de ' + Joueur1 + ' est de ' + str(score_joueur1) + '\n' + Joueur2 + ' votre score est de ' + str(score_joueur2))
        
        # itération pour les manches
        i += 1

    if score_joueur1 > score_joueur2:
        print(Joueur1 + " a gagné la partie")
    else :
        print(Joueur2 + " a gagné la partie")

# JOUEUR CONTRE ORDI
elif int(x) != 1:
    print ("\nVous avez décidé de jouer contre l'ordi !")
    Joueur = input("\nQuel est le nom du joueur ?\n")
    print ("ok c'est un match entre " + Joueur + " et L'ordi" )

    NbrManches = input("\nCombien de manches voulez-vous ?\n")
    reponse_manche = input('Le nombre de manches est de ' + NbrManches + ' êtes-vous sur ? (y/n)\n')
    
    #On appelle la fonction manche
    manches(reponse_manche, NbrManches)

    #Score des joueurs mis à 0 à chaque nouvelle partie
    score_joueur = 0
    score_ordi = 0
        
    i = 0
    while i < int(NbrManches):
        print(Joueur + " 1: pierre 2: papier 3: ciseau ")
        choix_joueur = input()
        choix_ordi = random.randint(1,3)

        if int(choix_joueur) == 1 and choix_ordi == 2:
            print('En effet le papier gagne contre la pierre l\ordinateur a gagné !')
            score_ordi += 1
            print('Le score de l\'ordi est de ' + str(score_ordi) + '\n' + Joueur + ' votre score est de ' + str(score_joueur))
        elif int(choix_joueur) == 2 and choix_ordi == 1:
            print('En effet le papier gagne contre la pierre ' + Joueur + ' vous avez gagné §')
            score_joueur += 1
            print('Le score de ' + Joueur + ' est de ' + str(score_joueur) + '\n Ordi votre score est de ' + str(score_ordi))
       
        if int(choix_joueur) == 1 and choix_ordi == 3:
            print('En effet la pierre gagne contre le ciseau ' + Joueur + ' vous avez gagné ')
            score_joueur += 1
            print('Le score de ' + Joueur + ' est de ' + str(score_joueur) + '\n Ordi votre score est de ' + str(score_ordi))
        elif int(choix_joueur) == 3 and choix_ordi == 1:
            print('En effet la pierre gagne contre le ciseau ' + Joueur2 + ' vous avez gagné ')
            score_ordi += 1
            print('Le score de l\'ordi est de ' + str(score_ordi) + '\n' + Joueur + ' votre score est de ' + str(score_joueur))
        
        if int(choix_joueur) == 2 and choix_ordi == 3:
            print('En effet le ciseau gagne contre le papier l\'ordi vous avez gagné ')
            score_ordi += 1
            print('Le score de l\'ordi est de ' + str(score_ordi) + '\n' + Joueur + ' votre score est de ' + str(score_joueur))
        elif int(choix_joueur) == 3 and choix_ordi == 2:
            print('En effet le ciseau gagne contre le papier ' + Joueur + ' vous avez gagné ')
            score_joueur += 1
            print('Le score de ' + Joueur + ' est de ' + str(score_joueur) + '\n Ordi votre score est de ' + str(score_ordi))
        
        # itération pour les manches
        i += 1

    if score_joueur > score_ordi:
        print(Joueur + " a gagné la partie")
    else :
        print(Joueur2 + " a gagné la partie")    

# PERSONNE NE VEUT JOUER LE PROGRAMME SE FINIT
else : 
    print('Bye Bye !')

# FIN
