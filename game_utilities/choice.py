
from colorama import Fore, Style

def choix(choix_user, ordi, score_joueur, score_ordi, i):
    if choix_user==ordi:                                                            # si egalite
        print("egalite ! \n")
        print("score : joueur "+ str(score_joueur) + " | ordi "+ str(score_ordi)+ "\n")

    elif (choix_user=="pierre" and ordi=="ciseaux") or (choix_user=="ciseaux" and ordi=="feuille") or (choix_user=="feuille" and ordi=="pierre"): # conditions de victoire pour le joueur
        score_joueur+=1
        print( str(Fore.GREEN) + "tu as gagne cette manche ! \n" + Style.RESET_ALL +"\n On est a la "+ str(i+1)+"eme manche(s) \n ")
        print("score : joueur "+ str(score_joueur) + " | ordi "+ str(score_ordi))

    else:                                                                           # sinon l ordi gagne
        score_ordi+=1
        print(str(Fore.RED) +"tu as perdu cette manche ! \n"+ Style.RESET_ALL + " on est a la "+ str(i+1)+"eme manche(s)\n")        # i+1 car i commence a 0 dans une boucle for 
        print("score : joueur "+ str(score_joueur) + " | ordi "+ str(score_ordi))
    return score_joueur, score_ordi