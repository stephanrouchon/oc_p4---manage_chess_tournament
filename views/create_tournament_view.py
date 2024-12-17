class CreateTournamentView:
    def get_name(self):
        return input("Enter the name of the tournament: ")

    def get_location(self):
        return input("Enter the location of the tournament: ")

    def get_description(self):
        return input("Enter the description of the tournament: ")

    def get_rounds_nb(self):
        if input("Do you want to set the number of rounds (default 4) ? (y/n) ") == "y":
            return int(input("Enter the number of rounds: "))
        return 4

    def get_nb_players(self):

        if input("Do you want to set the number of players (default 8) ? (y/n) ") == "y":
            choice = input("Enter the number of players: ")

        else:
            choice = "8"

        while not choice.isdigit() or (choice.isdigit() and int(choice) % 2 != 0):
            print("Please enter an even number of players")
            choice = input("Enter the number of players: ")
        choice = int(choice)
        return choice

    def check_nb_players(self, choice):
        if not choice.isdigit or (choice.isdigit and int(choice) % 2 != 0):
            print("Please enter an even number of players")
            return False

    def display_tournament(self, tournament):
        print(f"\nTournament created: {tournament.name}")
        print(f"Location: {tournament.location}")
        print(f"Date: {tournament.start_date}")
        print(f"Description: {tournament.description}")
        print(f"Number of rounds: {tournament.nb_rounds}")


class AddTournamentPlayersView:
    def display_players(self, players):
        print("\n===== PLAYERS LIST =====")
        for player in players:
            print(f"{player.id}. {player.first_name} {player.last_name}")
        return input("Enter the number of the player to add in the tournament: ")
