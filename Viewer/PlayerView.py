import json
import re
from pathlib import Path
from datetime import datetime

def print_list_players():
        current_list=Player.get_list_players()
        for index, player in enumerate(current_list):
            print(f"[{index}]{player.id_number} - {player.firstname} {player.surname} (né.e le : {player.birthdate})")

def display_text(text_string):
      print(text_string) 
   
    

