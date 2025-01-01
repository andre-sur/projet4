import time
from datetime import datetime
import re
import json
from Player import Player
from pathlib import Path
from TournamentView import TournamentView
from TournamentControl import TournamentControl

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
            list_participants += Player.find_name_with_code(what_code=player)+"\n"
        list_participants = list_participants[:-2]
        return (list_participants)

    def get_ranking(self):
        # Création d'un dictionnaire pour faire classement selon score
        all_matches = self.matches
        the_players = self.players
        all_data = Player.get_list_player_json("players_database.json")
        all_players=Player.extract_list_players(all_data)
        players_for_id = [zz.surname + " ["+ zz.id_number+"]" for zz in all_players if zz.id_number in self.players]
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

    def get_matches(self):
        all_matches = self.matches
        view_matches = ""
        match = []
        score_players=dict.fromkeys(self.players,0)
        already_played=[]
        counter_round = 1
        for match in all_matches:
            view_matches += f"\n   ROUND # {counter_round}\n"
            for m in match:
                score_players[m[0][0]]+=m[0][1]
                score_players[m[1][0]]+=m[1][1]
                already_played.append((m[0][0],m[1][0]))
                view_matches += f"{m[0][0]} vs {m[1][0]}" + " "*(25 - len(
                    f"{m[0][0]} vs {m[1][0]}")) + " : "+f"{str(m[0][1])} - {str(m[1][1])}\n"
            counter_round = counter_round + 1
        return (view_matches,score_players,already_played,counter_round)

    def change_specific_data(tournament, name_file, key_to_change, new_value):
        with open(name_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            data["tournaments"][tournament][key_to_change] = new_value
        with open(name_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def delete_matches(tournament):
        TournamentModel.change_specific_data(
            tournament=tournament, name_file="tournament_data.json", key_to_change="matches", new_value=[])

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

    def save_match(tournament,current_tournament):
        
            TournamentView.record()
            TournamentModel.change_specific_data(
                tournament, name_file="tournament_data.json", key_to_change="matches", new_value=current_tournament.matches)
            TournamentView.main_menu()

    def list_of_tournament(file_name):
        list_tournament = ""
        try:
            with open(file_name, 'r', encoding='utf-8') as fichier_json:
                all_datas = json.load(fichier_json)
        except FileNotFoundError:
            all_datas = '"tournaments": {"1": {}}'
        if not all_datas:
            all_datas = '"tournaments": {"1": {}}'
        for tournament_id, tournament_data in all_datas['tournaments'].items():
            list_tournament += f"{str(tournament_id)} - {tournament_data['name']}\n"
        return list_tournament, tournament_id

    def check_format_date (data):
        pattern = r'^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9]{2}|20[0-4][0-9]|202[0-4])$'
  
        if re.match(pattern, data):
            try:
                jour, mois, annee = map(int, data.split('-'))
                datetime(annee, mois, jour)
                return True
            except ValueError:
                return False
        else:
            return False



