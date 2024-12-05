NOTES EXPLICATIVES

Utilisation de l'application

Avant l'accès au menu est proposé le fichier source.
Par défaut, c'est "tournament_data.json".
Taper sur Entrée pour continuer.

Ensuite, affichage des tournois. On choisit celui qu'on veut, ou 0 pour en ajouter un.

Alors s'affichent les données du tournoi choisi :
+Données de Base : Nom, Lieu, Date de début et fin, Nombre de rounds, Description
+Liste des participants (si elle existe)
+Les Matches enregistrés (chaque round, qui vs qui, scores)

On peut alors 
+ Modifier les données de base
+ Ajouter/modifier la liste des participants
+ (Re)jouer les rounds : via "saisie manuelle" ou "aléatoire"

Ou sélectionner un autre tournoi, ou quitter l'application.

A noter :
+ impossible de faire des matchs sans liste de participants (> 2 et pair)
+ modifier les participants implique d'effacer les matches (cohérence)

Les données sont enregistrées (après confirmation) à chaque étape utile.


#Application

Il y a trois classes principales : 
+ Une classe contenant les contrôleurs généraux
+ Une classe Tournament contenant vue, modèle et contrôleur pour les tournois
+ Une classe Player contenant les attributs des joueurs (et une méthode : add_player)

1/ Classe General

CONTROLE/VUE
*play_match(mode,player1,player2) : jouer les matchs, round par round, en saisie ou aléatoire 
*generate_set_players : génère liste de pairs non encore jouées (si possible)

MODELE
*load_tournament_from_json : alimente une instance de Tournament avec les données du fichier
*list_of_tournament : récupère les méta-données sur les noms des tournois dans le fichier

VUE
*main_menu : menu principal 


2/ Classe Tournament

Accès fichier / données : sauvegarde et upload (MODELE)

*change_specific_data : pour enregistrer dans json la liste de participants et les matches joués
*change_data_file : pour enregistrer les données de base d'un tournoi (à partir d'un dictionnaire)
*get_list_player_json : récupérer les données des joueurs et les affecter aux attributs de la Classe Player

Interaction utilisateur (VUE)

*choose_participants : pour choisir les participants à partir liste des joueurs 
*play_round : jouer [x] rounds de [nbre participants/2] matches, avec option "input" (saisie manuelle) ou "random" (aléatoire). Utilise la fonction play_match
La première liste est celle des participants puis une liste des meilleurs joueurs, avec une vérification qu'ils n'ont pas précédemment joué ensemble.
*input_data_tournament: saisie des données d'un tournoi (sauf matches et participants)

3/ Classe Player

Accès fichier / données : sauvegarde et upload (MODELE)

*get_list_player_json : récupère la liste des joueurs dans le fichier les contenant
*add_player : EN COURS

VUE
*list_of_participants : renvoie une liste des participants (séparés par virgule)
*show_matches : extraction de tous les matchs d'un tournoi et affichage round par round

CONTROLES
*generate_set_players : on crée copie de la liste, on vérifie si première paire déjà jouée; si oui, on garde premier élément et on
fait une paire avec l'élément suivant; on retire les éléments de la liste et on reprend le processus. Le but est d'avoir le moins de 
paires jouées deux fois.

