NOTES EXPLICATIVES - APPLICATION CHESS TOURNAMENT MANAGER

Généralités
On utilise le modèle MVC
>Modèle : les données et structuration
>Vue : saisie et interaction utilisateur, affichage des données
>Controle : gestion interne et coordination vue et modèle

Les modules "Controller" sont au coeur du programme et leur fonction est:
- appeler des modules Viewer pour 
a)gérer affichage 
b)enregistrer des interactions avec utilisateur

- appeler des modules Model pour :
a)obtenir de l'information extraite des fichiers Json
b)vérifier un format (date)
c)regrouper/élaborer/présenter des données dans une présentation spécifique (liste)

Une fonction remplit une tâche déterminée avec uniquement le minimum de paramètres dont elle a besoin et renvoie ce pour quoi elle est destinée (séparation des tâches, lisibilité, évolutivité, simplicité, réutilisation).
L'identité d'un tournoi est son numéro.
L'identité d'un joueur est un code : deux alphabets, 4 chiffres.
On peut ajouter et modifier les listes de tournois et joueurs.
Chacun à son propre fichier Json.
Chaque tournoi puise ses participants dans la liste des joueurs.


A. Utilisation de l'application

Un premier menu propose : 
1. Gestion des joueurs
2. Gestion des tournois

La Gestion des joueurs permet :
1. Ajouter un joueur
2. Modifier un joueur

La Gestion des tournois permet : 
1. Afficher/Modifier les données du tournoi
2. Modifier la liste des participants (sélection à partir de la liste des joueurs)
3. Jouer le dernier round (en cours)
4. Voir les matchs déjà joués.
5. Voir les données de base du tournoi.


B. Structure et fonctionnement général de l'application 

Modèle Modèle-Vue-Controle, en séparant les fonctions.

Concernant la présentation, afin que le code soit lisible, maintenable et réutilisable, je respecte les principes du PEP-8, avec formatage automatique (autopep8) et formatage manuel (longueurs des lignes, vérification avec flake8).
    +indentation par 4
    +variable aussi explicite que possible
    +espacement autour des opérateurs
    +longueur des lignes
    +underscore pour nom de variable/fonction
    +camel case pour les classes
    +snake_case pour les fonctions
    +import en début de fichier
    +utiliser les f-strings pour concaténation

A. LA PARTIE TOURNOI

1/ Le Contrôle

Catégories de controleurs:
a) des menus (menu principal et menu pour un tournoi)
c) gestion coordonnées extraction et sauvegarde de données
d) gestion des données saisies récupérées (via des vues)

Chaque contrôleur utilise des "vues" dans TournamentView et puise des données dans TournamentModel.

2/ Les Vues
Cinq catégories de vues:
a) des menus (principal et menu pour un tournoi)
b) affichage de données simples (données d'un tournoi)
c) saisie de données (round, données tournoi)
d) sélection de données (choisir les participants)
e) mise en forme de données (liste de matches déjà joués)

3/ Le Modèle

Catégorie
a) lire un fichier json
b) enregistrer sur un fichier json
c) classe Tournament et ses attributs (nom, date, lieu, description)
d) vérifier les formats: 
    +date cohérente
    +format date
    +identifiant joueur : bon format, pas de doublon
e) extraire des données 
    +les présenter : liste
    +les extraire : paire de match, score, round

B. LA PARTIE PLAYER

1/Modèle
a) vérification des formats (date)
b) extraction de données
c) composition de listes

2/Vues
a)affichage de liste
b)impression général (print), délocalisé afin de tenir compte éventuel changement c)futur de mode d'affichage (fonction display)

3/Contrôle
a)ajouter un joueur
b)changer les données d'un joueur
c)appel aux vérifications (pas de doublon identifiant, format des dates)
d)sauvegarde des données (via le modèle correspondant)

