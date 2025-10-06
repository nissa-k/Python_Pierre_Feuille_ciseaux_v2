import random
from time import *
from colorama import Fore, Style
from datetime import datetime

score_joueur=0
score_ordi=0
cpt_points=0
date=datetime.now()



choix_possible=["pierre","feuille","ciseaux"]
print(" Bienvenue dans le jeu pierre feuille ciseaux !" + date.strftime(" \n Nous sommes le %d/%m/%Y , il est %H:%M:%S"))      #formatage de la date et de l heure avec la classe datetime
nom=str(input(" quel est ton nom ? \n")).strip()                                               # on enleve les espaces avec strip pour eviter les erreurs de saisie
print(" Voici les regles du jeux ! \n \n Nous allons jouer a pierre feuille ciseaux \n pierre bat ciseaux ! \n ciseaux bat feuille ! \n feuille bat pierre \n si les 2 joueurs ont le meme element c est egalite ! \n \n Bonne chance les reufs ! \n")
nb_manches=int(input("choisi le nombre de manche que tu veux jouer ! \n "))


debut=time()                                                                        #on prend le temps de debut de la partie

for i in range (nb_manches):                                                        # on boucle sur le nombre de manches choisit 
    print("les choix possibles sont donc : "+ str(choix_possible))
    choix_user=str(input("choisi ton element !")).lower().strip()                   #.split() marche pas car le mets en liste                  # on met en minuscule avec lower et enleve les espaces avec strip pour eviter les erreurs de saisie

    if choix_user not in choix_possible:                                            #controle de saisie si l element saisie n est pas dans la liste des choix possibles il recommence 
        print("choix incorrect, recommence ! \n")
        choix_user=str(input("choisi ton element !")).lower().strip()

    ordi=random.choice(choix_possible)                                              # choix aleatoire de l ordi
    print("l ordi a choisi "+ str(ordi))

    if choix_user==ordi:                                                            # si egalite
        print("egalite ! \n")
        print("score : joueur "+ str(score_joueur) + " | ordi "+ str(score_ordi)+ "\n")

    elif (choix_user=="pierre" and ordi=="ciseaux") or (choix_user=="ciseaux" and ordi=="feuille") or (choix_user=="feuille" and ordi=="pierre"): # conditions de victoire pour le joueur
        score_joueur+=1
        print("tu as gagne cette manche ! \n On est a la "+ str(i+1)+"eme manche(s) \n ")
        print("score : joueur "+ str(score_joueur) + " | ordi "+ str(score_ordi))

    else:                                                                           # sinon l ordi gagne
        score_ordi+=1
        print("tu as perdu cette manche ! on est a la "+ str(i+1)+"eme manche(s)\n")        # i+1 car i commence a 0 dans une boucle for 
        print("score : joueur "+ str(score_joueur) + " | ordi "+ str(score_ordi))
    print("----------------------------------------------------------------------------------------------------------------------------------")
fin=time()
duree=fin-debut                                                                     # on calcule la duree de la partie 

if score_joueur>score_ordi:                                                         # si le score du joueur est superieur a celui de l ordi il gagne
    print("la partie a durée : " + str(duree))
    print("Felicitations tu as gagne la partie ! tu as defonce l ordinateur gg mon reuf !\n" + str(Fore.GREEN) + nom +" :) " + str(score_joueur) + " | " + str(Fore.RED) + " ordi :( " + str(score_ordi) + Style.RESET_ALL)

elif score_joueur<score_ordi:                                                       # si le score du joueur est inferieur a celui de l ordi il perd
    print("la partie a durée :  " + str(duree))
    print("Dommage tu as perdu la partie ! l ordi t a defonce !\n" + str(Fore.RED) + nom +"  :( " + str(score_joueur) + " | " + str(Fore.GREEN) + " ordi :) " + str(score_ordi) + Style.RESET_ALL)

else:                                                                               # sinon egalite
    print("la partie a durée : " + str(duree))
    print("Egalite ! \n tu as tenu tete a l ordi gg mon reuf l ia ne pourras jamais remplacer les humains la RESISTANCE !")
