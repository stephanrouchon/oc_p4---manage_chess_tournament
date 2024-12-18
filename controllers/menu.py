import json

from controllers.tournament import MenuTournamentController
from models.player import Player
from models.tournament import Tournament
from views import view

from views.main_menu_view import MainMenuView
from views.menu_tournament_view import MenuTournamentView, TournamentChoiceView, TournamentListView


class MenuController():
    def __init__(self):
        self.view = MainMenuView()

    def main_menu(self):
        while True:
            choice = self.view.display_main_menu()
            if choice == "1":
                tournament = self.create_tournament()
                MenuTournamentController(tournament).tournament_menu()

            elif choice == "2":
                tournament = self.choose_tournament()

            elif choice == "3":
                self.players_list()
                
            elif choice == "4":
                self.tournaments_list()
                
            elif choice == "5":
                self.view.goodbye()
                break
            else:
                self.view.invalid_choice()

    def create_tournament(self):
        tournament = MenuTournamentController().create_tournament()
        return tournament

    def load_tournaments(self):
        with open(".\\data\\tournaments.json", "r", encoding="utf-8") as file:
            tournaments_data = json.load(file)

            return tournaments_data

    def choose_tournament(self):
        tournaments_data = self.load_tournaments()
        choice = MainMenuView.choose_tournament(self, tournaments_data)
        tournament = tournaments_data[int(choice) - 1]
        self.load_tournament(tournament)

    def load_tournament(self, tournament):

        self.tournament = self.load_tournament_info(tournament)
        self.load_tournament_players(tournament)
        self.load_rounds(tournament)
        MenuTournamentController(self.tournament).tournament_menu()

    def load_tournament_info(self, tournament):
        self.tournament = Tournament(tournament["name"],
                                     tournament["location"],
                                     tournament["description"],
                                     tournament["nb_rounds"],
                                     tournament["nb_players"],
                                     tournament["id"]
                                     )
        self.tournament.start_date = tournament["start_date"]
        self.tournament.end_date = tournament["end_date"]
        return self.tournament

    def load_rounds(self, tournament):
        for round in tournament["rounds"]:
            self.tournament.add_round()
            self.tournament.rounds[-1].start_date = round["start_date"]
            self.tournament.rounds[-1].end_date = round["end_date"]

            for match in round["matches"]:

                player1 = match["player1"]
                player2 = match["player2"]

                for player in self.tournament.tournament_players:
                    if player.player.id == match["player1"]:
                        player1 = player
                    if player.player.id == match["player2"]:
                        player2 = player

                self.tournament.rounds[-1].add_match(player1,
                                                     player2,
                                                     match["player1_score"],
                                                     match["player2_score"])

    def load_tournament_players(self, tournament):

        for player in tournament["players"]:
            player_score = player["score"]
            player_opponents = player["opponents"]
            player = Player(player["first_name"],
                            player["last_name"],
                            player["birth_date"],
                            player["id"]
                            )

            tournament_player = self.tournament.add_player_in_tournament(player)
            tournament_player.score = player_score
            tournament_player.opponents = player_opponents

    def search_tournament_by_name(self):
        tournaments = self.load_tournaments()
        choice = TournamentChoiceView.find_by_name(self)
        tournaments_list = [tournament for tournament in tournaments
                            if tournament.name.lower().startswith(choice.lower())]
        return tournaments_list
    
    def players_list(self):
        with open("./data/players.json", "r", encoding="utf-8") as file:
                players_data = json.load(file)

        players_data.sort(key=lambda x: x["last_name"])
        
        self.view.players_list(players_data)

    def tournaments_list(self):
        tournaments = self.load_tournaments()

        tournaments.sort(key=lambda x: x["name"])
        
        self.view.tournaments_list(tournaments)
        