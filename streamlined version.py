import random
import time
import json
import tkinter as tk
from tkinter import ttk

# LES MODELES
class Player:

    def __init__(self,surname,firstname,birthday):
        self.surname=surname
        self.firstname=firstname
        self.birthday=birthday 

class Match:
    def __init__(self,j1,j2):
        self.j1=j1
        self.j2=j2
        self.sc1=None
        self.sc2=None
        self.pair=None

class Controle_app :
    # SIMULATEUR D'ENREGISTREMENT
    def record():
        print("Enregistrement en cours...")
        time.sleep(1)
        print("Paramétrage et synchronisation des modules...")
        time.sleep(2)
        print("Enregistrement confirmé.")

    #DETERMINATION ALEATOIRE DU RESULTAT D'UN MATCH
    def play_match_random(j1,j2):
        
        dice=str(random.randint(1, 3))

        if dice =="1":
                sc1=0
                sc2=1
                
        if dice =="2":
                sc1=1
                sc2=0
                
        if dice =="3":
                sc1=0.5
                sc2=0.5

        return (sc1,sc2) 
    
    #VUE : DETERMINATION DU RESULTAT D'UN MATCH VIA SAISIE CLAVIER
    def play_match_input(player1,player2):
        text="1. "+player1+" 2."+player2+" 3. Match nul. >>>"
        choice=input(text)

        if choice =="1":
                score1=0
                score2=1
                
        if choice =="2":
                score1=1
                score2=0
                
        if choice =="3":
                score1=0.5
                score2=0.5

        return (score1,score2) 
    
    #CHARGER LES DONNEES TOURNOI DU FICHIER JSON ET 
    #LES AFFECTER A UNE INSTANCE DE CLASSE 
    #(POUR UN NUMERO DE TOURNOI SPECIFIQUE)

    def load_tournament_from_json(tournament,filename):
        # Ouvre le fichier JSON et charge les données
        with open(filename, "r",encoding='utf-8') as file:
            all_datas = json.load(file)
            
        # Affectation des données à une instance de classe (pour l'identifiant tournament (chiffre))
        data = all_datas["tournaments"][tournament]
        selected_tournament = Tournament(name=data.get("name",""), location=data.get("location",""), start=data.get("start","")\
                                            ,end=data.get("end",""),num_round=data.get("num_round",""),description=data.get("description","")\
                                                ,players=data.get("players","test"),matches=data.get("matches",""))

        return selected_tournament
    
    def main_menu():
            print("")
            print("MENU PRINCIPAL")
            print("")
            file_name=input("FICHIER SOURCE (par défaut: tournement_data.json)")
            if file_name=="" :
                file_name="tournament_data.json"
     
            if file_name=="" :
                file_name="tournament_data.json"
            text,last_one=Controle_app.list_of_tournament(file_name)
            print(text)
            chosen_tournament=""
            list_options=[str(i) for i in range(0, int(last_one) + 1)]
            print(list_options)
            while chosen_tournament not in list_options:
                chosen_tournament=input("Quel tournoi ? (0 pour en créer un) >>>")
                
            if chosen_tournament=="0":
                        tournoi=Tournament()
                        tournoi.input_data_tournament((str(int(last_one)+1)))
            else:   
                    tournoi=Controle_app.load_tournament_from_json(chosen_tournament,file_name)
                    tournoi.show_basic_tournament()
                    
            sub_choice=""
            while sub_choice not in ["1","2","3","4"]:
                    sub_choice=input("  (1) Modifier ce tournoi (données de base) "
                                "\n  (2) Ajouter/Modifier la liste des participants"
                                "\n  (3) Jouer un round de "+str(tournoi.num_round)+" matches"
                                "\n  (4) Sélectionner un autre tournoi."
                                "\n  (5) Quitter l'application."
                                "\n   >>>")
                    
                    if sub_choice=="1":
                        tournoi.input_data_tournament(chosen_tournament)
                    if sub_choice=="2":
                        tournoi.choose_participants(chosen_tournament)
                    if sub_choice=="3":
                        if tournoi.players in [None, '', [], {}, ()] or len(tournoi.players)==0 or len(tournoi.players)% 2 != 0:
                            print("Aucun joueur ne participe ou un nombre impair de joueurs \nMerci d'ajouter des joueurs.")
                            Controle_app.main_menu()
                        else:
                                if tournoi.num_round=="" or tournoi.num_round not in ["1","2","3","4"]:
                                    print("Il manque le nombre de match pour ce tournoi ou bien trop de matches (>4).")
                                    print("Prière de changer cette données avant de continuer.")
                                    print("Retour au Menu Principal...")

                                    Controle_app.main_menu()
                                else:
                                    choice=""
                                    while choice not in ["1","2","3"]:
                                        choice=input("(1) Matches virtuels aléatoires"
                                                    "\n(2) Matches réels et saisie clavier"
                                                    "\n(3) Retour au Menu" 
                                                    "\n>>>")
                                        if choice=="1":
                                            tournoi.play_round("random")
                                        if choice=="2":
                                            tournoi.play_round("input")    
                                        if choice=="3": 
                                            Controle_app.main_menu()  
                                        print("MATCHES :")
                                        print(tournoi.show_matches())
                                        ask_save=input("Vous voulez sauvegarder ce round (o/n) ?")
                                        if ask_save=="o":
                                            Controle_app.record()
                                            tournoi.change_specific_data(chosen_tournament, name_file="tournament_data.json", key_1="matches", new_value=tournoi.matches)
                                        else:
                                            Controle_app.main_menu()
                    if sub_choice=="4":
                        Controle_app.main_menu()
                    
                    if sub_choice=="5":
                        exit()
#MODELE
    def list_of_tournament (file_name):
        text=""
        try:
            with open(file_name, 'r',encoding='utf-8') as fichier_json:
                all_datas = json.load(fichier_json)
                
        except FileNotFoundError:
            # Si le fichier n'existe pas, initialiser une liste vide
            all_datas = '"tournaments": {"1": {}}'
        
        list = []

# Parcourir les tournois dans le dictionnaire
        if not all_datas:
             all_datas = '"tournaments": {"1": {}}'
        for tournament_id, tournament_data in all_datas['tournaments'].items():
            text+= str(tournament_id)+ " - " + tournament_data['name']+"\n"

# Afficher la liste des identifiants et des noms de tournois
        return text,tournament_id

        
class Tournament:
    def __init__(self,id="id",name="",location="",start="",end="",num_round="",description="",players=[],matches=[]):
        self.id=id
        self.name=name
        self.location=location
        self.start=start
        self.end=end
        self.num_round=num_round
        self.description=description
        self.matches=matches
        self.players=players
        
#MODELE
    def change_specific_data(self,tournament, name_file, key_1, new_value):
        with open(name_file, 'r', encoding='utf-8') as file:
            data = json.load(file)

            data["tournaments"][tournament][key_1] = new_value
    
    # Sauvegarder les données modifiées dans le fichier JSON
        with open(name_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

#MODELE
    def change_data_file (self,tournament,name_file,new_dict):
        """Changer des données dans un fichier : données de base (pas joueurs, ni tournois joués)"""
        #name_file = "tournament_data.json"

        try:
            with open(name_file, 'r', encoding='utf-8') as fichier_json:
                all_datas = json.load(fichier_json)
                print(all_datas)
        except json.JSONDecodeError:
            all_datas = {}
        except FileNotFoundError:
            all_datas = []

        all_datas['tournaments'][tournament] = new_dict

        # Réécrire les données mises à jour dans le fichier JSON
        with open(name_file, 'w', encoding='utf-8') as fichier_json:
            json.dump(all_datas, fichier_json, indent=4)

    #VIEW
    def choose_participants(self,tournament):
         chosen_list=[]
         current_players=", ".join(self.players)
         print("Voici la liste des joueurs actuellement enregistrés :"
               +"\n"+current_players+
               "\nTapez Entrée si vous excluez le joueur"
               "\nTapez x ou X si vous incluez le joueur.")
         file_name="players_database.json"
         all_players = self.get_list_player_json("players_database.json")
         for player in all_players:
              decision=input(player+" "*(20-len(player))+"  : ")
              if decision=="x" or decision=="X":
                chosen_list.append(player)
         text_chosenlist=", ".join(chosen_list)
         if len(chosen_list)<2 or len(chosen_list) % 2 != 0 :
              print("Liste trop courte ou nombre de participants impair.")
              self.choose_participants(tournament)
         print("Voici la liste des joueurs demandée : "+text_chosenlist)
         
         print("(1) Confirmer et sauvegarder"
         "\n(2) Annuler et retour au Menu")  
         
         decision =""
         while decision not in ["1","2"]:
               decision = input("Votre décision >>> ")
               if decision == "1":
                    #Modification spécifique de la liste des joueurs pour le tournoi en cours
                    self.change_specific_data(tournament,name_file="tournament_data.json",key_1="players",new_value=chosen_list)
                    Controle_app.record()

                    print("Merci. La nouvelle liste de participant(e)s est enregistrée.")
                    print("")
                    Controle_app.main_menu()
                        
               if decision == "2" :
                    Controle_app.main_menu()
                
    #CONTROLE
    def play_round_suspendu(self,input_or_random):
        save_list=[]
        player=[]
        sub_list=[]
        past_matches=[]
        score1=0
        score2=0
        list_players=self.players
        
        score=[0]*len(self.players)
        all_past=[]
        storage_score=dict(zip(self.players, score))

        nbre=int(len(self.players))
        tours=int(self.num_round)

        for turn in range (0,tours):  
            sub_list=[]
            for i in range(0,nbre,2):
                    
                        player1=list_players[i]
                        player2=list_players[i+1]
                        print(player1+" VERSUS "+player2)
                        #current_match=Match(player1,player2)
                        #current_match.play_match_random()
                        if input_or_random=="input":
                        
                            score1,score2 = Controle_app.play_match_input(player1,player2)
                        elif input_or_random=="random":
                             score1,score2 = Controle_app.play_match_random(player1,player2)
                        #current_match.pair=([player1,current_match.sc1],[player2,current_match.sc2])
                        #score1+=current_match.sc1
                        #list_players[i+1].birthday+=current_match.sc1
                        #print(player1+" "+str(sc1))
                        print("cours de route")
                        print(list_players[i])
                        print(str(score1))
                    
                        #print(current_match.pair)
                        #Sélection des deux premiers participants de la liste
                        sub_list.append(([player1,score1],[player2,score2]))

                        #On ajoute à la liste des paires déjà jouées la paire actuelle
                        past_matches.append({player1,player2})

                        storage_score[player1] += score1
                        storage_score[player2] += score2
            
            #new_list=sorted(storage_score, key=lambda k: storage_score[k], reverse=True)
            new_list=self.ranking_players()
            list_players=new_list      
            #tester les doublons et modifier la liste si c'est le cas
            list_players=generate_set_players(input_list=new_list,past_matches=past_matches)
            
            #print("new list")
            #print(new_list)
            #print("sublist")
            #print(sub_list)

            save_list.append(sub_list)
        all_past.append(past_matches)
  
        
        print("la save list à enregistrer dans le fichier")
        self.matches=save_list
        #print(self.matches)
        
        #self.change_specific_data(tournament="1", name_file="tournament_data.json", key_1="matches", new_value=self.matches)

        return(new_list,save_list)
    
    def play_round(self,input_or_random):
        save_list=[]
        player=[]
        sub_list=[]
        past_matches=[]
        score1=0
        score2=0

        list_players=self.players
        
        score=[0]*len(self.players)
        all_past=[]
        storage_score=dict(zip(self.players, score))

        nbre=int(len(self.players))
        tours=int(self.num_round)

        for turn in range (0,tours):  
            sub_list=[]
            for i in range(0,nbre,2):
                    
                        player1=list_players[i]
                        player2=list_players[i+1]
                        print(player1+" VERSUS "+player2)
                        #current_match=Match(player1,player2)
                        #current_match.play_match_random()
                        if input_or_random=="input":  
                            score1,score2 = Controle_app.play_match_input(player1,player2)
                        elif input_or_random=="random":
                             score1,score2 = Controle_app.play_match_random(player1,player2)
                     
                        sub_list.append(([player1,score1],[player2,score2]))

                        #On ajoute à la liste des paires déjà jouées la paire actuelle
                        past_matches.append({player1,player2})

                        storage_score[player1] += score1
                        storage_score[player2] += score2
            
            new_list=sorted(storage_score, key=lambda k: storage_score[k], reverse=True)
                 
            #tester les doublons et modifier la liste si c'est le cas
            #list_players=generate_set_players(new_list,past_matches)
            
          
            save_list.append(sub_list)
            list_players=generate_set_players(new_list,past_matches)
            #self.change_specific_data("tournament_data.json",key_1="matches",new_value=save_list)
        all_past.append(past_matches)
  
        
        print("la save list à enregistrer dans le fichier")
        self.matches=save_list
        #print(self.matches)
        
        #self.change_specific_data(tournament="1", name_file="tournament_data.json", key_1="matches", new_value=self.matches)

        return(new_list,save_list)


#MODELE
    def get_list_player_json_2(self,name_file):
        
        players=[]

        data={}
        data = read_filejson(name_file)
      
        for player_data in data["joueurs"]:
            player=Player(player_data["surname"],player_data["firstname"],player_data["birthday"])
            self.players.append(player.surname)
        return(self.players)

#VIEW
    def show_basic_tournament(self):
        categories=["Nom","Lieu","Date de début","Date de fin","Nombre de rounds","Description"]
        datas=[self.name,self.location,self.start,self.end,self.num_round,self.description]
        for item1,item2 in zip (categories,datas):
             if len(item1)<20:
                  item1=item1+" "*(20-len(item1))
             print(item1+" : "+item2)
        print("JOUEURS              : "+self.show_players()) 
        print("MATCHES :")
        print(self.show_matches())
        
        print(self.show_ranking())
    
#VUE
    def input_data_tournament(self,tournament):
        dictio={}
        input_text=["Nom","Lieu","Date de début","Date de fin","Nombre de rounds","Description"]
        categories=["name","location","start","end","num_round","description"]
        already=[self.name,self.location,self.start,self.end,self.num_round,self.description]
        #current_datas=load_tournament_from_json("tournoi 1","tournament_data.json")
        dictio["players"]=self.players
        dictio["matches"]=self.matches
        print("Entrez les données du Tournoi." 
              "\nLa valeur par défaut est entre parenthèses"
              "\nTapez sur Entrée si pas de changement (valeur par défaut)"
              "\nChiffre entre 1 et 4 pour le nombre de rounds. \nMerci."
              "\n TOURNOI #"+str(tournament))
        for item1, item2,item3 in zip(input_text, categories, already):
            asked=item1+" - ("+str(item3)+")"
            if len(asked)<30:
                  asked=asked+" "*(30-len(asked))+":"
            new_data=input(asked)
            #si on change rien, donnée reste la même
            if new_data=="":
                dictio[item2]=item3
            else:
                dictio[item2]=new_data
             
            #ne pas toucher aux clés players et rounds
            #ajouter save specific
        

        print("nouvelles données entrées")
        for cle, valeur in dictio.items():
            
            print(f" {cle} : {valeur}")
        confirmation=""
        while confirmation not in ["o","n"]:
            confirmation=input("Voulez-vous sauvegarder ces changements du Tournoi # "+str(tournament)+ " (o/n)?\n>>>")
            
            if confirmation == "n":
                    Controle_app.main_menu()
            elif confirmation == "o":
                self.change_data_file(tournament,name_file="tournament_data.json",new_dict=dictio)
            
        return dictio
        
#A VOIR POUBELLE
    def choose_player(self,tournament,file_name):
            liste=[]
            # Liste d'éléments
            elements = self.get_list_player_json(file_name)
           
            # Fonction qui va être appelée lorsque l'on appuie sur "Enregistrer"
            def fermer():
                # Stocker la sélection dans l'attribut de l'instance
                #self.players = [listbox[i] for i in range(len(listbox)) if var[i].get() == 1]
                self.players=[listbox[i] for i in range(len(listbox)) if var[i].get() == 1]
                print("alors")
                for u in self.players:
                     liste.append(u)
                print(self.players)  # Affiche les joueurs sélectionnés
                print(liste)
                #enregistrer dans fichier json
                
                #self.change_specific_data("tournoi 1","tournament_data.json","players",liste)
                fenetre.quit()  # Ferme la fenêtre
                

            # Créer la fenêtre principale
            fenetre = tk.Tk()
            fenetre.title("Sélection d'éléments")

            # Créer une liste pour les variables de chaque case à cocher
            var = []
            
            # Créer une case à cocher pour chaque élément de la liste
            listbox = []
            for element in elements:
                var_element = tk.IntVar()  # Variable pour savoir si la case est cochée (1) ou non (0)
                var.append(var_element)
                checkbox = tk.Checkbutton(fenetre, text=element, variable=var_element)
                checkbox.pack(anchor="w")  # Ajouter la case à cocher à la fenêtre
                listbox.append(element)  # Ajouter l'élément à la liste des éléments

            # Bouton pour enregistrer les sélections
            button_enregistrer = tk.Button(fenetre, text="Enregistrer", command=fermer)
            button_enregistrer.pack()

            # Lancer la boucle principale de la fenêtre
            fenetre.mainloop()
#modele
    def get_list_player_json(self,name_file):
        with open(name_file,"r",encoding="utf-8") as file:
            data_1=json.load(file)
            
        #data_players=json.load(data_1)
        #for i in range (0,len(players)):
      
        #players=[]
    
        list = [joueur["surname"] for joueur in data_1["joueurs"]]
        return(list)
    

    #trash
    def show_players(self):
         text=""
         for player in self.players:
              text+=player+", "
         text=text[:-2]
         return(text)
    
    def show_ranking(self) :
         all_matches=self.matches
         the_players=self.players
         the_scores=[0]*len(self.players)
         text="CLASSEMENT :"
        # Faire un dictionnaire avec joueurs en clé et score en valeur pour 
        # extraire les données contenues dans l'archivage des parties
        # et faire un cumul pour chaque joueur afin de faire un classement
         ranked_players=dict(zip(the_players, the_scores))

         for match in all_matches : 
                
                for m in match:
                    ranked_players [m[0][0]] += m[0][1]
                    ranked_players [m[1][0]] += m[1][1]
        
         sorted_players={k: v for k, v in sorted(ranked_players.items(), key=lambda item: item[1], reverse=True)}

         for key in sorted_players:
            text+=f"{key} ({sorted_players[key]}),"
         text=text[:-1]
         return(text)            
#UNFOLD LA LISTE DES PARTIES SAUVEES
    def show_matches (self):
        all_matches=self.matches
        text=""
        match=[]
        list_players=[]
        #print(all_matches)
        t=1
        
        for match in all_matches : 
                text+="\n   ROUND # "+str(t)+"\n"
                for m in match:
    
                     text+=m[0][0]+" vs "+m[1][0]+" "*(20-(len(m[0][0]+" vs "+m[1][0])))+" : "+str(m[0][1])+ "-"+str(m[1][1])+"\n"
                     
                        
                t=t+1 
        return(text)
     
    
    #UNFOLD LA LISTE DES PARTIES SAUVEES
    def ranking_players (self):
        all_matches=self.matches

        score_players={}
        #print(all_matches)
        t=1
        for match in all_matches : 
                text+="\nRound"+str(t)+"\n"
                for m in match:
                     
                     score_players[m[0][0]]+=m[0][1]
                     score_players[m[1][0]]+=m[1][1]                
                        

                t=t+1 
        ranking_players=sorted(score_players, key=score_players.get, reverse=True)
        return(ranking_players)



#à voir
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

def load_tournament_from_json(tournament,filename):
    # Ouvre le fichier JSON et charge les données
    with open(filename, "r",encoding='utf-8') as file:
        all_datas = json.load(file)
        
    print (type(all_datas))
    
    data = all_datas["tournaments"][tournament]
    # Crée une instance de Person en utilisant les données du fichier JSON
    ongoing_tournament = Tournament(name=data.get("name",""), location=data.get("location",""), start=data.get("start","")\
                                         ,end=data.get("end",""),num_round=data.get("num_round",""),description=data.get("description","")\
                                            ,players=data.get("players",""),matches=data.get("matches",""))

    return ongoing_tournament


list_round=[]

test=load_tournament_from_json("1","tournament_data.json")
#test.play_round_random()
Controle_app.main_menu()
#test.input_data_tournament("1")


#========================================================================================================
#========================================================================================================
#========================================================================================================


