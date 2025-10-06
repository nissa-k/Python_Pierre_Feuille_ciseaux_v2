from colorama import Fore, Style
from gaming.game import *
import pyfiglet


def score(score_joueur, score_ordi, duree, nom_joueur):
    
    message=pyfiglet.figlet_format("MERCI")                                             #on importe un style d'ecriture avec pyfiglet
    
    if score_joueur>score_ordi:                                                         # si le score du joueur est superieur a celui de l ordi il gagne
        print("la partie a durée : " + str(duree))
        print("Felicitations tu as gagne la partie ! tu as defonce l ordinateur gg mon reuf !\n" + str(Fore.GREEN) + nom_joueur +" :) " + str(score_joueur) + " | " + str(Fore.RED) + " ordi :( " + str(score_ordi) + Style.RESET_ALL)

    elif score_joueur<score_ordi:                                                       # si le score du joueur est inferieur a celui de l ordi il perd
        print("la partie a durée :  " + str(duree))
        print("Dommage tu as perdu la partie ! l ordi t a defonce !\n" + str(Fore.RED) + nom_joueur +"  :( " + str(score_joueur) + " | " + str(Fore.GREEN) + " ordi :) " + str(score_ordi) + Style.RESET_ALL)

    else:                                                                               # sinon egalite
        print("la partie a durée : " + str(duree))
        print("Egalite ! \n tu as tenu tete a l ordi gg mon reuf l ia ne pourras jamais remplacer les humains la RESISTANCE !")
   
    print(message)
