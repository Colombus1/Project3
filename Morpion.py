# # -*- coding: utf-8 -*-
# # Tic Tack Toe
import os
from time import sleep 

# Création de la grille de jeu
def newBoard():
    board = [' ', ' ', ' ',
             ' ', ' ', ' ',
             ' ', ' ', ' ']
    return board

#  affichage de la grille et de quel nombre jouer
def displayBoard(board):
    print(board[0], '|', board[1], '|', board[2], '     1 | 2 | 3')
    print('--+---+--', '     --+---+--')
    print(board[3], '|', board[4], '|', board[5], '     4 | 5 | 6')
    print('--+---+--', '     --+---+--')
    print(board[6], '|', board[7], '|', board[8], '     7 | 8 | 9')

#  fonction des tours des joueurs 
def play(player, board):

    print("\nAu joueur ", player, " de jouer")
    answer = int(input('En quelle case voulez-vous jouer: '))
    while (answer <= 0 or answer >= 10 or board[answer - 1] != ' '):
        print("La case n'est pas valide")
        answer = int(input('En quelle case voulez-vous jouer: '))
    board[answer - 1] = player
    return board

#  Les coups gagnant
combosWin = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

# fonction pour détecter qui gagne 
def detectWIN(board):
    global combosWin
    for i in range(0, len(combosWin)):
        if (board[combosWin[i][0]] == board[combosWin[i][1]] and board[combosWin[i][1]] == board[combosWin[i][2]] and
                board[combosWin[i][0]] != ' '):
            displayBoard(board)
            print('\nLe joueur', board[combosWin[i][0]], 'gagne la partie !')
            return True
    return False

# fonction principale
def main():
    print("Bienvenue sur le morpion !\n")
    board = newBoard()
    rounds = 0
    while True:  # boucle infinie
        displayBoard(board)
        if (rounds % 2 == 0):  # un coup sur deux
            play("X", board)
        else:
            play("O", board)
        if (detectWIN(board)):
            break

        rounds += 1
        if (rounds == 9):  # tout est rempli mais pas de win donc match nul
            displayBoard(board)
            print('\nMatch nul !!!')
            break

main()

#  Game restart
answer = str(input("\nVoulez-vous recommencer: "))
while (answer.lower() == "oui"):
    print('\n\n\n\n\n--- NOUVELLE PARTIE --- \n')  # saut de lignes
    main()
    answer = str(input("\nVoulez-vous recommencer: "))
