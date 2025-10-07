██████╗ ██╗██╗██████╗ ██████╗ ███████╗██████╗ 
██╔══██╗██║██║██╔══██╗██╔══██╗██╔════╝██╔══██╗
██████╔╝██║██║██████╔╝██████╔╝█████╗  ██████╔╝
██╔═══╝ ██║██║██╔═══╝ ██╔══██╗██╔══╝  ██╔══██╗
██║     ██║██║██║     ██║  ██║███████╗██║  ██║
╚═╝     ╚═╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
         🎮 PIERRE – FEUILLE – CISEAUX 🎮




🧩 Description du projet

Ce projet est une implémentation du célèbre jeu Pierre – Feuille – Ciseaux en Python, avec une structure modulaire et un affichage soigné.
L’objectif est de permettre à un joueur d’affronter l’ordinateur dans une série de manches, avec gestion du score, du menu et des règles du jeu.

🚀 Fonctionnalités principales :

🪨 Choix interactif : le joueur choisit entre pierre, feuille ou ciseaux.

💻 Adversaire virtuel : l’ordinateur fait un choix aléatoire grâce au module random.

⚖️ Système de victoire clair :

Pierre bat Ciseaux

Feuille bat Pierre

Ciseaux bat Feuille

🔁 Boucle de jeu continue : possibilité de rejouer autant de fois que le joueur le souhaite

🧮 Score automatique : comptabilisation des victoires, défaites et égalités.

🕹️ Menu principal : navigation intuitive entre les options du jeu.

🧼 Effacement automatique du terminal : utilisation de la fonction clear() pour un affichage propre.

📅 Affichage de la date et de l’heure actuelles au lancement du jeu.


PYTHON_PIERRE_FEUILLE_CISEAUX/
│
├── main.py                      
│
├── game_utilities/
│   ├── __init__.py
│   ├── menu.py                  
│   ├── choice.py               
│   ├── score.py              
│
├── gaming/
│   ├── __init__.py
│   ├── game.py                
│
├── info/
│   ├── __init__.py
│   ├── info_player.py           
│   ├── info_bot.py           
│
├── rules/
│   ├── __init__.py
│   ├── rules_game.py           
├── useful_function/
│   ├── __init__.py
│   ├── clear.py               
│
└── README.md                  



🏁 Lancer le jeu

Installation et Lancement

1. Clonez ce projet sur votre machine locale :
git clone https://github.com/nissa-k/Python_Pierre_Feuille_ciseaux_v2.git

2. Dans le terminal 
python main.py

👤 Auteur

Projet réalisé par Safaa Zemmar et Nissa Karadag