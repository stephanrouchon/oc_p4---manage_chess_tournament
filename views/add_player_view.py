class CreatePlayerView:
    def get_first_name(self):
        return input("Enter the first name of the player: ")

    def get_last_name(self):
        return input("Enter the last name of the player: ")

    def get_birth_date(self):
        return input("Enter the birth date of the player (dd/mm/yyyy): ")

    def get_id(self):
        return input("Enter the ID of the player: ")


class PlayerChoiceView:
    def find_by_name(self):
        return input("Enter the name of the player to find: ")

    def choose_player(self):
        message = "Which player do you want to add ? (give the number)"
        choice = input(message)

        return choice


class AddPlayerView:
    def player_already_added(self):
        print("This player is already added to the tournament")

    def create_or_search(self):
        message = "Do you want to create a new player or search an existing one ? (c/s) "
        choice = input(message)
        while choice not in ["c", "s"]:
            print("This choice is not valid")
            choice = input(message)
        return choice

    def choose_player_or_create_one(self):
        choice = input("give number or C to create a new player ?")
        return choice

    def add_player(self, player_name, players_nb):
        print(f"{player_name} added to the tournament")
        print(f"{players_nb} players in the tournament")

    def player_created(self, player_name):
        print(f"{player_name} created and added to the tournament")
