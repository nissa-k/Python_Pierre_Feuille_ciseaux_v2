from info.info_bot import *
from info.info_player import *
from rules.rules_game import *
from gaming.game import *

def menu():                                                                         #fonction pour afficher le menue
    while True:                                             #boucle infinie pour revenir au menue apres chaque partie s arrete qu avec un break                             
        print (" 1- jouer \n 2- regles du jeu \n 3- info sur le bot \n 4- quitter \n")
        choix=int(input("choisi une option ! \n "))                                      

        if choix==1:
            debut_game()                                                              #on appelle la fonction debut_game pour lancer le jeu
        elif choix==2:
            print(regles_jeu())                                                                  #on appelle la fonction regles pour afficher les regles du jeu
        elif choix==3:
            print(info_bot() )                                                               #on appelle la fonction info_bot pour afficher les infos sur le bot
        elif choix==4:
            print("merci d avoir joue ! a bientot j espere !")
            clear()
            break
        else:
            print("choix incorrect, recommence ! \n")
            continue                                   # si le choix n est pas bon on recommence la boucle  on saute le code avec continue


