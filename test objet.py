import random
import json
import views as v

class Player:
    def __init__(self,surname,firstname,birthday):
        self.surname=surname
        self.firstname=firstname
        self.birthday=birthday
        
        
        self.baratin=f"mon nom c'est {surname}"

    def __str__(self):
        return f"je suis {self.surname}"

class Match:
    def __init__(self,j1,j2,sc1,sc2):
        self.j1=j1
        self.j2=j2
        self.sc1=sc1
        self.sc2=sc2
        self.pair=([j1,sc1],[j2,sc2])

class Tournament:
    def __init__(self,name,location,start,end,num_round,description,players,rounds):
        self.name=name
        self.location=location
        self.start=start
        self.end=end
        self.num_round=num_round
        self.rounds=rounds
        self.players=players
        self.description=description

def ranking_players (dictionnary):
        text=""
        dictionnary=dict(sorted(dictionnary.items(), key=lambda item: item[1], reverse=True))
        for index, (cle, valeur) in enumerate(dictionnary.items()):
       
            text+=str(index+1)+"> "+cle+ " - "+ str(valeur)+" \n"
        return(text)

def record_list_in_tournament (list_data,list_players,list_round) :
        
    # Nom du fichier JSON
    nom_fichier = "tournament_data.json"

    # Créer un dictionnaire pour stocker les éléments sous des rubriques
    donnees = {}
    rubrique=["name","location","start JJMMAAAA","end JJMMAAAA","num_round","description","list_players",'list_round']
    for x, element in enumerate(list_data, start=0):
        donnees[rubrique[x]] = list_data[x]
    donnees[rubrique[6]]=list_players
    donnees[rubrique[7]]=list_round

    # Ajouter chaque élément de la liste sous une rubrique
    
        #rubrique = f"nom_{i}"  # Rubrique sous la forme nom_1, nom_2, etc.
        #donnees[rubrique] = element

    # Enregistrer le dictionnaire dans un fichier JSON
    with open(nom_fichier, 'w') as fichier_json:
        json.dump(donnees, fichier_json, indent=4)


def play_a_round_input (list_players) :
#premier tour, j'affecte des scores et je fais nbre participant/2
    save_list=[]
    past_matches=[]
    score=[0]*len(list_players)
    storage_score=dict(zip(list_players, score))

    nbre=int(len(list_players)/2)+2
    for rounds in range(0,2):
        result=v.choice_three_options(list_players)
        for i in range(0,nbre,2):
            
            player1=list_players[i]
            player2=list_players[i+1]
            sc1=result[i]
            sc2=result[i+1]
            #print(player1+" "+str(sc1))
            current_match=Match(player1,player2,sc1,sc2)
            #print(current_match.pair)
            #Sélection des deux premiers participants de la liste
            save_list.append(current_match.pair)

            #On ajoute à la liste des paires déjà jouées la paire actuelle
            past_matches.append({player1,player2})

            storage_score[player1] += sc1
            storage_score[player2] += sc2
            
        new_list=sorted(storage_score, key=lambda k: storage_score[k], reverse=True)

        list_players=generate_set_players(new_list,past_matches)
            
    return(past_matches,save_list,storage_score)


def play_a_round_random (list_players) :
#premier tour, j'affecte des scores et je fais nbre participant/2
    save_list=[]
    past_matches=[]
    score=[0]*len(list_players)
    storage_score=dict(zip(list_players, score))

    nbre=int(len(list_players)/2)+2
    for rounds in range(0,2):
        for i in range(0,nbre,2):
        
            player1=list_players[i]
            player2=list_players[i+1]
            sc1,sc2=play_match(player1,player2)
            #print(player1+" "+str(sc1))
            current_match=Match(player1,player2,sc1,sc2)
            #print(current_match.pair)
            #Sélection des deux premiers participants de la liste
            save_list.append(current_match.pair)

            #On ajoute à la liste des paires déjà jouées la paire actuelle
            past_matches.append({player1,player2})

            storage_score[player1] += sc1
            storage_score[player2] += sc2
            
        new_list=sorted(storage_score, key=lambda k: storage_score[k], reverse=True)

        list_players=generate_set_players(new_list,past_matches)
            
    return(past_matches,save_list,storage_score)



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

def generate_set_players (input_list,past_matches):
    output_list=[]
    ongoing=input_list.copy()
    a=0
    b=1
    elt1=ongoing[a]
    elt2=ongoing[b]
    pair={elt1,elt2}
    
    while len(ongoing)>0:
        elt1=ongoing[a]
        elt2=ongoing[b]
        pair={elt1,elt2}
        if pair in past_matches:
            print("la paire suivante a déjà été jouée")
            print(pair)
            print('avec la liste')
            print (ongoing)
            print("et le déjà joué")
            #print(input_list)
            for h in range (2,len(ongoing)):
                elt1=ongoing[a]
                elt2=ongoing[h]
                pair_t={elt1,elt2}
                if pair_t not in past_matches:
                      print("donc proposition suivante")
                      print(pair_t)
                      output_list.append(elt1)
                      output_list.append(elt2)
                      break
                elif pair_t in past_matches:
                    print("DOUBLON - bon bah faut rejouer")
                    elt1=ongoing[a]
                    elt2=ongoing[b]
                    output_list.append(elt1)
                    output_list.append(elt2)
                    pair_t={elt1,elt2}
                    print(pair_t)
                    break
        if pair not in past_matches:
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


def get_list_player_json(name_file):
    liste=[]
    players=feed_data_player(name_file)
    for i in range (0,len(players)):
        liste.append(players[i].surname)

    return (liste)

#print(get_list_player_json("players_database.json"))

#liste=["andre","joe","fabien","suzie","bertha","mélodie","fred",'paula']
liste=get_list_player_json("players_database.json")
print(liste)
#a,b,c=play_a_round_input(liste)
#print(a)
#print(b)
#print(c)

#v.show_text("CLASSEMENT",ranking_players (c))

bidule=["name","location","start JJMMAAAA","end JJMMAAAA","num_round","description"]


#retour_input.append(joueurs)
#print(retour_input[6][3])

formulaire = v.FormulaireSaisie(bidule)

# Lancer l'interface graphique
formulaire.lancer()

# Après la fermeture de la fenêtre, afficher les valeurs saisies
valeurs = formulaire.afficher_valeurs()
print(valeurs)
#back=v.choice_elements(liste)
joueurs=v.choice_elements(liste)
print(joueurs)
list_round=[]

record_list_in_tournament (list_data=valeurs,list_players=joueurs,list_round=list_round)
#print(back)