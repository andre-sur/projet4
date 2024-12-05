import random
import time
import json
import tkinter as tk
from tkinter import ttk
from pathlib import Path

# LES MODELES
class Player:

    def __init__(self,surname,firstname,birthday):
        self.surname=surname
        self.firstname=firstname
        self.birthday=birthday 
    
    def add_player():
         pass

class Match:
    def __init__(self,j1,j2):
        self.j1=j1
        self.j2=j2
        self.sc1=None
        self.sc2=None
        self.pair=None

class General :

    def generate_set_players (input_list,past_matches):
        output_list=[]
        list_tocheck=input_list.copy()
        a=0
        b=1
        item_1=list_tocheck[a]
        item_2=list_tocheck[b]
        print("élément 1"+item_1)
        print("élément 2"+item_2)
        pair={item_1,item_2}
        
        while len(list_tocheck)>0:
            item_1=list_tocheck[0]
            item_2=list_tocheck[1]
            pair={item_1,item_2}
            if pair in past_matches:
            
                for second_item in range (2,len(list_tocheck)):
                    item_1=list_tocheck[0]
                    item_2=list_tocheck[second_item]
                    pair_t={item_1,item_2}
                    if pair_t not in past_matches and second_item<=len(list_tocheck):
                        output_list.append(item_1)
                        output_list.append(item_2)
                        list_tocheck.remove(item_1)
                        list_tocheck.remove(item_2)
                        break
                    if pair_t in past_matches and second_item==len(list_tocheck):      
                        item_1=list_tocheck[0]
                        item_2=list_tocheck[1]
                        output_list.append(item_1)
                        output_list.append(item_2)
                        list_tocheck.remove(item_1)
                        list_tocheck.remove(item_2)
                        break
                    if pair_t in past_matches and second_item<len(list_tocheck):
                        continue
                        
            else:    
                output_list.append(item_1)
                output_list.append(item_2)
                list_tocheck.remove(item_1)
                list_tocheck.remove(item_2)
    
        return(output_list)

    
    #DETERMINATION DU RESULTAT D'UN MATCH : SAISIE OU ALEATOIRE
    def play_match(mode,player1,player2):
        
        if mode=="random":
        #Jet de dé à 3 résultats équiprobables possibles
           result = str(random.randint(0, 2))

        if mode=="input":
            text="1. "+player1+" 2."+player2+" 0. Match nul. >>>"
            result=""
            while result not in ["1","2","0"]:
                result=input(text)

        #Player 1 gagne si dé=1
        if result =="1":
                score1=0
                score2=1

        #Player 2 gagne si dé=2 
        if result =="2":
                score1=1
                score2=0

        #Match nul si dé = 0        
        if result =="0":
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
     
            else:
                 if not Path(file_name).exists():
                      print("Ce fichier n'existe pas. \nNous utiliserons : ")
                      print("Le fichier par défaut: tournament_data.json")  
                      file_name="tournament_data.json"
                      
            #Appel à fonction pour récupérer la liste des tournois et le numéro du dernier enregistré 
            #(donc quantité total de tournois)
            all_tournaments,last_one=General.list_of_tournament(file_name)

            print("\nLISTE DES TOURNOIS")
            print(all_tournaments)
            #Une liste des numéros pour vérifier que l'input est l'un d'eux
            chosen_tournament=""
            list_options=[str(i) for i in range(0, int(last_one) + 1)]
            while chosen_tournament not in list_options:
                chosen_tournament=input("Quel tournoi ? (0 pour en créer un) >>>")
                
            if chosen_tournament=="0":
                        tournoi=Tournament()
                        tournoi.input_data_tournament((str(int(last_one)+1)))
            else:   
                    tournoi=General.load_tournament_from_json(chosen_tournament,file_name)
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
                        print("Avant de modifier la liste des joueurs, il faut effacer les matches."
                              "Effacer les matches (o/n)?")
                        decision=input(">>>")
                        if decision == "o" :
                            tournoi.delete_matches(chosen_tournament)
                            tournoi.choose_participants(chosen_tournament)
                        else :
                             General.main_menu()
                    if sub_choice=="3":
                        if tournoi.players in [None, '', [], {}, ()] or len(tournoi.players)==0 or len(tournoi.players)% 2 != 0:
                            print("Aucun joueur ne participe ou un nombre impair de joueurs \nMerci d'ajouter des joueurs.")
                            General.main_menu()
                        else:
                                if tournoi.num_round=="" or tournoi.num_round not in ["1","2","3","4"]:
                                    print("Il manque le nombre de match pour ce tournoi ou bien trop de matches (>4).")
                                    print("Prière de changer cette données avant de continuer.")
                                    print("Retour au Menu Principal...")

                                    General.main_menu()
                                else:
                                    choice=""
                                    while choice not in ["1","2","3"]:
                                        choice=input("(1) Matches virtuels aléatoires"
                                                    "\n(2) Matches réels et saisie clavier"
                                                    "\n(3) Retour au Menu" 
                                                    "\n>>>")
                                        if choice=="1":
                                            time.sleep(1)
                                            print("Détermination aléatoire des scores")
                                            time.sleep(1)
                                            tournoi.play_round("random")       
                                        if choice=="2":
                                            time.sleep(1)
                                            print("Saisie manuelle des scores")
                                            time.sleep(1)
                                            tournoi.play_round("input")    
                                        if choice=="3": 
                                             General.main_menu()  
                                        print("MATCHES :")
                                        print(tournoi.show_matches())
                                        ask_save = input("Vous voulez sauvegarder ces "+tournoi.num_round+" rounds (o/n) ?")
                                        if ask_save == "o":
                                            General.record()
                                            tournoi.change_specific_data(chosen_tournament, name_file="tournament_data.json", key_1="matches", new_value=tournoi.matches)
                                            General.main_menu()
                                        else:
                                            General.main_menu()
                    if sub_choice == "4":
                        General.main_menu()
                    if sub_choice == "5":
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
    
    # SIMULATEUR D'ENREGISTREMENT
    def record():
        print("Enregistrement en cours...")
        time.sleep(1)
        print("Sauvegarde dans un fichier Json...")
        time.sleep(2)
        print("Enregistrement confirmé.")

        
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

    def delete_matches (self,tournament):
         print("Les matches sont tous effacés.")
         self.change_specific_data(tournament,name_file="tournament_data.json",key_1="matches",new_value=[])

    def change_data_file (self,tournament,name_file,new_dict):
        try:
            with open(name_file, 'r', encoding='utf-8') as fichier_json:
                all_datas = json.load(fichier_json)          
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
              print("Liste trop courte (<2) ou nombre de participants impair."
                    "\nMerci de recommencer.\n_____________________")
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
                    General.record()

                    print("Merci. La nouvelle liste de participant(e)s est enregistrée.")
                    print("")
                    General.main_menu()
                        
               if decision == "2" :
                    General.main_menu()

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
        #initialisation d'un dictionnaire avec liste des joueurs et scores à zéro 
        # (pour archiver les scores du match en cours)
        storage_score=dict(zip(self.players, score))

        nbre=int(len(self.players))
        tours=int(self.num_round)
      
        for turn in range (0,tours):  
            print("ROUND # "+str(turn))
            sub_list=[]
            for i in range(0,nbre-1,2):
                    
                        player1=list_players[i]
                        player2=list_players[i+1]

                        if input_or_random=="input":  
                    
                            score1,score2 = General.play_match (mode="input",player1=player1,player2=player2)
                        elif input_or_random=="random":
                             score1,score2 = General.play_match(mode="random",player1="",player2="")
                     
                        sub_list.append(([player1,score1],[player2,score2]))

                        #On ajoute à la liste des paires déjà jouées la paire actuelle
                        # (pour comparaison ultérieure)
                        past_matches.append({player1,player2})

                        storage_score[player1] += score1
                        storage_score[player2] += score2
            
            #La liste pour prochain round se compose des meilleurs joueurs (ordre décroissant)
            new_list=sorted(storage_score, key=lambda k: storage_score[k], reverse=True)
                 
            save_list.append(sub_list)
            #faire une exception pour le premier tour
            #pour lequel on ne compare pas avec les matches précédents
            if turn==0:
                 list_players=new_list
                 
            if turn>0:
                #On appelle la fonction qui vérifie si déjà jouée et crée nouvelle paire si oui
                #Elle renvoie une liste avec des paires non déjà jouées
                list_players=General.generate_set_players(new_list,past_matches)
    
        all_past.append(past_matches)

        self.matches=save_list
     
        return(list_players,save_list)


#VIEW
    def show_basic_tournament(self):
        categories=["Nom","Lieu","Date de début","Date de fin","Nombre de rounds","Description"]
        datas=[self.name,self.location,self.start,self.end,self.num_round,self.description]
        for item1,item2 in zip (categories,datas):
             if len(item1)<20:
                  item1=item1+" "*(20-len(item1))
             print(item1+" : "+item2)
        print("Participants au tournoi ("+self.name+") : "+self.list_of_participants()) 
        print("MATCHES ("+str(self.num_round)+" rounds) :")
        print(self.show_matches())
        
        print(self.show_ranking())
    
#VIEW
    def input_data_tournament(self,tournament):
        dictio={}
        input_text=["Nom","Lieu","Date de début","Date de fin","Nombre de rounds","Description"]
        categories=["name","location","start","end","num_round","description"]
        already=[self.name,self.location,self.start,self.end,self.num_round,self.description]
     
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
             
        confirmation=""
        while confirmation not in ["o","n"]:
            confirmation=input("Voulez-vous sauvegarder ces changements du Tournoi # "+str(tournament)+ " (o/n)?\n>>>")
            
            if confirmation == "n":
                    General.main_menu()
            elif confirmation == "o":
                self.change_data_file(tournament,name_file="tournament_data.json",new_dict=dictio)
                General.record()
                General.main_menu()
            
        return dictio
        

#modele
    def get_list_player_json(self,name_file):
        with open(name_file,"r",encoding="utf-8") as file:
            data_1=json.load(file)
    
        list = [joueur["surname"] for joueur in data_1["joueurs"]]
        return(list)
    

    #trash
    def list_of_participants(self):
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
         text+="\n"
         return(text)            
#UNFOLD LA LISTE DES PARTIES SAUVEES
    def show_matches (self):
        all_matches=self.matches
        text=""
        match=[]
        list_players=[]
        t=1
        
        for match in all_matches : 
                text+="\n   ROUND # "+str(t)+"\n"
                for m in match:
    
                     text+=m[0][0]+" vs "+m[1][0]+" "*(20-(len(m[0][0]+" vs "+m[1][0])))+" : "+str(m[0][1])+ "-"+str(m[1][1])+"\n"       
                t=t+1 
        return(text)

def generate_set_players (input_list,past_matches):
    output_list=[]
    list_tocheck=input_list.copy()
    a=0
    b=1
    item_1=list_tocheck[a]
    item_2=list_tocheck[b]
    print("élément 1"+item_1)
    print("élément 2"+item_2)
    pair={item_1,item_2}
    
    while len(list_tocheck)>0:
        item_1=list_tocheck[0]
        item_2=list_tocheck[1]
        pair={item_1,item_2}
        if pair in past_matches:
        
            for second_item in range (2,len(list_tocheck)):
                item_1=list_tocheck[0]
                item_2=list_tocheck[second_item]
                pair_t={item_1,item_2}
                if pair_t not in past_matches and second_item<=len(list_tocheck):
                      output_list.append(item_1)
                      output_list.append(item_2)
                      list_tocheck.remove(item_1)
                      list_tocheck.remove(item_2)
                      break
                if pair_t in past_matches and second_item==len(list_tocheck):      
                    item_1=list_tocheck[0]
                    item_2=list_tocheck[1]
                    output_list.append(item_1)
                    output_list.append(item_2)
                    list_tocheck.remove(item_1)
                    list_tocheck.remove(item_2)
                    break
                if pair_t in past_matches and second_item<len(list_tocheck):
                     continue
                    
        else:    
            output_list.append(item_1)
            output_list.append(item_2)
            list_tocheck.remove(item_1)
            list_tocheck.remove(item_2)
  
    return(output_list)


General.main_menu()

