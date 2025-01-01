import json
import re
from pathlib import Path
from datetime import datetime

class Player:

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
        # Méthode de classe pour extraire tous les prénoms
        return [player.id_number for player in Player.all_players]

    def get_list_player_json(name_file):
        with open(name_file, "r", encoding="utf-8") as file:
            data_player = json.load(file) 
        return (data_player)
    
    def change_specific_data(index,name_file, key_to_change, new_value):
        with open(name_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if index not in data["players"]:
                data["players"][index][key_to_change].append(new_value)
            else:
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

    def change_one_item (choice,current_list):
        choice=int(choice)
        input_data={}
        input_text = ["Identifiant", "Prénom", "Nom",
                      "Date de naissance"]
        categories = ["id_number", "firstname", "surname",
                      "birthdate"]
        existing_data = [current_list[choice].id_number, current_list[choice].firstname, current_list[choice].surname,
                         current_list[choice].birthdate]
        new_id=""
        list_id=Player.get_all_id("")

        while new_id in list_id or Player.check_format_id(new_id)==False:
            new_id=input(f"Identifiant - ({current_list[choice].id_number})")
            if new_id in list_id:
                print("Cet identifiant existe déjà.")
            if Player.check_format_id(new_id)==False:
                print("Mauvais format, il faut respecter : AA000")
        current_list[choice].id_number=new_id

        new_birthdate=""
        while Player.check_format_birthdate(new_birthdate)==False:
            print("Le format doit être JJMMAAAA")
            new_birthdate=input(f"Date de naissance - ({current_list[choice].birthdate})")
        current_list[choice].birthdate=new_birthdate

        new_surname=input(f"Nom - ({current_list[choice].surname})")
        current_list[choice].surname=new_surname

        new_firstname=input(f"Prénom - ({current_list[choice].firstname})")
        current_list[choice].firstname=new_firstname
        
        print(current_list[choice].firstname)
        print(current_list[choice].surname)
        print(current_list[choice].birthdate)
        print(current_list[choice].id_number)

        save_or_not=input("Voulez vous sauvegarder ces données ? (o/n)")
        if save_or_not=="o":
            Player.change_specific_data(choice,"players_database.json", "id_number", new_id)
            Player.change_specific_data(choice,"players_database.json", "firstname", new_firstname)
            Player.change_specific_data(choice,"players_database.json", "surname", new_surname)
            Player.change_specific_data(choice,"players_database.json", "birthdate", new_birthdate)

            #if new_data == "":
             #   input_data[item2] = item3
            #else:
            #    input_data[item2] = new_data
            #Player.change_specific_data(index,"players_database.json", item2, new_data)
        

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

    def add_player(current_list):
        index_new_player=len(current_list)
        print("Vous ajoutez un joueur numéro "+str(index_new_player))
        current_list.append(Player(id_number="",surname="",firstname="",birthdate=""))
        print("la longueur de la liste est désormais" + str(len(current_list)))
        Player.change_one_item (index_new_player,current_list)
        
    def get_list_players():
        raw_data=Player.get_list_player_json("players_database.json")
        list_players=Player.extract_list_players(raw_data)
        return(list_players)
    
    def change_player():
        current_list=Player.get_list_players()
        input_data = {}
        input_text = ["Identifiant", "Prénom", "Nom",
                      "Date de naissance"]
        categories = ["id_number", "firstname", "surname",
                      "birthdate"]
       # existing_data = [current_list.id_number, current_list.firstname, current_list.surname,
       #                  current_list.birthdate]
        print ("Entrez le numéro du joueur pour le changer ou X pour en ajouter.")
        for index, player in enumerate(current_list):
            print(f"[{index}]{player.id_number} - {player.firstname} {player.surname} (né.e le : {player.birthdate})")
        choice=input("Votre choix : ")
        if choice=="X":
            Player.add_player(current_list)
        else:
            print(f"Votre choix c'est {current_list[int(choice)].firstname}")
            Player.change_one_item (choice,current_list)
    
"""
list=Player.get_list_player_json("players_database.json")
list_players=Player.extract_list_players(list)

for index, player in enumerate(list_players):
    print (f"{index} {player.surname}")

list_id=Player.get_all_id("")
print("liste id")
print(list_id)

Player.change_player(current_list=list_players)




        
#Player.change_player(list)
"""