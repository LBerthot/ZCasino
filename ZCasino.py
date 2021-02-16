# -*-coding:Latin-1 -*

import os
from random import randrange
from math import ceil

continuer_partie = True

# S�lection du solde de d�part
solde = -1
while solde <= 0:
    solde = input("Quelle est votre solde de d�part? ")
    try:
        solde = int(solde)
    except ValueError:
        print("Vous n'avez pas saisi de solde.")
        solde = -1
        continue
    if solde < 1:
        print("Vous ne pouvez pas d�marer avec un solde n�gatif.")
print("Vous commencez la partie avec", solde, "$.")


while continuer_partie == True:

    # Selection du num�ro
    nb = -1
    while nb < 0 or nb > 49:
        nb = input("Choisissez un num�ro compris de 0 � 49 :")
        try:
            nb = int(nb)
        except ValueError:
            print("Vous n'avez pas saisi de num�ro.")
            nb = -1
            continue
        if nb < 0:
            print("Vous avez saisi un num�ro n�gatif.")
            nb = -1
        if nb > 49:
            print("Vous avez saisi un num�ro sup�rieur � 49.")
            nb = -1

    # Selection de la mise
    mise = -1
    while mise <= 0 or mise > solde:
        mise = input("Combien misez-vous? ")
        try:
            mise = int(mise)
        except ValueError:
            print("Vous n'avez pas mis�.")
            mise = -1
            continue
        if mise <= 0:
            print("Vous avez saisi une mise n�gative.")
            mise = -1
        if mise > solde:
            print("Vous avez", solde, "$. Vous ne pouvez pas miser plus.")

    # Tirage et r�sultat
    nb_tire = randrange(50)
    print("Le num�ro tir� au hasard est le", nb_tire)
    if nb == nb_tire:
        print("Les deux num�ros sont identiques. Vous gagnez", 3 * mise, "$!")
        solde += 3 * mise
    elif (nb % 2 == 0 and nb_tire % 2 == 0) or (nb % 2 == 1 and nb_tire % 2 == 1):
        print("Les deux num�ros sont de la m�me couleur. Vous gagnez", ceil(0.5 * mise), "$!")
        solde += ceil(0.5 * mise)
    else:
        print("Perdu! Les deux num�ros sont diff�rents et n'ont pas la m�me couleur.")
        solde -= mise

    # Condition d'arret de partie
    if solde <= 0:
        print("Votre solde est de 0, veuillez rejouer une prochaine fois.")
        continuer_partie = False
    else:
        print("Vous avez ", solde, "$.")
        quitter = input("Souhaitez-vous continuer de jouer? (o/n)")
        if quitter == "n" or quitter == "N":
            print("Vous quittez la partie avec", solde, "$. A la prochaine fois!")
            continuer_partie = False




os.system("pause")
