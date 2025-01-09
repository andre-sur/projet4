import json
import re
from pathlib import Path
from datetime import datetime

class Player:

#MODELES
    all_players=[]
    def __init__(self, surname, firstname, birthdate, id_number):
        self.surname = surname
        self.firstname = firstname
        self.birthdate = birthdate
        self.id_number = id_number
        Player.all_players.append(self)
    
    def __str__(self):
        return f"ID Number: {self.id_number}, Surname: {self.surname}, Firstname: {self.firstname}, Birthdate: {self.birthdate}"

    def get_all_id(self):
        return [player.id_number for player in Player.all_players]

    def get_list_player_json(name_file):
        with open(name_file, "r", encoding="utf-8") as file:
            data_player = json.load(file) 
        return (data_player)
    
    def change_specific_data(index,name_file, key_to_change, new_value):
        with open(name_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            #if index not in data["players"]:
               # data["players"][index][key_to_change].append(new_value)
            #else:
            data["players"][index][key_to_change] = new_value
        with open(name_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def find_name_with_code (what_code):
        all_data = Player.get_list_player_json("players_database.json")
        list_players=Player.extract_list_players(all_data)
        for player in list_players:
            if player.id_number == what_code:
                return f"[{player.id_number}] - {player.firstname} {player.surname}"  # Retourne le nom du joueur correspondant
        return "pas trouvé"  

    def check_format_id (data):
        pattern = r'^[A-Za-z]{2}\d{4}$'
        if re.match(pattern, data):
            return True
        else:
            return False

    def check_format_birthdate (data):
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

    def extract_list_players(data):
        players = []
        for player_data in data['players']:
            player = Player(
                id_number=player_data['id_number'],
                surname=player_data['surname'],
                firstname=player_data['firstname'],
                birthdate=player_data['birthdate']
            )
            players.append(player)
        
        return players
    def get_list_players():
        raw_data=Player.get_list_player_json("players_database.json")
        list_players=Player.extract_list_players(raw_data)
        return(list_players)
    