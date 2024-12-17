class MenuTournamentView:
    def display_tournament_menu(self, tournament_name):
        print(f"\n===== TOURNAMENT MENU =====\nTournament: {tournament_name}")
        print("1. Start or resume tournament")
        print("2. Show tournament players")
        print("3. Show tournament ranking")
        print("4. Show tournament rounds")
        print("5. Back to main menu")

        choice = input("Enter your choice: ")
        while choice not in ["1", "2", "3", "4","5"]:
            print("This choice is not valid")
            choice = input("Enter your choice: ")
        return choice

    def how_many_players(self):

        message = "How many players do you want to add ? "
        choice = input(message)

        while not choice.isdigit:
            print("This choice is not valid")
            choice = input(message)

        while int(choice) % 2 == 0:
            print("The number of players must be even")
            choice = input(message)

        return choice

    def all_players_added(self):
        print("All players have been added")
        print("the first round can start")

    def set_rounds_results(self):

        message = "Enter the number to set the result or B to go back: "

        choice = input(message)
        while choice not in ["1", "2", "3", "4", "B"]:
            print("This choice is not valid")
            choice = input(message)
        return choice

    def set_match_result(self, player1, player2):

        message = f"Enter the result of the match (1: {player1} win, 2: {player2} win, 3: draw): "
        result = input(message)
        while result not in ["1", "2", "3"]:
            print("This choice is not valid")
            result = input(message)

        return result

    def view_rounds_matches(self, matches, round_name):

        print(f"\n===== {round_name.upper()} MATCHES =====")
        for match in matches:
            print(match)

    def all_rounds_played(self):
        print("All rounds have been played")

    def tournament_end(self):
        print("The tournament is over")

    def show_players(self, players):
        print("\n===== PLAYERS LIST =====")
        i = 1
        for player in players:
            print(f"{i} - {player.name}")
            i += 1
        print("\n")

    def show_rounds(self, tournament):

        for round in tournament.rounds:
            print(f"\n===== {round} =====")
            for match in round.matches:
                if match[0][1] == None:
                    print(f"{match[0][0].player.name} vs {match[1][0].player.name} : en cours")
                          
                else: print(f"{match[0][0].player.name} vs {match[1][0].player.name} {match[0][1]} - {match[1][1]} ")           

    def show_tournament_players(self, players):
        print("\n===== PLAYERS LIST =====")
        i = 1
        for player in players:
            print(f"{i} - {player.player.name}")
            i += 1
        print("\n")

    def show_round(self, round):
        print(f"\n===== {round} =====")

    def show_matches(self, matches):
        print("\n===== MATCHES =====")
        for match in matches:
            print(match)

    def show_tournaments(self, tournaments):
        print("\n===== TOURNAMENTS =====")
        i = 1
        for tournament in tournaments:
            print(f"{i} - {tournament.name} {tournament.location} {tournament.start_date}")

    def no_player(self):
        print("No player found")

    def show_ranking(self, players):
        print("\n===== RANKING =====")
        i = 1
        for player in players:
            print(f"{i} - {player.player.name} : {player.score} points")
            i += 1

    def invalid_choice(self):
        print("This choice is not valid")


class MenuTournamentReportsView:
    def display_tournament_reports_menu(self):
        print("\n===== REPORTS MENU =====")
        print("1. Players list")
        print("2. Tournaments Results")
        print("3. Back to previous menu")
        return input("Enter your choice: ")


class TournamentListView:
    def display_tournaments(self, tournament):
        print(tournament)

    def not_found(self):
        print("Tournament not found")
        choice = input(
            "Do you want to create a new tournament or search an existing one ? (c/s) ")
        while choice not in ["c", "s"]:
            print("This choice is not valid")
            choice = input(
                "Do you want to create a new tournament or search an existing one ? (c/s) ")
        return choice

class TournamentChoiceView:
    def find_by_name(self):
        return input("Enter the name of the tournament to find: ")
