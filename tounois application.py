import random
import json
from datetime import datetime,date,time,timedelta

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



def read_filejson (name):
    with open(name,"r",encoding="utf-8") as file:
        database_player=json.load(file)
    return(database_player)

match=()
#matches = ((("A",0),("B",1)),(("C",0),("D",1)),(("E",0),("F",1)),(("G",0),("H",1)),(("I",0),("J",1)),(("K",0),("L",1)))

#element = input("quelle place dans la liste")
#element=1
#paire_associee=matches[element][0][0]+" --- "+matches[element][1][0]
#pair1=(matches[element][0][0],matches[element][1][0])
#print ("la paire associée est"+str(pair1))

#set1=set(pair1)

#test=(("A","B"),("C","D"))
#settest=set(test)

#print ("est ce que "+str(set1)+" est égale à "+str(settest))
#print(set1==test)

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
    
def feed_data_tournament(self):
    with open('tournament_data', 'r',encoding="utf-8") as fichier:
        data={}
        data = json.load(fichier)
        tournois=[]
        tourm = data.get('tournament', [])
        print("ICI")
        print(tourm[0]['list_round'])
        for t in tourm:
            tournoi=Tournament(t["name"],t["location"],t["start"],t["end"],t["rounds"],t["current_round"],t["list_round"],t["players"],t["description"])

            tournois.append(tournoi)

        return(tournois)


class Player:
    def __init__(self,surname,firstname,birthday):
        self.surname = surname
        self.firstname = firstname
        self.birthday=birthday
    
def feed_data(self,name_file):
    data={}
    data = read_filejson(name_file)
    players=[]
    for player_data in data["joueurs"]:
        player=Player(player_data["surname"],player_data["firstname"],player_data["birthday"])
        players.append(player)
    return(players)

liste=[]

def get_datas_player_json(name_file):

    players=feed_data("",name_file)
    for i in range (0,len(players)):
        liste.append(players[i].surname)

    return (liste)


#already_played=[('Albert', 'Béatrice'), ('Carole', 'Denis'), ('Edouard', 'François'), ('Gérard', 'Hector'), ('Isabelle', 'Jules'), ('Karl', 'Louis')]

def play_match(self,joueur1,joueur2):
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


def play_matches(self,liste,storage_score,match) :
#premier tour, j'affecte des scores et je fais nbre participant/2
    joueur1=[]
    match=[]
    already_played=[]
    joueur2=[]
    ensemble=[]
    match_complet=[]
    current_list_set=[]
    nbre=int(len(liste)/2)
   
    for i in range(0,nbre):
        joueur1=liste[2*i]
        joueur2=liste[2*i+1]
        score1,score2 = play_match("",joueur1,joueur2)
        #play_match("",joueur1,joueur2)
        print (score1)
        storage_score[joueur1] += score1
        storage_score[joueur2] += score2
        already_played.append({liste[2*i],liste[2*i+1]})
        print({liste[2*i],liste[2*i+1]})

        print("Match :"+liste[2*i]+ " vs. "+liste[2*i+1] + "/ "+str(score1)+ " - "+str(score2))
        mon_tuple=(joueur1,joueur2)
        print ("tuplesque "+str(mon_tuple))
        match.append(mon_tuple)

    return(match,already_played,storage_score)

def sorting_players (self,list_score):
    
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


def generate_set_players (self,sorted_list,current_list_set):
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

print("DEBUT ICI DEBUT DEBUT DEBUT DEBUT")
lestournois=feed_data_tournament("")

liste_initiale=get_datas_player_json("players_database.json")
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
            liste=generate_set_players ("",sorted_list=sorted_keys,current_list_set=already_played)
        print("ROUND #"+str(i))
        pair1=[]
        pair2=[]
        joueur1=liste[2*i]
        joueur2=liste[2*i+1]
        score1,score2 = play_match("",joueur1,joueur2)
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
        sorted_keys= sorting_players ("",storage_score)
    matches.append(match)

    print("score des joueurs tableau")
    print(storage_score)
    print(sorting_players ("",storage_score))
    sorted_keys= sorting_players ("",storage_score)
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

testing=feed_data_tournament("")
print(testing[0].name)
print(testing[1].location)
print(testing[0].start)
print(testing[1].list_round)
print(testing[0].players)
print(testing[1].rounds)
print(testing[1].description)

print("====================")

print(" 1● liste de tous les joueurs par ordre alphabétique \n 2● liste de tous les tournois \n 3● nom et dates d’un tournoi donné \n 4● liste des joueurs du tournoi par ordre alphabétique \n 5● liste de tous les tours du tournoi et de tous les matchs du tour.\n 6● Ajouter un joueur/joueuse")
choice=input("Que voulez vous faire ?")

if choice == "1" :
    print("Voici la liste des joueurs par ordre alphabétique")
    print(liste)
elif choice == "2" :
    print("Voici la liste des tournois")
    for i in testing:
        print(i.name)
elif choice == "3" :
    print("Nom et date pour quel tournoi ?")
    for i in range(0,len(testing)):
        print(str(i)+">"+testing[i].name)        
    print("===============================================")
    choice2=input("Pour quel tournoi ?")
    print("Ce tournoi se déroule du "+format_date(testing[int(choice2)].start)+" au "+format_date(testing[int(choice2)].end))
    print("Il se tiendra à "+testing[int(choice2)].location)

elif choice == "5" :
    print("Nom et date pour quel tournoi ?")
    for i in range(0,len(testing)):
        print(str(i)+">"+testing[i].name)
    print("======")
    choice3=input("Pour quel tournoi ?")
    les_matches=get_matches(int(choice3),"tournament_data.json")
    for t in range(0,len(les_matches)):
        print("ROUND #"+str(t))
        print("-----------------")
        for u in range(0,len(les_matches[t])):
            print("MATCH #"+str(u+1)+" "+les_matches[t][u][0][0]+" vs "+les_matches[t][u][1][0]+" => "+str(les_matches[t][u][0][1])+" - "+str(les_matches[t][u][1][1]))
        print("++++++++++++++++++++1")

elif choice=="6":
    dictionnaire={}
    print("Ajouter un joueur")
    surname=input("Nom")
    name=input("Prénom")
    birth=input("Date de naissance")
    dictionnaire["surname"]=surname
    dictionnaire["name"]=name
    dictionnaire["birthday"]=birth
    confirmation=input("Vous confirmez l'enregistrement ? (o/n)")
    if confirmation == "o":
        add_player(new_one=dictionnaire)




    




