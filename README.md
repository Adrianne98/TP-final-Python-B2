# TP-final-Python-B2

🔁 Partie – Détection de boucle & Sauvegarde (Jeu de la Vie de Conway)

                  🧩 Détection de boucle

L’objectif était de repérer les situations où le jeu entre dans un cycle (oscillation entre plusieurs états identiques).

Principe d’implémentation :


- À chaque génération, l’état de la grille est converti en une chaîne de caractères unique (hashable).

- Cet état est ajouté à une liste ou un ensemble.

- Avant d’ajouter un nouvel état, on vérifie s’il existe déjà dans l’historique.

- Si c’est le cas → une boucle est détectée.


                💾 Sauvegarde et chargement

J’ai également développé un module permettant de sauvegarder et recharger la grille à tout moment.

Fonctionnalités principales :


- Sauvegarde d’un état dans un fichier .json ou .txt.

- Chargement d’un état sauvegardé pour relancer la simulation.

- Vérification de l’intégrité du fichier lors du chargement.
