
from Viewer.PlayerView import PlayerView
from Model.PlayerModel import Player


class PlayerControl:

    def change_one_item(choice, current_list):
        choice = int(choice)

        new_id = ""
        list_id = Player.get_all_id("")

        while new_id in list_id or Player.check_format_id(new_id) is False:
            new_id = input(f"Identifiant - ({current_list[choice].id_number})")
            if new_id in list_id:
                PlayerView.display_text("Cet identifiant existe déjà.")
            if Player.check_format_id(new_id) is False:
                PlayerView.display_text(
                    "Mauvais format, il faut  ce format : AB1234")
        current_list[choice].id_number = new_id

        new_birthdate = ""
        while Player.check_format_birthdate(new_birthdate) is False:
            PlayerView.display_text("Le format doit être JJ-MM-AAAA")
            new_birthdate = input(
                f"Date de naissance - ({current_list[choice].birthdate})")
        current_list[choice].birthdate = new_birthdate

        new_surname = input(f"Nom - ({current_list[choice].surname})")
        current_list[choice].surname = new_surname

        new_firstname = input(f"Prénom - ({current_list[choice].firstname})")
        current_list[choice].firstname = new_firstname

        PlayerView.display_text(current_list[choice].firstname)
        PlayerView.display_text(current_list[choice].surname)
        PlayerView.display_text(current_list[choice].birthdate)
        PlayerView.display_text(current_list[choice].id_number)

        save_or_not = ""
        while save_or_not not in ["o", "n"]:
            save_or_not = input("Voulez vous sauvegarder ces données ? (o/n)")
            if save_or_not == "o":
                Player.change_specific_data(
                    choice, "players_database.json", "id_number", new_id)
                Player.change_specific_data(
                    choice, "players_database.json",
                    "firstname", new_firstname)
                Player.change_specific_data(
                    choice, "players_database.json", "surname", new_surname)
                Player.change_specific_data(
                    choice, "players_database.json",
                    "birthdate", new_birthdate)
                return
            else:
                return
            # if new_data == "":
            #   input_data[item2] = item3
            # else:
            #    input_data[item2] = new_data
            # Player.change_specific_data(index,
            # "players_database.json", item2, new_data)

    def add_player(current_list):
        index_new_player = len(current_list)
        PlayerView.display_text(
            "Vous ajoutez un joueur numéro " + str(index_new_player))
        current_list.append(
            Player(id_number="", surname="", firstname="", birthdate=""))
        PlayerView.display_text(
            "la longueur de la liste est désormais" + str(len(current_list)))
        PlayerControl.change_one_item(index_new_player, current_list)

    def check_input_choice_player(max_digit):

        while True:
            # Demander à l'utilisateur de saisir une valeur
            choice = input(
                "Veuillez entrer un chiffre entre 0 " +
                f"et {max_digit - 1} ou 'x' pour quitter : ")

        # Vérifier si l'entrée est 'x'
            if choice == 'x':
                PlayerView.display_text(
                    "Vous avez choisi d'ajouter un joueur'.")
                return choice

        # Vérifier si l'entrée est un chiffre entre 1 et 10
            if choice.isdigit():
                nombre = int(choice)
                if 0 <= nombre <= max_digit:
                    return str(nombre)
                else:
                    PlayerView.display_text(
                        "Erreur : Le chiffre doit être entre 0 " +
                        f"et {max_digit - 1}.")
            else:
                PlayerView.display_text("Erreur : Veuillez entrer un"
                                        + f"chiffre entre 0 et {max_digit - 1}"
                                        + "ou x pour ajouter un joueur.")

    def change_player():
        current_list = Player.get_list_players()
        PlayerView.print_list_players()
        # existing_data = [current_list.id_number,
        # current_list.firstname, current_list.surname,
        #                  current_list.birthdate]
        PlayerView.display_text(
            "Entrez le numéro du joueur pour le changer ou X pour en ajouter.")
        choice = PlayerControl.check_input_choice_player(
            max_digit=len(current_list))
        if choice.isdigit():
            PlayerView.display_text(
                f"\nVotre choix c'est {current_list[int(choice)].firstname}")
            PlayerControl.change_one_item(choice, current_list)
        if choice == "x":
            Player.add_player

        return choice


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
