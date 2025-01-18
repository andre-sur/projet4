from datetime import datetime
import re
import json
from Model.PlayerModel import Player


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

    def quantity_tournaments(filename):
        with open(filename, "r", encoding='utf-8') as file:
            all_datas = json.load(file)
        num_tournaments = len(all_datas['tournaments'])
        return num_tournaments

    def load_tournament_from_json(tournament, filename):
        with open(filename, "r", encoding='utf-8') as file:
            all_datas = json.load(file)
            data = all_datas["tournaments"][tournament]
            selected_tournament = TournamentModel(
                name=data.get("name", ""),
                location=data.get("location", ""),
                start=data.get("start", ""),
                end=data.get("end", ""),
                num_round=data.get
                ("num_round", ""),
                description=data.get
                ("description", ""),
                players=data.get
                ("players", "test"),
                matches=data.get("matches", ""))
        return selected_tournament

    def list_of_participants(current_tournament):
        list_participants = ""
        for player in current_tournament.players:
            name_corresponding = Player.find_name_with_code(what_code=player)
            list_participants += f"{name_corresponding}, "
        list_participants = list_participants[:-2]
        return (list_participants)

    def get_ranking(self):
        all_matches = self.matches
        all_data = Player.get_list_player_json("players_database.json")
        all_players = Player.extract_list_players(all_data)
        players_for_id = [zz.surname + " [" + zz.id_number +
                          "]" for zz in all_players if
                          zz.id_number in self.players]
        the_scores = [0]*len(self.players)
        list_ranked_players = "CLASSEMENT :"
        ranked_players = dict(zip(players_for_id, the_scores))
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

    def get_matches_alreadyplayed(self):
        all_matches = self.matches
        already_played = []
        for match in all_matches:
            for player in match:
                already_played.append((player[0][0], player[1][0]))
        return (already_played)

    def get_matches_overallscore(self):
        all_matches = self.matches
        score_players = dict.fromkeys(self.players, 0)
        for match in all_matches:
            for elements in match:
                score_players[elements[0][0]] += elements[0][1]
                score_players[elements[1][0]] += elements[1][1]
        return (score_players)

    def get_matches_lastround(self):
        all_matches = self.matches
        counter_round = len(all_matches)
        return (counter_round)

    def get_matches_display(self):
        all_matches = self.matches
        display_match = ""
        players_match = ""
        score_match = ""
        counter_round = 0
        print("counter")
        print(counter_round)
        for match in all_matches:
            display_match += f"\n   ROUND # {counter_round}\n"
            for elements in match:
                name_player1 = Player.find_name_with_code(elements[0][0])
                name_player2 = Player.find_name_with_code(elements[1][0])
                players_match = f"{name_player1} vs {name_player2}"
                score_match = f"{str(elements[0][1])}-{str(elements[1][1])}\n"
                presentation_space = " "*(30 - len(players_match))+": "
                display_match += players_match+presentation_space+score_match
            counter_round = counter_round + 1
        return (display_match)

    def change_specific_data(tournament, name_file, key_to_change, new_value):
        with open(name_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            data["tournaments"][tournament][key_to_change] = new_value
        with open(name_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def delete_matches(tournament):
        TournamentModel.change_specific_data(
            tournament=tournament,
            name_file="tournament_data.json",
            key_to_change="matches", new_value=[])

    def change_tournament_record(tournament, name_file, new_dict):
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

    def save_match(tournament, current_tournament):
        TournamentModel.change_specific_data(
            tournament, name_file="tournament_data.json",
            key_to_change="matches",
            new_value=current_tournament.matches)

    def list_of_tournament(file_name):
        list_tournament = []
        try:
            with open(file_name, 'r', encoding='utf-8') as fichier_json:
                all_datas = json.load(fichier_json)
        except FileNotFoundError:
            all_datas = '"tournaments": {"1": {}}'
        if not all_datas:
            all_datas = '"tournaments": {"1": {}}'
        for tournament_id, tournament_data in all_datas['tournaments'].items():
            list_tournament.append(
                f"{str(tournament_id)} - {tournament_data['name']}")
        return list_tournament

    def check_format_date(data):
        j = r'^(0[1-9]|[12][0-9]|3[01])'
        m = r'(0[1-9]|1[0-2])'
        a = r'(19[0-9]{2}|20[0-4][0-9]|202[0-4])$'
        pattern = j + '-' + m + '-' + a
        if re.match(pattern, data):
            try:
                jour, mois, annee = map(int, data.split('-'))
                datetime(annee, mois, jour)
                return True
            except ValueError:
                return False
        else:
            return False
