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
        print("3. View Reports")
        print("4. Quit software")

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
