
import os
import platform

def clear():                                                                        #fonction pour nettoyer le terminal en fonction du systeme d exploitation clear ou cls 
    if platform.system() == "Windows": 
        os.system('cls')
    else:
        os.system('clear') 
 