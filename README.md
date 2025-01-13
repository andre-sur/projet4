NOTES EXPLICATIVES - APPLICATION CHESS TOURNAMENT MANAGER

correction auto pep8
autopep8 --in-place --recursive .
flake8 .
puis flake8
variable inutilisée
conditions pas claires
too lo,ng autopep8 --in-place --max-line-length 79 --recursive .

Généralités
On utilisera le modèle MVC
Modèle : les données et structuration
Vue : saisie et interaction utilisateur, affichage des données
Controle : gestion interne

Cela signifie:
- Modèle n'appelle jamais ni Vue, ni Controle
- Vue peut appeler Modèle mais pas Controle
- Contrôle appele Vue et Modèle selon ses besoins

Une fonction remplit une tâche déterminée avec uniquement le minimum de paramètres dont elle a besoin et renvoie ce pour quoi elle est destinée


A. Utilisation de l'application

Un premier menu propose : 
1. Gestion des joueurs
2. Gestion des tournois

La Gestion des joueurs permet :
1. Ajouter un joueur
2. Modifier un joueur

La Gestion des tournois permet : 
1. Afficher/Modifier les données d'un tournoi
2. Modifier la liste des participants
3. Jouer le dernier round (en cours).



B. Structure et fonctionnement général de l'application 

Modèle Modèle-Vue-Controle, en séparant les fonctions.

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

A. LA PARTIE TOURNOI

1/ Le Contrôle

Quatre catégories de controleurs
a) des menus (menu principal et menu pour un tournoi)
b) vérification (format, contenu d'entrées saisies)
c) sauvegarde de données
d) saisie de données

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
d) vérifier un format (modèle? contrôle?)
e) extraire des données via procédure : modèle

B. LA PARTIE PLAYER

Modèle

Vues

Contrôle

