#Début du programme
#Jeu du morpion
#tirer aléatoirement au début du jeu le joueur qui va commencer
import random
#def affichage du tableau de jeu

def afficher_tableau(tableau):
    print("     0)  1)  2)")
    print("   -------------")
    print("0)", end='')
    for i in range(3):
        print(" | "+str(tableau[i]), end='')
    print(" |")
    print("   -------------")
    print("1)", end='')
    for i in range(3):
        print(" | "+str(tableau[i+3]), end='')
    print(" |")
    print("   -------------")
    print("2)", end='')
    for i in range(3):
        print(" | "+str(tableau[i+6]), end='')
    print(" |")
    print("   -------------")
#règle du jeu    
print("Bienvenue dans le jeu du morpion !\n"
      "Les règles du jeu sont simples :\n"
      "Pour gagner, il faut que vous aligner trois de vos symboles :\n"
      "  - Sur une même ligne\n"
      "  - Sur une même colonne\n"
      "  - Sur une même diagonale\n"
      "On peut commencer !\n")
#defintion des noms de joueurs
joueur1 = input ("Veuillez entrer le nom du joueur 1 : ") 
joueur2 = input ("Veuillez entrer le nom du joueur 2 : ")
#on definit l'odre de passage des joueurs
print ("Un tirage aléatoire va avoir lieu pour savoir qui va commencer !")
joueur =  random.choice (['joueur1','joueur2'])
#commencement du jeu  
def tour(tableau, joueur):
    print("C'est à "+str(joueur)+" de jouer ! ")
    colonne=input("Veuillez entrez le numero de la colonne : ")
    ligne=input("Veuillez entrez le numero de la ligne : ")
#afficher la commande joué
    print("Vous avez joué la case ("+colonne+","+ligne+")")
#erreur case déjà joué (veuillez réessayer)
    while tableau[int(colonne)+int(ligne)*3]!=" ":
        afficher_tableau(tableau) 
        print("Cette case est deja jouée ! Saisissez une autre case svp !")
        colonne=input("Veuillez entrez le numero de la colonne : ")
        ligne=input("Veuillez entrez le numero de la ligne : ")
        print("Vous avez joué la case ("+colonne+","+ligne+")")
#affichage des formes dans le tableau ( X et O)
    if joueur==joueur1 :
        tableau[int(colonne)+int(ligne)*3]="X"
    if joueur==joueur2 :
        tableau[int(colonne)+int(ligne)*3]="O"
    afficher_tableau(tableau)
#definition du gagnant (par des conditions)
def gagnant(tableau):
    if (tableau[0]==tableau[1]) and (tableau[0]==tableau[2]) and (tableau[0]!=" "):
        return 1
    if (tableau[3]==tableau[4]) and (tableau[3]==tableau[5]) and (tableau[3]!=" "):
        return 1
    if (tableau[6]==tableau[7]) and (tableau[6]==tableau[8]) and (tableau[6]!=" "):
        return 1
    if (tableau[0]==tableau[3]) and (tableau[0]==tableau[6]) and (tableau[0]!=" "):
        return 1
    if (tableau[1]==tableau[4]) and (tableau[1]==tableau[7]) and (tableau[1]!=" "):
        return 1
    if (tableau[2]==tableau[5]) and (tableau[2]==tableau[8]) and (tableau[2]!=" "):
        return 1
    if (tableau[0]==tableau[4]) and (tableau[0]==tableau[8]) and (tableau[0]!=" "):
        return 1
    if (tableau[2]==tableau[4]) and (tableau[2]==tableau[6]) and (tableau[2]!=" "):
        return 1

#definir l'égalité
def egalite(tableau):
    for i in range(9):
        if tableau[i]==" ":
            return 0
    return 1
 
joueur=joueur1
#symbole pour jouer
print(" - Le joueur 1 possède les | X | \n"
      " - Le joueur 2 possède les | O | \n")
#affiher tableau + boucle while
tableau=[" "," "," "," "," "," "," "," "," "]
afficher_tableau(tableau)
gagne=0
while gagne==0:
    tour(tableau,joueur)
    if  gagnant(tableau):
        print("Le joueur "+str(joueur)+" remporte la partie ! Félicitations !")
        gagne=1
    else:
        if egalite(tableau):
            print("Le tableau est plein ! Il y a égalité !")
            gagne=1
    if joueur==joueur1:
        joueur=joueur2
    else:
        joueur=joueur1
#fin du programme

