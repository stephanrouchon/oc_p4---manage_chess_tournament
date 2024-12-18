from tabulate import tabulate


class MainMenuView:
    def display_main_menu(self, active_tournament=None):
        if active_tournament is None:
            print("no active tournament")
        else:
            print(active_tournament)

        print("\n===== MAIN MENU =====")
        print("1. Create a tournament")
        print("2. Select a tournament")
        print("3. Players list in database")
        print("4. Tournaments list in database")
        print("5. Quit software")

        choice = input("Enter your choice: ")
        while choice not in ["1", "2", "3", "4", "5"]:
            print("This choice is not valid")
            choice = input("Enter your choice: ")
        return choice

    def choose_tournament(self, tournaments):
        print("\n===== TOURNAMENTS LIST =====")

        headers = ["n°", "Name", "Location", "Start Date", "End Date"]
        tournaments = [(i+1, tournament["name"],
                        tournament["location"],
                        tournament["start_date"],
                        tournament["end_date"])
                       for i, tournament in enumerate(tournaments)]

        print(tabulate(tournaments, headers=headers, tablefmt="grid"))

        return input("Choose a tournament: ")

    def tournaments_list(self, tournaments):
        print("\n===== TOURNAMENTS LIST =====")

        headers = ["n°", "Name", "Location", "Start Date", "End Date"]
        tournaments = [(i+1, tournament["name"],
                        tournament["location"],
                        tournament["start_date"],
                        tournament["end_date"])
                       for i, tournament in enumerate(tournaments)]

        print(tabulate(tournaments, headers=headers, tablefmt="grid"))

    def players_list(self, players):
        print("\n===== PLAYERS LIST =====")

        headers = ["Last_Name", "First Name", "Birthdate", "id"]
        players = [(i+1, player["last_name"],
                    player["first_name"],
                    player["birthdate"],
                    player["id"])
                   for i, player in enumerate(players)]
        print(tabulate(players, headers=headers, tablefmt="grid"))

    def goodbye(self):
        print("Goodbye!")
        return
    
    def invalid_choice(self):
        print("This choice is not valid")