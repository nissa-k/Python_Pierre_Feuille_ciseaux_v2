from src.useful_function.clear import clear 
from src.game_utilities.menu import menu
from datetime import * 

def main():
    clear()
    print("Bienvenue dans le jeu du pierre-feuille-ciseaux ! \n")
    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n")
    menu()
    
if __name__ == "__main__":
    main()