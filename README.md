# TP-final-Python-B2

🧬 Jeu de la Vie de Conway

Le Jeu de la Vie est un automate cellulaire imaginé par le mathématicien John Conway en 1970. Il s'agit d'un simulateur de vie artificielle où des cellules naissent, vivent ou meurent selon des règles simples. Ce projet implémente le Jeu de la Vie en [langage de programmation utilisé].

🎮 Fonctionnement

Le jeu se déroule sur une grille de cellules pouvant être soit vivantes, soit mortes. À chaque itération (ou "génération"), l'état des cellules évolue selon les règles suivantes :

🧍‍♂️ Survie : Une cellule vivante avec 2 ou 3 voisines vivantes reste en vie.

☠️ Mort par isolement : Une cellule vivante avec moins de 2 voisines meurt.

🔥 Mort par surpopulation : Une cellule vivante avec plus de 3 voisines meurt.

👶 Naissance : Une cellule morte avec exactement 3 voisines vivantes devient vivante.

🧱 Technologies utilisées

Langage : [Python ]

🚀 Lancer le projet
🔧 Prérequis

[Python 3.x ]

[Dépendances si besoin]

▶️ Exécution
# Cloner le dépôt
git clone https://github.com/Adrianne98/TP-final-Python-B2.git
cd TP-final-Python-B2

# Installer les dépendances
Si besoin

# Lancer le jeu
python main.py


💡 Adapte les commandes ci-dessus selon ton environnement.

🖥️ Exemple de rendu

📁 Structure du projet
jeu-de-la-vie/
├── main.py              # Fichier principal
├── data.py              # Logique du jeu
├── grid.py              # Gestion de la grille
├── cell.py             # Fonctions utilitaires
└── README.md            # Ce fichier

✅ Fonctions implémentées

 Initialisation aléatoire de la grille

 Mise à jour automatique des générations

 Sauvegarde/chargement de grilles
