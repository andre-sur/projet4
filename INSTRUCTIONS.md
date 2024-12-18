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
+ Jouer les rounds du tournoi (les enregistrer)

Ou sélectionner un autre tournoi, ou quitter l'application.

A noter :
+ impossible de faire des matchs sans liste de participants (> 2 et pair)
+ modifier les participants implique d'effacer les matches (cohérence)

Les données sont enregistrées (après confirmation) à chaque étape utile.


#Application

Autant que possible, j'applique le modèle Modèle-Vue-Controle, en séparant les fonctions.

Concernant la présentation, afin que le code soit lisible, maintenable et réutilisable, je respecte les principes du PEP-8
+indentation par 4
+variable aussi explicite que possible
+espacement autour des opérateurs
+longueur des lignes
+underscore pour nom de variable/fonction
+camel case pour les classes
+snake_case pour les fonctions
+import en début de fichier
+utiliser les f-strings pour concaténation

Des corrections manuelles ont été faites, ainsi qu'avec autopep8 et en utilisant flake8.
Ne reste que des lignes "trop" longues, un peu plus de 79 caractères.

Concernant la structure générale, il y a trois classes  : 
+ Une classe TournamentModel qui contient les attributs (et modèles)
+ Une classe TournamentControl qui contient les contrôles
+ Une classe TournamentView contenant les vues pour les tournois, notamment le menu principal et les sous-menus
+ Une classe Player contenant les attributs des joueurs 

1/ Classe TournamentModel (attribut et MODELE)
Elle contient les attributs d'un tournoi : nom, lieu, date départ/fin, liste des participants, archivage des matches joués...

*upload_file : récupérer données tournoi d'un fichier json
*load_tournament_from_json : alimente une instance de Tournament avec les données du fichier
*list_of_tournament : récupère les méta-données sur les noms des tournois dans le fichier
*change_specific_data : pour enregistrer dans json la liste de participants et les matches joués
*change_data_file : pour enregistrer les données de base d'un tournoi (à partir d'un dictionnaire)

2/ Classe des VUES : TournamentView

*main_menu : menu général
*choose_which_tournament : choisir le tournoi qu'on veut afficher parmi ceux enregistrés
*menu_tournament : sous-menu pour un tournoi spécifique
*change_participants : vérification condition pour demande de changer les participants
*choose_participants : choix des participants parmi les joueurs existants (fichier json)
*choose_howto_play : sous-menu pour choisir si jeu aléatoire ou saisie clavier
*list_of_tournament : la liste des tournois, extraites du fichier json
*input_data_tournament: saisie des données d'un tournoi (sauf matches et participants)
*list_of_participants : renvoie une liste des participants (séparés par virgule)
*show_matches : extraction de tous les matchs d'un tournoi et affichage round par round

3/ Classe des CONTROLES : TournamentControl
*play_match(mode,player1,player2) : enregistre les scores des matchs, round par round
*generate_set_players : génère liste de pairs non encore jouées (si possible)
*play_round : jouer [x] rounds de [nbre participants/2] matches. Utilise la fonction play_match

2/ Class Player
*get_list_player_json : récupérer les données des joueurs et les affecter aux attributs de la Classe Player
