import random
from useful_function.clear import *
from info.info_player import *
from time import *
from datetime import datetime
from game_utilities.choice import *
from game_utilities.score import score


def debut_game():
    
    score_joueur=0
    score_ordi=0
    choix_possible=["pierre","feuille","ciseaux"]

    clear()                                                                            #fonction pour nettoyer le terminal en fonction du systeme d exploitation clear ou cls
    
    nom_joueur=nom()                                                                           #on appelle la fonction nom pour demander le nom du joueur
    nombre_manches=nb_manches()                                                             #on appelle la fonction nb_manches pour demander


    debut=time()                                                                        #on prend le temps de debut de la partie

    for i in range (nombre_manches):                                                        # on boucle sur le nombre de manches choisit 
        print("Les choix possibles sont donc : "+ str(choix_possible))
        
        while True:
            choix_user=str(input("Choisi ton element ! \n ")).lower().strip()           #.split() marche pas car le mets en liste                  # on met en minuscule avec lower et enleve les espaces avec strip pour eviter les erreurs de saisie
            if choix_user in choix_possible:
                break                                                                   #si le choix est bon on sort de la boucle
            else:
                print("Choix incorrect, recommence ! \n")


        print("Prépare Toi a 3 !!!!!! ")
        for j in range (3):
            print(j+1)
            sleep(1)

        ordi=random.choice(choix_possible)                                              # choix aleatoire de l ordi
        print("l'ordi a choisi "+ str(ordi))

        score_joueur, score_ordi= choix( choix_user, ordi, score_joueur, score_ordi, i)                                                                       # on appelle la fonction choix pour determiner le gagnant de la manche
        print("-"*35)
    fin=time()
    duree=fin-debut         
#ajoute les scores et la duree a la fin de la partie
    score(score_joueur, score_ordi, duree, nom_joueur)                                                      # on appelle la fonction score pour afficher le score final et le gagnant de la partie

