import json
from TournamentView import TournamentView
from TournamentModel import TournamentModel
from Player import Player

class TournamentControl:

    def choice_tournament(file_name):
        TournamentView.show_list_tournament()
        choice=TournamentView.input_chosen_tournament()
        if choice == "0":
            pass
            #current_tournament = TournamentModel()
            #TournamentView.input_data_tournament(current_tournament,
             #   tournament=str(int(last_one)+1))
        else:
            TournamentControl.menu_tournament_controller(index_tournament=choice)


    def menu_tournament_controller(index_tournament):
            choice=TournamentView.menu_tournament(index_tournament)
            if choice == "1":
                TournamentView.input_data_tournament(
                    current_tournament, index_tournament)
            if choice == "2":
                TournamentView.change_participants(
                    current_tournament, tournament=index_tournament)
            if choice == "3":
                        TournamentControl.input_new_round(
                            index_tournament, current_tournament)
            if choice == "4":
                TournamentView.main_menu()
            if choice == "5":
                
                list=Player.get_list_player_json("players_database.json")
                list_players=Player.extract_list_players(list)
                Player.change_player(current_list=list_players)
        return ()


    def check_conditions_new_round(index_tournament, current_tournament):
        x,y,z,w=current_tournament.get_matches()
        if current_tournament.players in [None, '', [], {}, ()] or len(current_tournament.players) == 0 or len(current_tournament.players) % 2 != 0:
                    print(
                        "Aucun joueur ne participe ou un nombre impair de joueurs \nMerci d'ajouter des joueurs.")
                    TournamentView.menu_tournament(index_tournament)
        if current_tournament.num_round == "" or current_tournament.num_round not in ["1", "2", "3", "4"]:
                        print(
                            "Il manque le nombre de match pour ce tournoi ou bien trop de matches (>4).")
                        print("Prière de changer cette données avant de continuer.")
                        print("Retour au Menu Principal...")
                        TournamentView.menu_tournament(index_tournament)
        if current_tournament.num_round == w:
                        print ("Tous les matches ont déjà été joués pour ce tournoi.")
                        TournamentView.menu_tournament(index_tournament)
        else:
             return

    def generate_set_players(list_to_check, sets_of_past_matches):

        generated_list = []
        a = 0
        b = 1
        item_1 = list_to_check[a]
        item_2 = list_to_check[b]
        pair = {item_1, item_2}
        while len(list_to_check) > 1:
            item_1 = list_to_check[0]
            item_2 = list_to_check[1]
            pair = {item_1, item_2}
            if pair in sets_of_past_matches:
                for second_item in range(2, len(list_to_check)):
                    item_1 = list_to_check[0]
                    item_2 = list_to_check[second_item]
                    pair_t = {item_1, item_2}
                    if pair_t not in sets_of_past_matches and second_item <= len(list_to_check):
                        generated_list.append(item_1)
                        generated_list.append(item_2)
                        list_to_check.remove(item_1)
                        list_to_check.remove(item_2)
                        break
                    if pair_t in sets_of_past_matches and second_item == len(list_to_check):
                        item_1 = list_to_check[0]
                        item_2 = list_to_check[1]
                        generated_list.append(item_1)
                        generated_list.append(item_2)
                        list_to_check.remove(item_1)
                        list_to_check.remove(item_2)
                        break
                    if pair_t in sets_of_past_matches and second_item < len(list_to_check):
                        continue
            else:
                generated_list.append(item_1)
                generated_list.append(item_2)
                list_to_check.remove(item_1)
                list_to_check.remove(item_2)
        return (generated_list)

    def play_one_round(current_tournament,turn,save_list):

        view_matches,score_players,already_played,counter_round=current_tournament.get_matches()
        print("liste joueurs dico")
        print(y)
        print("liste triée")
        print(sorted(score_players, key=lambda x: score_players[x], reverse=True))
        print("matches jouées")
        print(already_played)
        if turn == 1:
                list_players=current_tournament.players
        if turn == 2:
                list_players = sorted(score_players, key=lambda x: score_players[x], reverse=True)
        if turn > 2:
                # On appelle la fonction qui vérifie si déjà jouée et crée nouvelle paire si oui
                # Elle renvoie une liste avec des paires non déjà jouées
                list_players = TournamentControl.generate_set_players(
                    sorted(score_players, key=lambda x: score_players[x], reverse=True), past_matches=already_played)

        nbre = int(len(current_tournament.players))
        print(f"ROUND # {str(turn)}")
        sub_list = []
        for i in range(0, nbre-1, 2):
                player1 = list_players[i]
                player2 = list_players[i+1]
                score1, score2 = TournamentView.play_match(
                    id_player1=player1, id_player2=player2)
                sub_list.append(([player1, score1], [player2, score2]))
        save_list.append(sub_list)
        current_tournament.matches = save_list    
        return (list_players, save_list)
    
    def input_new_round(tournament, current_tournament):
        view_matches,score_players,already_played,counter_round=current_tournament.get_matches()
        print(" ♗ MATCHES :")
        print(TournamentView.matches_already_played(tournament, current_tournament))
        TournamentControl.check_conditions_new_round(tournament, current_tournament)
        print ("NOUVEAU ROUND")
        list_players, current_tournament.matches = TournamentControl.play_one_round(current_tournament,turn=counter_round,save_list=current_tournament.matches)
        
        print("SAUVEGARDE")
        ask_save = input(
            f"Vous voulez sauvegarder ce round (o/n) ?")
        if ask_save == "o":
            TournamentModel.save_match(tournament,current_tournament)
        else:
            TournamentView.main_menu()
