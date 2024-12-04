NOTES EXPLICATIVES

Utilisation de l'application

Un menu principal propose systématiquement le choix du fichier où sont enregistrés les tournois.
Par défaut, il puise ses données dans "tournament_data.json".
Taper sur Entrée pour continuer.
On choisit ensuite quel tournoi on souhaite voir/modifier ou bien "0" si on veut en créer un.
Si on crée un tournoi, il aura comme identifiant (dernier tournoi +1).
Une fois le tournoi choisi, on voit les données de base le concernant et qui sont renseignées :
Nom, Lieu, Date de début et fin, Nombre de rounds, Description
Puis la liste des participants (si elle existe)
Et la totalité des Matches enregistrés (round par round)

On peut alors 
+ Modifier les données de base
+ Ajouter/modifier la liste des participants
+ Jouer les rounds : sous-menu entre "saisie manuelle" et "aléatoire"

Ou sélectionner un autre tournoi, ou quitter l'application.

A noter :
+ avant de lancer des matches, il faut avoir une liste de participants 
  avec un nombre pair de participants et supérieur à 2
+ si on souhaite modifier la liste des participants, les matches seront effacés 
  (pour éviter les incohérences)

Les données sont régulièrement enregistrées, après la confirmation de l'utilisateur, à chaque étape.


#Application

Il y a trois classes principales : 
+ Une classe contenant les contrôleurs généraux
+ Une classe Tournament contenant vue, modèle et contrôleur pour les tournois
+ Une classe Player contenant les attributs des joueurs (et une méthode : add_player)

Classe Controle_app

*play_match(mode,player1,player2)
*load_tournament_from_json
*main_menu
*list_of_tournament

Classe Tournament
<u>Accès fichier / données : sauvegarde et upload (MODELE)</u>
*change_specific_data : pour enregistrer dans json la liste de participants et les matches joués
*change_data_file : pour enregistrer les données de base d'un tournoi (à partir d'un dictionnaire)
*get_list_player_json : récupérer les données des joueurs et les affecter aux attributs de la Classe Player

<u>Interaction utilisateur (VUE)</u>
*choose_participants : pour choisir les participants à partir liste des joueurs 
*play_round : jouer [x] rounds de [nbre participants/2] matches, avec option "input" (saisie manuelle) ou "random" (aléatoire).
La première liste est celle des participants puis une liste des meilleurs joueurs, avec une vérification qu'ils n'ont pas précédemment joué ensemble.
*input_data_tournament: saisie des données d'un tournoi (sauf matches et participants)


Classe Player

*get_list_player_json : récupère la liste des joueurs dans le fichier les contenant
*add_player : 
*list_of_participants : renvoie une liste des participants (séparés par virgule)
*show_matches : extraction de tous les matchs d'un tournoi et affichage round par round


CONTROLES
*generate_set_players : on crée copie de la liste, on vérifie si première paire déjà jouée; si oui, on garde premier élément et on
fait une paire avec l'élément suivant; on retire les éléments de la liste et on reprend le processus. Le but est d'avoir le moins de 
paires jouées deux fois.





MODELE

Extraction de listes