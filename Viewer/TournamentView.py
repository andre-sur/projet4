import time
from datetime import datetime
import re
import json
from Player import Player
from pathlib import Path
from TournamentModel import TournamentModel

class TournamentView:

    def show_list_tournament(file_name):
        all_tournaments = TournamentModel.list_of_tournament(
            file_name)
        print("\n♙LISTE DES TOURNOIS")
        for tournament in all_tournaments:
            print(tournament)
    
    def input_chosen_tournament(file_name):
        all_tournaments = TournamentModel.list_of_tournament(
            file_name)
        last_one=len(all_tournaments)
        chosen_tournament = ""
        list_options = [str(i) for i in range(0, int(last_one) + 1)]
        while chosen_tournament not in list_options:
            chosen_tournament = input(
                "Quel tournoi ? (0 pour en créer un) >>>")

        return(chosen_tournament)
           

    def menu_tournament(index_tournament):
        current_tournament=TournamentView.show_basic_tournament(index_tournament)
        #x,y,z,w=current_tournament.get_matches()
        choice = ""
        while choice not in ["1", "2", "3", "4"]:
            choice = input("  (1) Modifier ce tournoi (données de base) "
                           "\n  (2) Ajouter/Modifier la liste des participants"
                           f"\n  (3) Jouer le match #  (total {current_tournament.num_round})"
                           "\n  (4) Quitter l'application."
                           "\n   >>>")
            return(choice)
            
    def matches_already_played(index_tournament):
        current_tournament = TournamentModel.load_tournament_from_json(
        index_tournament, "tournament_data.json")
        view_matches,score_players,already_played,counter_round=current_tournament.get_matches()
        print("MATCHES DEJA JOUES")
        return(view_matches)
        
    def main_menu():
        file_name="tournament_data.json"
        print("♔  CHESS TOURNAMENT MANAGER ♔ \n♖  MENU PRINCIPAL ♖")
        print("1> Gestion des joueurs")
        print("2> Gestion des tournois")
        print("3> Quitter")
        choice=""
        while choice not in ["1","2","3"]:
            choice=input("Votre choix >>>")
        return(choice)
            
    def choose_participants(index_tournament):
        current_tournament = TournamentModel.load_tournament_from_json(
        index_tournament, "tournament_data.json")
        chosen_list = []
        current_players = ", ".join(current_tournament.players)
        print("Voici la liste des joueurs actuellement enregistrés :"
              f"\n{current_players}"
              "\nTapez Entrée si vous excluez le joueur"
              "\nTapez x ou X si vous incluez le joueur.")
        all_data = Player.get_list_player_json("players_database.json")
        all_players=Player.extract_list_players(all_data)
        for player in all_players:
            decision = input(player.firstname+" "+player.surname+" ["+player.id_number+"]"+" "*(30-(len(player.firstname)+len(player.id_number)+len(player.surname)))+"  : ")
            if decision == "x" or decision == "X":
                chosen_list.append(player.id_number)
        text_chosen_list = ", ".join(chosen_list)
        return (chosen_list,text_chosen_list)
        
    def ask_save_or_not(text_chosen_list):
        print(f"Voici la liste des joueurs demandée : {text_chosen_list}")
        print("(1) Confirmer et sauvegarder"
              "\n(2) Annuler et retour au Menu")
        decision = ""
        while decision not in ["1", "2"]:
            decision = input("Votre décision >>> ")
        return decision

    def show_basic_tournament(index_tournament):
        current_tournament = TournamentModel.load_tournament_from_json(
                index_tournament, "tournament_data.json")
        categories = ["Nom", "Lieu", "Date de début",
                      "Date de fin", "Nombre de rounds", "Description"]
        datas = [current_tournament.name, current_tournament.location, current_tournament.start,
                 current_tournament.end, current_tournament.num_round, current_tournament.description]
        for item1, item2 in zip(categories, datas):
            if len(item1) < 20:
                item1 = item1+" "*(20-len(item1))
            print(f"{item1} : {item2}")
        participants=TournamentModel.list_of_participants(current_tournament)
        print(
            f"Participants au tournoi ({current_tournament.name}) :\n{participants}")
        print(f"TOTAL ROUNDS ({str(current_tournament.num_round)}")
        return(current_tournament)
        
       # print(self.get_ranking())
    def view_data_tournament(current_tournament, tournament):
        label_data = ["Nom", "Lieu", "Date de début",
                      "Date de fin", "Nombre de rounds", "Description"]
        corresponding_data = [current_tournament.name, current_tournament.location, current_tournament.start,
                         current_tournament.end, current_tournament.num_round, current_tournament.description]
        for item1, item2 in zip(label_data,corresponding_data):
            print(item1 + " " * (30-len(item1)) + ":"+ item2)


    def input_data_tournament(index_tournament):
        current_tournament = TournamentModel.load_tournament_from_json(
        index_tournament, "tournament_data.json")
        input_data = {}
        input_text = ["Nom", "Lieu", "Date de début",
                      "Date de fin", "Nombre de rounds", "Description"]
        categories = ["name", "location", "start",
                      "end", "num_round", "description"]
        existing_data = [current_tournament.name, current_tournament.location, current_tournament.start,
                         current_tournament.end, current_tournament.num_round, current_tournament.description]
        input_data["players"] = current_tournament.players
        input_data["matches"] = current_tournament.matches
        print("Entrez les données du Tournoi."
              "\nLa valeur par défaut est entre parenthèses"
              "\nTapez sur Entrée si pas de changement (valeur par défaut)"
              "\nChiffre entre 1 et 4 pour le nombre de rounds. \nMerci."
              f"\n Ce tournoi sera numéroté : #{str(index_tournament)}")
        for item1, item2, item3 in zip(input_text, categories, existing_data):
            data_update = f"{item1} - ({str(item3)})"
            if len(data_update) < 30:
                data_update = data_update + " " * (30-len(data_update)) + ":"
                new_data=""
                check_answer=False
            while check_answer ==False:
                new_data = input(data_update)
                if new_data == "":
                    input_data[item2] = item3
                    check_answer=True
                elif (item2=="start" or item2=="end") and TournamentModel.check_format_date(new_data)==False:
                    print("Le format de la date est incorrect. Il doit être : JJ-MM-AAAA")
                    check_answer=False 
                elif item2=="end" and new_data < input_data["start"]:
                    print("La date de fin doit être ultérieure à celle de début")
                    check_answer=False
                else:
                    input_data[item2] = new_data
                    check_answer=True
        
        TournamentView.save_basic_datas(input_data,index_tournament)
        return input_data

    def save_basic_datas (input_data,index_tournament):
       
        confirmation = ""
        while confirmation not in ["o", "n"]:
            confirmation = input(
                f"Voulez-vous sauvegarder ces changements du Tournoi # {str(index_tournament)} (o/n)?\n>>>")
            if confirmation == "n":
                TournamentView.main_menu()
            elif confirmation == "o":
                TournamentModel.change_tournament_record(
                    tournament=index_tournament, name_file="tournament_data.json", new_dict=input_data)
                TournamentView.record()
                TournamentView.main_menu()
        
    def record():
        print("Enregistrement en cours...")
        time.sleep(1)
        print("Sauvegarde dans un fichier Json...")
        time.sleep(2)
        print("Enregistrement confirmé.")

    
    def play_match(id_player1, id_player2):

        name_player1=Player.find_name_with_code (id_player1)
        name_player2=Player.find_name_with_code (id_player2)

        choice = f"1.{name_player1} [{id_player2}] a gagné \n2.{name_player2} [{id_player2}] a gagné \n0. Match nul. \n>>>"
        result = ""
        while result not in ["1", "2", "0"]:
            result = input(choice)
        if result == "1":
            score1 = 0
            score2 = 1
        if result == "2":
            score1 = 1
            score2 = 0
        if result == "0":
            score1 = 0.5
            score2 = 0.5
        return (score1, score2)