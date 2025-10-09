from src.info.info_bot import *
from src.info.info_player import *
from src.rules.rules_game import *
from src.gaming.game import *

def menu():                                                                         #fonction pour afficher le menue
    while True:                                             #boucle infinie pour revenir au menue apres chaque partie s arrete qu avec un break                             
        print (" ***MENU*** \n \n 1- Jouer \n 2- Régles du jeu \n 3- Info sur le bot \n 4- Quitter \n")
        choix=int(input("Choisis une option ! \n "))                                      

        if choix==1:
            debut_game()                                                              #on appelle la fonction debut_game pour lancer le jeu
        elif choix==2:
            print(regles_jeu())                                                                  #on appelle la fonction regles pour afficher les regles du jeu
        elif choix==3:
            print(info_bot() )                                                               #on appelle la fonction info_bot pour afficher les infos sur le bot
        elif choix==4:
            print("Merci d avoir joué ! à bientot j'éspere !")
            clear()
            break
        else:
            print("Choix incorrect, recommence ! \n")
            continue                                   # si le choix n est pas bon on recommence la boucle  on saute le code avec continue


