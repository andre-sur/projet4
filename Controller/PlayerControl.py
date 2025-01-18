from Viewer.PlayerView import PlayerView
from Model.PlayerModel import Player


class PlayerControl:

    def change_one_item(index_player, current_list):
        index_player = int(index_player)
        new_id = ""
        list_id = Player.get_all_id("")
        while new_id in list_id or Player.check_format_id(new_id) is False:
            new_id = input(
                f"Identifiant - ({current_list[index_player].id_number})")
            if new_id in list_id:
                PlayerView.display_text("Cet identifiant existe déjà.")
            if Player.check_format_id(new_id) is False:
                PlayerView.display_text(
                    "Respectez ce format : AB1234")
        current_list[index_player].id_number = new_id
        new_birthdate = ""
        while Player.check_format_birthdate(new_birthdate) is False:
            PlayerView.display_text("Le format doit être JJ-MM-AAAA")
            new_birthdate = input(
                f"Date de naissance - ({current_list[index_player]
                                        .birthdate})").strip()
            current_list[index_player].birthdate = new_birthdate
        new_surname = input(f"Nom - ({current_list[index_player].surname})")
        current_list[index_player].surname = new_surname
        new_firstname = input(
            f"Prénom - ({current_list[index_player].firstname})")
        current_list[index_player].firstname = new_firstname
        PlayerView.display_text(current_list[index_player].firstname)
        PlayerView.display_text(current_list[index_player].surname)
        PlayerView.display_text(current_list[index_player].birthdate)
        PlayerView.display_text(current_list[index_player].id_number)
        save_or_not = ""
        while save_or_not not in ["o", "n"]:
            save_or_not = input("Voulez vous sauvegarder ces données ? (o/n)")
            if save_or_not == "o":
                Player.change_specific_data(
                    index_player, "players_database.json",
                    "id_number", new_id)
                Player.change_specific_data(
                    index_player, "players_database.json",
                    "firstname", new_firstname)
                Player.change_specific_data(
                    index_player, "players_database.json",
                    "surname", new_surname)
                Player.change_specific_data(
                    index_player, "players_database.json",
                    "birthdate", new_birthdate)
                return
            else:
                return

    def add_player(current_list):
        index_new_player = len(current_list)
        PlayerView.display_text(
            "Vous ajoutez le joueur numéro " + str(index_new_player))
        current_list.append(
            Player(id_number="", surname="", firstname="", birthdate=""))
        PlayerView.display_text(
            "La longueur de la liste est \
            désormais : " + str(len(current_list)))
        PlayerControl.change_one_item(index_new_player, current_list)

    def check_input_choice_player(max_digit):
        while True:
            # Demander à l'utilisateur de saisir une valeur
            choice = input(
                "Veuillez entrer un chiffre entre 0 " +
                f"et {max_digit - 1} ou 'x' pour ajouter un joueur : ")
            if choice == 'x':
                PlayerView.display_text(
                    "Vous avez choisi d'ajouter un joueur'.")
                return choice
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
        PlayerView.display_text(
            "Entrez le numéro du joueur pour le changer ou X pour en ajouter.")
        choice = PlayerControl.check_input_choice_player(
            max_digit=len(current_list))
        if choice.isdigit():
            PlayerView.display_text(
                f"\nVotre choix c'est {current_list[int(choice)].firstname}")
            PlayerControl.change_one_item(choice, current_list)
        if choice == "x" or choice == "X":
            PlayerControl.add_player(current_list)
        return choice
