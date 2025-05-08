# Projet-Blackjack-PIL-Tkinter

# Blackjack - Jeu de Cartes

## Description

Le jeu **Blackjack** est une version numérique du célèbre jeu de casino. Dans ce jeu, l'objectif est de battre le croupier sans dépasser un score de 21 points. Le jeu utilise les cartes traditionnelles, et chaque carte a une valeur spécifique :

- Les cartes de 2 à 9 valent leur valeur nominale.
- Les cartes de 10, Valet, Dame et Roi valent 10 points.
- L'As peut valoir 1 ou 11 points, selon le choix du joueur.

## Fonctionnalités

### Interface Graphique
Le jeu utilise **Tkinter**, une bibliothèque Python pour créer des interfaces graphiques, pour afficher le jeu. Il inclut une fenêtre avec :
- Le **menu principal** : un écran d'accueil avec les options "Jouer" ou "Quitter".
- Une **fenêtre de jeu** avec un fond personnalisé, des boutons pour "Hit", "Stand", et "Remake".
- **Cartes de jeu** : affichage dynamique des cartes du joueur et du croupier.

### Règles du Jeu
- Le joueur commence avec deux cartes visibles.
- Le joueur peut choisir de demander une carte supplémentaire ("Hit") ou de s'arrêter ("Stand").
- Le joueur doit tenter d'atteindre 21 points sans dépasser ce total.
- Si le joueur dépasse 21, il "brûle" et perd la partie.
- Le croupier suit une règle spécifique : il tire jusqu'à 16 et s'arrête à 17.

### Options Supplémentaires
- **Choix de la valeur de l'As** : Lors de la distribution des cartes, l'As peut être choisi comme 1 ou 11, selon la préférence du joueur.
- **Gestion des scores** : Le score du joueur et du croupier est mis à jour et affiché en temps réel pendant le jeu.
