import random
import json
from datetime import datetime,date,time,timedelta
import views as v


#MODELE

class Tournament:
    def __init__(self,name,location,start,end,rounds,current_round,list_round,players,description):
        self.name=name
        self.location=location
        self.start=start
        self.end=end
        self.rounds=rounds
        self.current_round=current_round
        self.list_round=list_round
        self.players=players
        self.description=description

class Player:
    def __init__(self,surname,firstname,birthday):
        self.surname = surname
        self.firstname = firstname
        self.birthday=birthday

def read_filejson (name):
    with open(name,"r",encoding="utf-8") as file:
        database_player=json.load(file)
    return(database_player)

def feed_data_player(name_file):
    data={}
    data = read_filejson(name_file)
    players=[]
    for player_data in data["joueurs"]:
        player=Player(player_data["surname"],player_data["firstname"],player_data["birthday"])
        players.append(player)
    return(players)

liste=[]

def get_list_player_json(name_file):

    players=feed_data_player(name_file)
    for i in range (0,len(players)):
        liste.append(players[i].surname)

    return (liste)

def play_match(joueur1,joueur2):
    dice=random.randint(1,3)

    if dice ==1:
            score_joueur1=0
            score_joueur2=1
            
    if dice ==2:
            score_joueur1=1
            score_joueur2=0
            
    if dice ==3:
           score_joueur1=0.5
           score_joueur2=0.5

    return (score_joueur1,score_joueur2)    


def play_first_round_random(liste,storage_score,match) :
#premier tour, j'affecte des scores et je fais nbre participant/2
    joueur1=[]
    match=[]
    already_played=[]
    joueur2=[]
    ensemble=[]
    match_complet=[]
    current_list_set=[]

    nbre=int(len(liste)/2) #nombre de match = nombre participants / 2
   
    for i in range(0,nbre):

        #Sélection des deux premiers participants de la liste
        joueur1=liste[2*i]
        joueur2=liste[2*i+1]

        #On joue le premier match
        score1,score2 = play_match(joueur1,joueur2)
        #On récupère les scores pour chaque joueur et on les enregistre dans le dictionnaire
        storage_score[joueur1] += score1
        storage_score[joueur2] += score2

        #On ajoute à la liste des paires déjà jouées la paire actuelle
        already_played.append({liste[2*i],liste[2*i+1]})

        #Enregistrement sous forme de tuple
        pair_players=(joueur1,joueur2)
        match.append(pair_players)

        #On écrit le résultat du match en cours

        print("Match :"+liste[2*i]+ " vs. "+liste[2*i+1] + "/ "+str(score1)+ " - "+str(score2))


    return(match,already_played,storage_score)

def update_scores(storage_score,list_players,list_scores):

    for i in range(0,len(list_players)):
        print(str(list_players[i]))
        print(list_scores[i])
        storage_score[str(list_players[i])]+=list_scores[i]
        print(storage_score)
    
    return(storage_score)


def play_first_round_input(list,storage_score) :
#premier tour, j'affecte des scores et je fais nbre participant/2
    list_players=[]
    storage_score={}
    choice=v.scroll_menu("Choix du tournoi",list_tournament())
    index_choice=list_tournament().index(choice)

    list_players,match,storage_score,nbre_round=unfold_tournament(index_choice)
    print("BOUCLE INPUT")
    print("liste")
    print(list_players)
    print("match")
    print(match)
    print("nombre de round")
    print(nbre_round)
    #for i in range(0,len(tournament_data)):
     #   print(str(i)+">"+tournament_data[i].name)

     #AJOUTER ICI LA VERIFICATION LIST PLAYERS puis mouliner

    v.choice_three_options(list_players)

def unfold_tournament(tournament_index):   
    all_matches=get_matches(tournament_index,"tournament_data.json")
    text=""
    match=[]
    list_players=[]
    print(all_matches)
    nbre_round=len(all_matches)
    for t in range(0,nbre_round):
        print("ROUND #"+str(t))
        for u in range(0,len(all_matches[t])):
            text+="ROUND #"+str(t)+" - MATCH #"+str(u+1)+" "+all_matches[t][u][0][0]+" vs "+all_matches[t][u][1][0]+" => "+str(all_matches[t][u][0][1])+" - "+str(all_matches[t][u][1][1])+"\n"
            joueur1=all_matches[t][u][0][0]
            joueur2=all_matches[t][u][1][0]
            score1=all_matches[t][u][0][1]
            score2=all_matches[t][u][1][1]

#alimente la liste des joueurs
            list_players.append(joueur1)
            list_players.append(joueur2)

#alimente le dictionnaire

            storage_score[joueur1]+=score1
            storage_score[joueur2]+=score2

#alimente les matchs déjà joués (paires)

            pair_players=(joueur1,joueur2)
            match.append(pair_players)

#crée un texte de synthèse (avec retour à la ligne)
            text+="ROUND #"+str(t)+" - MATCH #"+str(u+1)+" "+all_matches[t][u][0][0]+" vs "+all_matches[t][u][1][0]+" => "+str(all_matches[t][u][0][1])+" - "+str(all_matches[t][u][1][1])+"\n"
    

            print("ROUND #"+str(t)+" "+joueur1+" VS "+joueur2+" - "+str(score1)+ " à "+str(score2))
            print(storage_score)
    print("")
    print("LISTE")
    
    #retire les doublons de la liste-player
    list_players=list(set(list_players))
    print(list_players)
    print("")
    print("MATCH")
   
    print(match)
    print("")
    print("DICO")
    
    print(storage_score)

    v.show_text("TOUS LES MATcHS",text)
    #add_a_round=v.choice_yesno("Ajouter un round","Voulez vous ajouter un round ?")
    return(list_players,match,storage_score,nbre_round)
   

def sorting_players (list_score):
    
    list_best=sorted(list_score, key=list_score.get,reverse=True)
    
    return(list_best)

next_list=[]

def format_date(date_str):
    jour = int(date_str[6:8])   # 01
    mois = int(date_str[4:6])    # 01
    annee = int(date_str[0:4])

    date_obj = datetime(annee, mois, jour)

# Définir le format souhaité
    format_choisi = "%d %B %Y"

    return(date_obj.strftime(format_choisi))

def generate_set_players (sorted_list,current_list_set):
    output_list=[]
    ongoing=sorted_list.copy()
    a=0
    b=1
    elt1=ongoing[a]
    elt2=ongoing[b]
    pair={elt1,elt2}
    
    while len(ongoing)>0:
        elt1=ongoing[a]
        elt2=ongoing[b]
        pair={elt1,elt2}
        if pair in current_list_set:
            print("la paire suivante a déjà été jouée")
            print(pair)
            print('avec la liste')
            print (ongoing)
            print("et le déjà joué")
            print(current_list_set)
            for h in range (2,len(ongoing)):
                elt1=ongoing[a]
                elt2=ongoing[h]
                pair_t={elt1,elt2}
                if pair_t not in current_list_set:
                      print("donc proposition suivante")
                      print(pair_t)
                      output_list.append(elt1)
                      output_list.append(elt2)
                      break
                elif pair_t in current_list_set:
                    print("DOUBLON - bon bah faut rejouer")
                    elt1=ongoing[a]
                    elt2=ongoing[b]
                    output_list.append(elt1)
                    output_list.append(elt2)
                    pair_t={elt1,elt2}
                    print(pair_t)
                    break
        if pair not in current_list_set:
            print("la paire suivante pas encore jouée donc on l'ajoute à la liste")
            print(pair)
            output_list.append(elt1)
            output_list.append(elt2)

        ongoing.remove(elt1)
        ongoing.remove(elt2)
    print("liste créée XXXXXXXXXXX")
    print(output_list)
        
    # next_list.append(first_element)
       # next_list.append(second_element)
    

   
        #list_final.append(new_pair)


    return(output_list)


#CONTROL

def get_matches(rang,name):
    # Lire le contenu actuel du fichier JSON
    with open(name, 'r',encoding="utf-8") as fichier:
        donnees = json.load(fichier)
   
    tournois = donnees.get('tournament', [])

    return(tournois[rang]['list_round'])

def update_list_match(rang,name,liste):
    # Lire le contenu actuel du fichier JSON
    with open(name, 'r',encoding="utf-8") as fichier:
        donnees = json.load(fichier)
    print(type(donnees))  # Affiche le type de données
    print(donnees)  
    tournois = donnees.get('tournament', [])
    # Mettre à jour l'attribut liste
    tournois[rang]['list_round'] = liste
    
    
    # Écrire le contenu modifié dans le fichier
    with open(name, 'w',encoding="utf-8") as fichier:
        json.dump(donnees, fichier,indent=1)

def add_player(new_one):
    # Lire le contenu actuel du fichier JSON
    with open("players_database.json", 'r',encoding="utf-8") as fichier:
        donnees = json.load(fichier)
    print(type(donnees))  # Affiche le type de données
    print(donnees)  
    donnees["joueurs"].append(new_one)
    
    # Écrire le contenu modifié dans le fichier
    with open("players_database.json", 'w',encoding="utf-8") as fichier:
        json.dump(donnees, fichier,indent=1)

match=()

def list_players():
    pass
    
def list_tournament ():
    list_tournament=[]
    for i in tournament_data:
        list_tournament.append(i.name)
    return(list_tournament)

def list_all_tournaments():
    choice=v.scroll_menu("Choix du tournoi",list_tournament())
    index_choice=list_tournament().index(choice)
    #for i in range(0,len(tournament_data)):
     #   print(str(i)+">"+tournament_data[i].name)
   
    all_matches=get_matches(int(index_choice),"tournament_data.json")
    text=""
    for t in range(0,len(all_matches)):
        #print("ROUND #"+str(t))
        for u in range(0,len(all_matches[t])):
            text+="ROUND #"+str(t)+" - MATCH #"+str(u+1)+" "+all_matches[t][u][0][0]+" vs "+all_matches[t][u][1][0]+" => "+str(all_matches[t][u][0][1])+" - "+str(all_matches[t][u][1][1])+"\n"
    
    v.show_text("SYNTHESE",text)

def show_tournament():
        for i in range(0,len(tournament_data)):
            print(str(i)+">"+tournament_data[i].name) 

def data_tournament(choice_tournament):
        choice2=input("Pour quel tournoi ?")
        date_start=v.format_date(tournament_data[int(choice_tournament)].start)
        date_end=v.format_date(tournament_data[int(choice2)].end)
        location=tournament_data[int(choice_tournament)].location
        return(date_start,date_end,location)
    
def feed_data_tournament():
        with open('tournament_data.json', 'r',encoding="utf-8") as fichier:
            data={}
            data = json.load(fichier)
            tournois=[]
            tourm = data.get('tournament', [])
            print(tourm[0]['list_round'])
            for t in tourm:
                tournoi=Tournament(t["name"],t["location"],t["start"],t["end"],t["rounds"],t["current_round"],t["list_round"],t["players"],t["description"])

                tournois.append(tournoi)
            return(tournois)
"""
print("DEBUT ICI DEBUT DEBUT DEBUT DEBUT")
lestournois=feed_data_tournament()

liste_initiale=get_list_player_json("players_database.json")
score_initial=[0]*len(liste_initiale)
storage_score=dict(zip(liste_initiale,score_initial))
print(storage_score)
liste=liste_initiale
pair1=[]
pair2=[]
already_played=[]
current_list_set=[]
sorted_list=[]
ajout_joue=[]
match=[]
matches=[]
sorted_keys=sorted(liste_initiale)
nbre=int(len(liste_initiale)/2)
liste=liste_initiale
round=[]
print(liste_initiale)
#generate_set_players ("",sorted_list=sorted_keys,current_list_set=already_played)

for tour in range(0,2):
    print("============================================================ROUND "+str(tour))
    match=[]
    
    for i in range (0,nbre):
        if tour == 0:
            liste=liste_initiale
        else:
            liste=generate_set_players (sorted_list=sorted_keys,current_list_set=already_played)
        print("ROUND #"+str(i))
        pair1=[]
        pair2=[]
        joueur1=liste[2*i]
        joueur2=liste[2*i+1]
        score1,score2 = play_match(joueur1,joueur2)
        storage_score[joueur1] += score1
        storage_score[joueur2] += score2
        already_played.append({liste[2*i],liste[2*i+1]})
        print("Match :"+liste[2*i]+ " vs. "+liste[2*i+1] + "/ "+str(score1)+ " - "+str(score2))

        pair1.append(joueur1)
        pair1.append(score1)

        pair2.append(joueur2)
        pair2.append(score2)
        mon_tuple=(pair1,pair2)
        print ("tuplesque "+str(mon_tuple))
        match.append(mon_tuple)
      
        lestournois[0].list_round.append(match)
        sorted_keys= sorting_players (storage_score)
    matches.append(match)

    print("score des joueurs tableau")
    print(storage_score)
    print(sorting_players (storage_score))
    sorted_keys= sorting_players (storage_score)
    print("on verifie la liste triée pour voir si pairs")
        
print("déjà joué - TOUR " + str(tour))
print(already_played)
print("ARCHIVAGE DES SCORES")
print(storage_score)

print("MATCH - FORMAT RECORDING")

print(matches)
update_list_match(rang=0,name="tournament_data.json",liste=matches)

print("le tournoi "+lestournois[0].name+" a les matchs suivants enregistrés")
print ("et il a lieu à "+lestournois[0].location)
print("")

#print(lestournois[0].list_round)

print("et le premier tour est")
print(lestournois[0].list_round[0])
print("et le premier match est")
print(lestournois[0].list_round[0][0])

print("nouvelle liste triée")

print("output generate")
print(next_list)
print("")

print ("et il a lieu à "+lestournois[1].location)
"""
# LES FONCTIONS - CHOIX DU MENU

def list_of_players():
    text=""
    for i in sorted_keys:
        text+="\n"+i
    v.show_text("liste des joueurs",text)

def list_of_tournament():
    v.show_text("liste des tournois",list_tournament ())

def when_tournament():
    a=list_tournament()
    v.about_tournament(a)
    #date_start=format_date(tournament_data[int(choice)].start)
    #date_end=format_date(tournament_data[int(choice)].end)
    #location=tournament_data[int(choice)].location

def choice4():
    v.show_text("liste des tournois",list_tournament ())


def add_a_player():
    dictionnaire={}
    surname,name,birthday=data_input_option("Ajouter un joueur",3,"Nom","Prénom","Date de naissance")
    dictionnaire["surname"]=surname
    dictionnaire["name"]=name
    dictionnaire["birthday"]=birthday
    confirmation=choice_yesno ("Confirmation enregistrement","Vous confirmez bien vouloir ajouter un participant ?")
    if confirmation :
        add_player(new_one=dictionnaire)

#Initialisation des données
tournament_data=feed_data_tournament()
print(tournament_data[0].name)

def input_matches():
    
    list_players,match,storage_score,nbre_round=unfold_tournament(0)
    play_first_round_input(list,storage_score)

#Paramétrage du menu principal et fonctions correspondantes à chaque bouton
list_of_choice=['1.joueurs (alphabétique)',"2.tous les tournois","3.nom/date d'un tournoi","4.joueurs d'un tournoi","5.tours d'un tournoi","6.ajouter joueur","7. Enregistrer un tour"]
functions=[list_of_players,list_of_tournament,when_tournament,choice4,list_all_tournaments,add_a_player,input_matches]
#Lancement de la fonction Menu paramétrée
listetemp=["andre","joe","fabien","suzie","bertha","mélodie"]
dico={"andre":1,"joe":0,"fabien":0,"suzie":0,"bertha":0,"mélodie":0}
print(listetemp)
back=v.choice_elements(listetemp)
print("CHOIX")
print(back)
#scoreround=v.choice_three_options(listetemp)
print("ICI")
#print(scoreround)
#new_dico=update_scores(dico,listetemp,scoreround)
print('old dico')
print(dico)
print("new dico")
#print(new_dico)

#v.menu("MENU",list_of_choice,functions)

    




    




