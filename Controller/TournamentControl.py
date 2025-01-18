from Viewer.TournamentView import TournamentView
from Model.TournamentModel import TournamentModel
from Controller.PlayerControl import PlayerControl


class TournamentControl:

    def main_menu_controller():
        choice = TournamentView.main_menu()
        # Gestion des joueurs (choix 1)
        if choice == "1":
            PlayerControl.change_player()
            TournamentControl.main_menu_controller()
        # Gestion des tournois (choix 2)
        if choice == "2":
            TournamentControl.choice_tournament(
                file_name="tournament_data.json")
        if choice == "3":
            exit()

    def choice_tournament(file_name):
        TournamentView.show_list_tournament("tournament_data.json")
        choice = TournamentView.input_chosen_tournament("tournament_data.json")
        # Ajouter un tournoi (option 0)
        if choice == "0":
            last_one = TournamentModel.quantity_tournaments(
                "tournament_data.json")
            TournamentControl.input_new_tournament(int(last_one)+1)
        # Modifier/afficher un tournoi existant (option x=numéro tournoi)
        else:
            TournamentControl.menu_tournament_controller(
                index_tournament=choice)

    def choice_of_participants(index_tournament):
        chosen_list, text_chosen_list = TournamentView.choose_participants(
            index_tournament)
        # Vérifier que nbre participants > 2 et impair
        if len(chosen_list) < 2 or len(chosen_list) % 2 != 0:
            TournamentView.display_text("Liste trop courte (<2) ou " +
                                        "nombre de participants impair." +
                                        "\nMerci de recommencer.\n")
            TournamentControl.choice_of_participants(index_tournament)
        else:
            decision = TournamentView.ask_save_or_not(text_chosen_list)
        # Option 1: sauver la nouvelle liste de participants
            if decision == "1":
                TournamentModel.change_specific_data(
                    tournament=index_tournament,
                    name_file="tournament_data.json",
                    key_to_change="players", new_value=chosen_list)
                TournamentView.record()
                TournamentView.display_text(
                    "Merci. La nouvelle liste de participant(e)s " +
                    "est enregistrée.\n")
                TournamentControl.menu_tournament_controller(index_tournament)
            # Option 2: annuler, retour menu tournoi
            if decision == "2":
                TournamentControl.menu_tournament_controller(index_tournament)
            # Option 2: annuler, retour menu principal
            if decision == "3":
                TournamentControl.main_menu_controller()

    def select_participants(index_tournament):
        TournamentView.display_text("Modifier la liste des participants" +
                                    " implique d'effacer tous les matches."
                                    "Effacer les matches (o/n)?")
        decision = input(">>>")
        if decision == "o":
            TournamentView.display_text("Les matches sont tous effacés.")
            TournamentModel.delete_matches(index_tournament)
            TournamentControl.choice_of_participants(index_tournament)
        else:
            TournamentControl.menu_tournament_controller(index_tournament)

    def input_save_data_tournament(index_tournament):
        current_tournament = TournamentModel.load_tournament_from_json(
            index_tournament, "tournament_data.json")
        input_data = TournamentView.input_data_tournament(current_tournament)
        TournamentControl.save_basic_datas(input_data, index_tournament)
        return input_data

    def input_new_tournament(index_tournament):
        current_tournament = TournamentModel()
        current_tournament.name = ""
        current_tournament.location = ""
        current_tournament.end = ""
        current_tournament.start = ""
        current_tournament.num_round = ""
        current_tournament.description = ""
        input_data = TournamentView.input_data_tournament(current_tournament)
        TournamentControl.save_basic_datas(input_data, index_tournament)
        return input_data

    def menu_tournament_controller(index_tournament):
        choice = TournamentView.menu_tournament(index_tournament)
        # Option 1: modifier tournoi
        if choice == "1":
            TournamentControl.input_save_data_tournament(
                index_tournament)
        # Option 2: modifier liste participants
        if choice == "2":
            TournamentControl.select_participants(
                index_tournament)
        # Option 3: jouer le match suivant
        if choice == "3":
            TournamentControl.input_new_round(
                index_tournament)
        # Option 4: voir matchs joués
        if choice == "4":
            TournamentView.matches_already_played(index_tournament)
            TournamentView.hit_enter("Tapez Entrée pour continuer.")
            TournamentControl.menu_tournament_controller(index_tournament)
        # Option 5: voir données de base
        if choice == "5":
            TournamentView.show_basic_tournament(index_tournament)
            TournamentView.hit_enter("Tapez Entrée pour continuer.")
            TournamentControl.menu_tournament_controller(index_tournament)
        # Option 6: quitter
        if choice == "6":
            exit()

    def save_basic_datas(input_data, index_tournament):
        confirmation = ""
        while confirmation not in ["o", "n"]:
            confirmation = input(
                "Voulez-vous sauvegarder ces changements" +
                f" du Tournoi # {str(index_tournament)} (o/n)?\n>>>")
            if confirmation == "n":
                TournamentControl.main_menu_controller()
            elif confirmation == "o":
                TournamentModel.change_tournament_record(
                    tournament=index_tournament,
                    name_file="tournament_data.json",
                    new_dict=input_data)
                TournamentView.record()
                TournamentControl.main_menu_controller()

    def check_conditions_new_round(index_tournament, current_tournament):
        counter_round = current_tournament.get_matches_lastround()
        if (current_tournament.players in [None, '', [], {}, ()]
                or len(current_tournament.players) == 0 or
                len(current_tournament.players) % 2 != 0):
            TournamentView.display_text(
                "Aucun joueur ne participe ou " +
                "un nombre impair de joueurs \n" +
                "Merci d'ajouter des joueurs.")
            TournamentControl.menu_tournament_controller(index_tournament)
        if (current_tournament.num_round == "" or
                current_tournament.num_round not in ["1", "2", "3", "4"]):
            TournamentView.display_text(
                "Il manque le nombre de match pour ce " +
                "tournoi ou bien trop de matches (>4).")
            TournamentView.display_text(
                "Prière de changer cette données avant de continuer.")
            TournamentControl.menu_tournament_controller(index_tournament)
        if int(current_tournament.num_round) <= counter_round:
            TournamentView.display_text(
                "Tous les matches ont déjà été joués pour ce tournoi.")
            TournamentControl.menu_tournament_controller(index_tournament)
        else:
            return

    def generate_set_players(list_to_check, sets_of_past_matches):
        # Vérifier dans une liste
        # si l'appariement des deux premiers
        # a déjà été joué ou non
        # et combiner avec autre paire
        # si c'est le cas
        # constituer ensuite une liste
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
                    if (pair_t not in sets_of_past_matches and
                            second_item <= len(list_to_check)):
                        generated_list.append(item_1)
                        generated_list.append(item_2)
                        list_to_check.remove(item_1)
                        list_to_check.remove(item_2)
                        break
                    if (pair_t in sets_of_past_matches and
                            second_item == len(list_to_check)):
                        item_1 = list_to_check[0]
                        item_2 = list_to_check[1]
                        generated_list.append(item_1)
                        generated_list.append(item_2)
                        list_to_check.remove(item_1)
                        list_to_check.remove(item_2)
                        break
                    if (pair_t in sets_of_past_matches
                            and second_item < len(list_to_check)):
                        continue
            else:
                generated_list.append(item_1)
                generated_list.append(item_2)
                list_to_check.remove(item_1)
                list_to_check.remove(item_2)
        return (generated_list)

    def play_one_round(current_tournament, turn, save_list):
        already_played = current_tournament.get_matches_alreadyplayed()
        score_players = current_tournament.get_matches_overallscore()
        # cas 1: premier round, liste initiale
        if turn == 0:
            list_players = current_tournament.players
            save_list = []
        # cas 2: deuxième round, liste des meilleurs scores
        if turn == 1:
            list_players = sorted(
                score_players, key=lambda x: score_players[x], reverse=True)
        # cas 3: rounds suivants, faire liste sans doublons
        if turn > 1:
            list_players = TournamentControl.generate_set_players(
                sorted(score_players, key=lambda x: score_players[x],
                       reverse=True), sets_of_past_matches=already_played)

        nbre = int(len(current_tournament.players))
        TournamentView.display_text(f"ROUND # {str(turn)}")
        sub_list = []
        for i in range(0, nbre, 2):
            player1 = list_players[i]
            player2 = list_players[i+1]
            score1, score2 = TournamentView.play_match(
                id_player1=player1, id_player2=player2)
            sub_list.append(([player1, score1], [player2, score2]))
        save_list.append(sub_list)
        return (save_list)

    def input_new_round(index_tournament):
        current_tournament = TournamentModel.load_tournament_from_json(
            index_tournament, "tournament_data.json")
        counter_round = current_tournament.get_matches_lastround()
        TournamentView.display_text(" ♗ MATCHES :")
        TournamentView.display_text(
            TournamentView.matches_already_played(index_tournament))
        TournamentControl.check_conditions_new_round(
            index_tournament, current_tournament)
        TournamentView.display_text("NOUVEAU ROUND :"+str(counter_round))
        current_tournament.matches = TournamentControl.play_one_round(
            current_tournament, turn=counter_round,
            save_list=current_tournament.matches)
        TournamentView.display_text("SAUVEGARDE")
        ask_save = input("Vous voulez sauvegarder ce round (o/n) ?")
        if ask_save == "o":
            TournamentModel.save_match(index_tournament, current_tournament)
            TournamentControl.menu_tournament_controller(index_tournament)
        else:
            TournamentControl.main_menu_controller()
