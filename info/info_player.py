def nom():                                                                          #fonction pour demander le nom du joueur
    nom=str(input(" quel est ton nom ? \n")).strip()                                #on enleve les espaces avec strip pour eviter les erreurs de saisie
    while nom == "":                                                             #controle de saisie si le nom est vide il recommence
        print("nom innexistant, recommence ! \n")
        nom=str(input(" quel est ton nom ? \n")).strip()
    return nom

def nb_manches():
    nb_manches=int(input("choisi le nombre de manche que tu veux jouer ! \n "))                                                                   #fonction pour demander le nombre de manches
    while nb_manches<=0:                                                            #controle de saisie si le nombre de manches est inferieur ou egal a 0 il recommence
        print("nombre de manches incorrect, recommence ! \n")
        nb_manches=int(input("choisi le nombre de manche que tu veux jouer ! \n "))
    return nb_manches

