import time
import json
from pathlib import Path


class Player:

    def __init__(self, surname, firstname, birthday):
        self.surname = surname
        self.firstname = firstname
        self.birthday = birthday

    def get_list_player_json(name_file):
        with open(name_file, "r", encoding="utf-8") as file:
            data_1 = json.load(file)

        list = [joueur["surname"] for joueur in data_1["joueurs"]]
        return (list)

class TournamentModel:
    def __init__(self, id="id", name="", location="", start="", end="",
                 num_round="", description="", players=[], matches=[]):
        self.id = id
        self.name = name
        self.location = location
        self.start = start
        self.end = end
        self.num_round = num_round
        self.description = description
        self.matches = matches
        self.players = players

    def load_tournament_from_json(tournament, filename):
        # Ouvre le fichier JSON et charge les données
        with open(filename, "r", encoding='utf-8') as file:
            all_datas = json.load(file)
        data = all_datas["tournaments"][tournament]
        selected_tournament = TournamentModel(name=data.get("name", ""), location=data.get("location", ""),
                                              start=data.get("start", ""), end=data.get("end", ""),
                                              num_round=data.get("num_round", ""), description=data.get("description", ""),
                                              players=data.get("players", "test"), matches=data.get("matches", ""))
        return selected_tournament

    def list_of_participants(self):
        list_participants = ""
        for player in self.players:
            list_participants += f"{player}, "
        list_participants = list_participants[:-2]
        return (list_participants)

    def get_ranking(self):
        # Création d'un input_datannaire pour faire classement selon score
        all_matches = self.matches
        the_players = self.players
        the_scores = [0]*len(self.players)
        list_ranked_players = "CLASSEMENT :"
        ranked_players = dict(zip(the_players, the_scores))

        for match in all_matches:
            for m in match:
                ranked_players[m[0][0]] += m[0][1]
                ranked_players[m[1][0]] += m[1][1]
        sorted_players = {k: v for k, v in sorted(
            ranked_players.items(), key=lambda item: item[1], reverse=True)}

        for key in sorted_players:
            list_ranked_players += f"{key} ({sorted_players[key]}),"
        list_ranked_players = list_ranked_players[:-1]
        list_ranked_players += "\n"
        return (list_ranked_players)

    def show_matches(self):
        all_matches = self.matches
        view_matches = ""
        match = []
        counter_round = 1
        for match in all_matches:
            view_matches += f"\n   ROUND # {str(counter_round)}\n"
            for m in match:
                view_matches += f"{m[0][0]} vs {m[1][0]}" + " "*(25 - len(
                    f"{m[0][0]} vs {m[1][0]}")) + " : "+f"{str(m[0][1])} - {str(m[1][1])}\n"
            counter_round = counter_round + 1
        return (view_matches)

    def change_specific_data(tournament, name_file, key_to_change, new_value):
        with open(name_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            data["tournaments"][tournament][key_to_change] = new_value
        with open(name_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def delete_matches(tournament):
        print("Les matches sont tous effacés.")
        TournamentModel.change_specific_data(
            tournament=tournament, name_file="tournament_data.json", key_to_change="matches", new_value=[])

    def change_data_file(tournament, name_file, new_dict):
        try:
            with open(name_file, 'r', encoding='utf-8') as fichier_json:
                all_datas = json.load(fichier_json)
        except json.JSONDecodeError:
            all_datas = {}
        except FileNotFoundError:
            all_datas = []
        all_datas['tournaments'][tournament] = new_dict
        with open(name_file, 'w', encoding='utf-8') as fichier_json:
            json.dump(all_datas, fichier_json, indent=4)

class TournamentView:
    def upload_file(file_name):
        file_name = input("FICHIER SOURCE (par défaut: tournement_data.json)")
        if file_name == "":
            file_name = "tournament_data.json"
        else:
            if not Path(file_name).exists():
                print("Ce fichier n'existe pas. \nNous utiliserons : ")
                print("Le fichier par défaut: tournament_data.json")
                file_name = "tournament_data.json"
        return (file_name)

    def change_participants(current_tournament, tournament):
        print("Avant de modifier la liste des joueurs, il faut effacer les matches."
              "Effacer les matches (o/n)?")
        decision = input(">>>")
        if decision == "o":
            TournamentModel.delete_matches(tournament)
            TournamentView.choose_participants(current_tournament, tournament)
        else:
            TournamentView.main_menu()

    def choose_which_tournament(last_one, file_name):
        chosen_tournament = ""
        list_options = [str(i) for i in range(0, int(last_one) + 1)]
        while chosen_tournament not in list_options:
            chosen_tournament = input(
                "Quel tournoi ? (0 pour en créer un) >>>")
        if chosen_tournament == "0":
            current_tournament = TournamentModel()
            TournamentView.input_data_tournament(
                (str(int(last_one)+1)), tournament=chosen_tournament)
        else:
            current_tournament = TournamentModel.load_tournament_from_json(
                chosen_tournament, file_name)
            TournamentView.show_basic_tournament(current_tournament)
        return (chosen_tournament, current_tournament)

    def menu_tournament(current_tournament, tournament):
        choice = ""
        while choice not in ["1", "2", "3", "4"]:
            choice = input("  (1) Modifier ce tournoi (données de base) "
                           "\n  (2) Ajouter/Modifier la liste des participants"
                           f"\n  (3) Jouer un round de {str(current_tournament.num_round)} matches"
                           "\n  (4) Sélectionner un autre tournoi."
                           "\n  (5) Quitter l'application."
                           "\n   >>>")
            if choice == "1":
                TournamentView.input_data_tournament(
                    current_tournament, tournament)
            if choice == "2":
                TournamentView.change_participants(
                    current_tournament, tournament=tournament)
            if choice == "3":
                if current_tournament.players in [None, '', [], {}, ()] or len(current_tournament.players) == 0 or len(current_tournament.players) % 2 != 0:
                    print(
                        "Aucun joueur ne participe ou un nombre impair de joueurs \nMerci d'ajouter des joueurs.")
                    TournamentView.main_menu()
                if current_tournament.num_round == "" or current_tournament.num_round not in ["1", "2", "3", "4"]:
                        print(
                            "Il manque le nombre de match pour ce tournoi ou bien trop de matches (>4).")
                        print("Prière de changer cette données avant de continuer.")
                        print("Retour au Menu Principal...")
                        TournamentView.main_menu()
                if current_tournament.matches :
                        print ("Les matches ont déjà été joués pour ce tournoi.")
                        TournamentView.main_menu()
                else:
                        TournamentView.choose_howto_play(
                            tournament, current_tournament)
            if choice == "4":
                TournamentView.main_menu()
        return ()

    def choose_howto_play(tournament, current_tournament):
        print("Saisie des scores...")
        list_players, save_list = TournamentView.play_round(current_tournament)
        current_tournament.matches = save_list
        print(" ♗ MATCHES :")
        print(current_tournament.show_matches())
        ask_save = input(
            f"Vous voulez sauvegarder ces {current_tournament.num_round} rounds (o/n) ?")
        if ask_save == "o":
            TournamentView.record()
            TournamentModel.change_specific_data(
                tournament, name_file="tournament_data.json", key_to_change="matches", new_value=current_tournament.matches)
            TournamentView.main_menu()
        else:
            TournamentView.main_menu()

    def main_menu():
        print("")
        print("♔  CHESS TOURNAMENT MANAGER ♔ \n♖  MENU PRINCIPAL ♖")
        print("")
        file_name = TournamentView.upload_file("tournament_data.json")
        # Appel à fonction pour récupérer la liste des tournois et le numéro du dernier enregistré
        # (donc quantité total de tournois)
        all_tournaments, last_one = TournamentView.list_of_tournament(
            file_name)
        print("\n♙LISTE DES TOURNOIS")
        print(all_tournaments)
        # Une liste des numéros pour vérifier que l'input est l'un d'eux
        chosen_tournament, current_tournament = TournamentView.choose_which_tournament(
            last_one, file_name)
        TournamentView.menu_tournament(
            current_tournament, tournament=chosen_tournament)

    def list_of_tournament(file_name):
        list_tournament = ""
        try:
            with open(file_name, 'r', encoding='utf-8') as fichier_json:
                all_datas = json.load(fichier_json)
        except FileNotFoundError:
            # Si le fichier n'existe pas, initialise une liste vide
            all_datas = '"tournaments": {"1": {}}'
        # Parcourir les tournois
        if not all_datas:
            all_datas = '"tournaments": {"1": {}}'
        for tournament_id, tournament_data in all_datas['tournaments'].items():
            list_tournament += f"{str(tournament_id)} - {tournament_data['name']}\n"
        # Afficher la liste des identifiants et des noms de tournois
        return list_tournament, tournament_id

    def choose_participants(current_tournament, tournament):
        chosen_list = []
        current_players = ", ".join(current_tournament.players)
        print("Voici la liste des joueurs actuellement enregistrés :"
              f"\n{current_players}"
              "\nTapez Entrée si vous excluez le joueur"
              "\nTapez x ou X si vous incluez le joueur.")
        all_players = Player.get_list_player_json("players_database.json")
        for player in all_players:
            decision = input(player+" "*(20-len(player))+"  : ")
            if decision == "x" or decision == "X":
                chosen_list.append(player)
        text_chosenlist = ", ".join(chosen_list)
        if len(chosen_list) < 2 or len(chosen_list) % 2 != 0:
            print("Liste trop courte (<2) ou nombre de participants impair."
                  "\nMerci de recommencer.\n_____________________")
            TournamentView.choose_participants(tournament)
        print(f"Voici la liste des joueurs demandée : {text_chosenlist}")
        print("(1) Confirmer et sauvegarder"
              "\n(2) Annuler et retour au Menu")
        decision = ""
        while decision not in ["1", "2"]:
            decision = input("Votre décision >>> ")
            if decision == "1":
                # Modification spécifique de la liste des joueurs pour le tournoi en cours
                TournamentModel.change_specific_data(
                    tournament=tournament, name_file="tournament_data.json", key_to_change="players", new_value=chosen_list)
                TournamentView.record()
                print("Merci. La nouvelle liste de participant(e)s est enregistrée.")
                print("")
                TournamentView.main_menu()
            if decision == "2":
                TournamentView.main_menu()

    def show_basic_tournament(self):
        # Afficher les données de base d'un tournoi
        categories = ["Nom", "Lieu", "Date de début",
                      "Date de fin", "Nombre de rounds", "Description"]
        datas = [self.name, self.location, self.start,
                 self.end, self.num_round, self.description]
        for item1, item2 in zip(categories, datas):
            if len(item1) < 20:
                item1 = item1+" "*(20-len(item1))
            print(f"{item1} : {item2}")
        print(
            f"Participants au tournoi ({self.name}) : {self.list_of_participants()}")
        print(f"MATCHES ({str(self.num_round)} rounds) :")
        print(self.show_matches())
        print(self.get_ranking())

    def input_data_tournament(current_tournament, tournament):
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
              f"\n TOURNOI #{str(tournament)}")
        for item1, item2, item3 in zip(input_text, categories, existing_data):
            data_update = f"{item1} - ({str(item3)})"
            if len(data_update) < 30:
                data_update = data_update + " " * (30-len(data_update)) + ":"
            new_data = input(data_update)
            if new_data == "":
                input_data[item2] = item3
            else:
                input_data[item2] = new_data
        confirmation = ""
        while confirmation not in ["o", "n"]:
            confirmation = input(
                f"Voulez-vous sauvegarder ces changements du Tournoi # {str(tournament)} (o/n)?\n>>>")
            if confirmation == "n":
                TournamentView.main_menu()
            elif confirmation == "o":
                TournamentModel.change_data_file(
                    tournament=tournament, name_file="tournament_data.json", new_dict=input_data)
                TournamentView.record()
                TournamentView.main_menu()
        return input_data

    def record():
        print("Enregistrement en cours...")
        time.sleep(1)
        print("Sauvegarde dans un fichier Json...")
        time.sleep(2)
        print("Enregistrement confirmé.")

    def play_round(current_tournament):
        save_list = []
        sub_list = []
        past_matches = []
        score1 = 0
        score2 = 0
        list_players = current_tournament.players
        score = [0]*len(current_tournament.players)
        all_past = []
        storage_score = dict(zip(current_tournament.players, score))
        nbre = int(len(current_tournament.players))
        tours = int(current_tournament.num_round)
        for turn in range(0, tours):
            print(f"ROUND # {str(turn+1)}")
            sub_list = []
            for i in range(0, nbre-1, 2):
                player1 = list_players[i]
                player2 = list_players[i+1]
                score1, score2 = TournamentControl.play_match(
                    player1=player1, player2=player2)
                sub_list.append(([player1, score1], [player2, score2]))
            # On ajoute à la liste des paires déjà jouées la paire actuelle
            # (pour comparaison ultérieure)
                past_matches.append({player1, player2})
                storage_score[player1] += score1
                storage_score[player2] += score2
            # La liste pour prochain round se compose des meilleurs joueurs (ordre décroissant)
            new_list = sorted(
                storage_score, key=lambda k: storage_score[k], reverse=True)

            save_list.append(sub_list)
            # faire une exception pour le premier tour
            # pour lequel on ne compare pas avec les matches précédents
            if turn == 0:
                list_players = new_list
            if turn > 0:
                # On appelle la fonction qui vérifie si déjà jouée et crée nouvelle paire si oui
                # Elle renvoie une liste avec des paires non déjà jouées
                list_players = TournamentControl.generate_set_players(
                    new_list, past_matches)
        all_past.append(past_matches)
        current_tournament.matches = save_list
        return (list_players, save_list)

class TournamentControl:

    def generate_set_players(input_list, past_matches):
        # Cette fonction vérifie si paire déjà jouée
        # et si oui, cherche la suivante jusqu'à en trouver une non dejà jouée
        output_list = []
        list_tocheck = input_list.copy()
        a = 0
        b = 1
        item_1 = list_tocheck[a]
        item_2 = list_tocheck[b]
        pair = {item_1, item_2}
        while len(list_tocheck) > 0:
            item_1 = list_tocheck[0]
            item_2 = list_tocheck[1]
            pair = {item_1, item_2}
            if pair in past_matches:
                for second_item in range(2, len(list_tocheck)):
                    item_1 = list_tocheck[0]
                    item_2 = list_tocheck[second_item]
                    pair_t = {item_1, item_2}
                    if pair_t not in past_matches and second_item <= len(list_tocheck):
                        output_list.append(item_1)
                        output_list.append(item_2)
                        list_tocheck.remove(item_1)
                        list_tocheck.remove(item_2)
                        break
                    if pair_t in past_matches and second_item == len(list_tocheck):
                        item_1 = list_tocheck[0]
                        item_2 = list_tocheck[1]
                        output_list.append(item_1)
                        output_list.append(item_2)
                        list_tocheck.remove(item_1)
                        list_tocheck.remove(item_2)
                        break
                    if pair_t in past_matches and second_item < len(list_tocheck):
                        continue
            else:
                output_list.append(item_1)
                output_list.append(item_2)
                list_tocheck.remove(item_1)
                list_tocheck.remove(item_2)
        return (output_list)

    def play_match(player1, player2):
        choice = f"1. {player1} 2.{player2} 0. Match nul. >>>"
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

TournamentView.main_menu()
