import json

from views.menu_tournament_view import MenuTournamentView, \
    TournamentChoiceView, TournamentListView
from models.tournament import Tournament
from models.player import Player
from views.view import display_error
from views.add_player_view import AddPlayerView, CreatePlayerView, PlayerChoiceView
from views import create_tournament_view, view
from models.round import Round

PLAYERS_FILE = "./data/players.json"
TOURNAMENTS_FILE = "./data/tournaments.json"


class MenuTournamentController:
    def __init__(self, tournament=None):
        self.view = MenuTournamentView()
        self.tournament = tournament

    def tournament_menu(self):
        self.view = MenuTournamentView()
        while True:
            choice = self.view.display_tournament_menu(self.tournament)
            if choice == "1":
                self.start_or_resume_tournament()
            elif choice == "2":
                self.show_players()
            elif choice == "3":
                MenuTournamentView.show_ranking(self, self.tournament.tournament_players)
            elif choice == "4":
                self.show_matches()
            elif choice == "5":
                return
            else:
                view.display_error("Invalid choice")

    def create_tournament(self):
        self.view = create_tournament_view.CreateTournamentView()
        name = self.view.get_name()
        location = self.view.get_location()
        rounds_nb = self.view.get_rounds_nb()
        description = self.view.get_description()
        nb_players = self.view.get_nb_players()
        self.tournament = Tournament(name, location, description, rounds_nb, nb_players=nb_players)
        self.save_tournament_to_json(self.tournament)
        self.view.display_tournament(self.tournament)
        return self.tournament

    def load_players(self):
        data = self.load_from_json(PLAYERS_FILE)

        players = [Player(player["first_name"], player["last_name"], player["birthdate"], player["id"])
                   for player in data]
        return players

    def add_player(self, player):

        players_data = self.load_players()
        for p in players_data:
            if p.id == player.id:
                if self.check_player(player) is True:
                    AddPlayerView.player_already_added(self)
                    self.display_players()
                    return
                self.tournament.add_player_in_tournament(player)
                nb_players = str(self.players_number())
                AddPlayerView.add_player(self, player.name, nb_players)
                self.update_tournament()

    def check_player(self, player_to_check):
        for player in self.tournament.tournament_players:
            if player.player.id == player_to_check.id:
                return True

    def order_tournament_players_by_score(self, players):
        players.sort(key=lambda x: x.score, reverse=True)
        return players

    def order_tournament_players_by_name(self, players):
        players.sort(key=lambda x: x.player.last_name)
        return players

    def players_number(self):
        return len(self.tournament.tournament_players)

    def show_players(self):
        self.order_tournament_players_by_name(self.tournament.tournament_players)
        MenuTournamentView.show_tournament_players(self, self.tournament.tournament_players)

    def start_tournament(self):
        while self.players_number() < self.tournament.nb_players:
            self.display_players()
        MenuTournamentView.all_players_added(self)

        self.start_round()

    def start_or_resume_tournament(self):
        if self.tournament.end_date is not None:
            self.view.tournament_end()

        if self.tournament.rounds == []:
            self.start_tournament()
        else:
            self.resume_tournament()

    def start_round(self):
        if len(self.tournament.rounds) >= self.tournament.nb_rounds:
            MenuTournamentView.all_rounds_played(self)
            self.end_tournament()
            self.view.tournament_end()
            self.update_tournament()

        else:
            self.tournament.add_round()
            self.tournament.toss()
            self.update_tournament()
            self.set_match_result()

    def check_matches(self):
        check_matches = []
        for match in self.tournament.rounds[-1].matches:
            if match[0][1] is None or match[1][1] is None:
                check_matches.append(True)

            else:
                check_matches.append(False)

        return True if True in check_matches else False

    def set_match_result(self):
        self.show_round_matches()
        choice = MenuTournamentView.set_rounds_results(self)
        self.set_rounds_results(choice)

    def set_rounds_results(self, match):

        if match == "B" or match == "b":
            return False

        elif match.isdigit() and int(match) <= len(self.tournament.rounds[-1].matches):
            match = int(match)
            player1 = self.tournament.rounds[-1].matches[match-1][0][0].player.name
            player2 = self.tournament.rounds[-1].matches[match-1][1][0].player.name

            result = MenuTournamentView.set_match_result(self, player1, player2)
            self.tournament.set_result(match, int(result))
            self.update_tournament()

            if self.check_matches() is True:
                self.set_match_result()
            else:
                self.tournament.rounds[-1].end_round()
                self.order_tournament_players_by_score(self.tournament.tournament_players)
                MenuTournamentView.show_ranking(self, self.tournament.tournament_players)
                if len(self.tournament.rounds) == self.tournament.nb_rounds:
                    self.show_round_matches()
                    self.end_tournament()
                    self.update_tournament()
                    return
                else:
                    self.start_round()
                    self.show_round_matches()
                    self.update_tournament()
                    self.set_match_result()
        else:
            self.view.invalid_choice()
            self.set_rounds_results()

    def resume_tournament(self):
        if self.tournament.end_date is not None:
            self.view.tournament_end()
            MenuTournamentView.show_ranking(self, self.tournament.tournament_players)
            return
        else:
            self.set_match_result()

    def show_matches(self):

        MenuTournamentView.show_rounds(self, self.tournament)

    def show_round_matches(self):
        i = 1
        matches_to_display = []
        for match in self.tournament.rounds[-1].matches:

            if match [0][1] is None:
                match = (f"{i} - {match[0][0].player.name} vs\
                         {match[1][0].player.name}: in progress")
                matches_to_display.append(match)

            else:
                match = (f"{i} - {match[0][0].player.name} vs\
                         {match[1][0].player.name} : {match[0][1]} - {match[1][1]}")
                matches_to_display.append(match)
            i += 1
        MenuTournamentView.view_rounds_matches(self, matches_to_display, self.tournament.rounds[-1].name)

    def end_tournament(self):
        self.tournament.end_tournament()
        self.view.tournament_end()

    def search_player_by_name(self):
        players = self.load_players()
        choice = PlayerChoiceView.find_by_name(self)
        players_list = [player for player in players if player.first_name.lower(
        ).startswith(choice.lower())]
        return players_list

    def display_players(self):
        players_list = self.search_player_by_name()
        if players_list == []:
            self.view.no_player()
            choice = AddPlayerView.create_or_search(self)
            if choice == "c" or choice == "C":
                self.create_player()
            if choice == "s" or choice == "S":
                self.display_players()

            return

        MenuTournamentView.show_players(self, players_list)

        self.add_player_to_tournament(players_list)

    def add_player_to_tournament(self, players_list):

        choice = PlayerChoiceView.choose_player(self)
        if choice == "C" or choice == "c":
            self.create_player()
        elif choice.isdigit() and int(choice)-1 <= len(players_list):
            choice = int(choice) - 1
            player = players_list[choice]
            self.add_player(player)
        elif choice.isdigit() and int(choice)-1 > len(players_list):
            MenuTournamentView.invalid_choice
            self.display_players()
        else:
            MenuTournamentView.invalid_choice
            self.display_players()

    def create_player(self):
        first_name = CreatePlayerView().get_first_name()
        last_name = CreatePlayerView().get_last_name()
        birthday = CreatePlayerView().get_birth_date()
        id = CreatePlayerView().get_id()
        new_player = Player(first_name, last_name, birthday, id)
        self.save_player(new_player)
        self.tournament.add_player_in_tournament(new_player)
        AddPlayerView.player_created(self, new_player.name)

    def save_player(self, new_player):
        try:
            with open("./data/players.json", "r", encoding="utf-8") as file:
                players_data = json.load(file)
        except FileNotFoundError:
            players_data = []
        players_data.append(new_player.__to_dict__())
        self.save_players(players_data, PLAYERS_FILE)

    def append_before_save(self, objet, file):
        try:
            with open(file, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        data.append(objet.__to_dict__())
        self.save_players(data)

    def load_from_json(self, path):
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    def save_to_json(self, data, path):
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def save_players(self, players, PLAYERS_FILE):
        self.save_to_json(players, PLAYERS_FILE)

    def save_tournament_to_json(self, tournament):
        try:
            tournaments_data = self.load_from_json(TOURNAMENTS_FILE)
        except FileNotFoundError:
            tournaments_data = []

        tournaments_data.append(tournament.__to_dict__())

        self.save_to_json(tournaments_data, TOURNAMENTS_FILE)

    def save_tournaments(self, tournaments):
        self.save_to_json(tournaments, TOURNAMENTS_FILE)

    def update_tournament(self):
        self.delete_tournament()
        self.save_tournament_to_json(self.tournament)

    def delete_tournament(self):
        data = self.load_from_json(TOURNAMENTS_FILE)
        data = [tournament for tournament in data if tournament["id"] != str(self.tournament.id)]
        self.save_to_json(data, TOURNAMENTS_FILE)

    def load_tournaments(self):

        tournaments_data = self.load_from_json(TOURNAMENTS_FILE)

        tournaments = [Tournament(tournament_data["name"],
                                  tournament_data["location"],
                                  tournament_data["description"],
                                  tournament_data["rounds_nb"],
                                  tournament_data["start_date"],
                                  tournament_data["end_date"],
                                  tournament_data["id"],
                                  tournament_data["nb_players"])
                       for tournament_data in tournaments_data]

        return tournaments

    def search_tournament_by_name(self):
        tournaments = self.load_tournaments()
        choice = TournamentChoiceView.find_by_name(self)
        tournaments_list = [tournament for tournament in tournaments
                            if tournament.name.lower().startswith(choice.lower())]
        return tournaments_list

    def show_tournaments(self):
        tournaments_list = self.search_tournament_by_name()
        if tournaments_list == []:
            choice = TournamentListView.not_found(self)

            if choice == "c" or choice == "C":
                self.tournament.create_tournament()
                MenuTournamentController(self.tournament).tournament_menu()
            if choice == "s" or choice == "S":
                self.display_tournaments()
            else:
                display_error("Invalid choice")
            return
        else:
            MenuTournamentView.display_tournament_menu(self, tournaments_list)

        self.load_tournament(tournaments_list)

    def load_tournament(self, tournament):

        tournaments_data = self.load_tournaments()

        for tournament_data in tournaments_data:
            if tournament_data["id"] == tournament.id:
                self.tournament = Tournament(tournament_data["name"],
                                             tournament_data["location"],
                                             tournament_data["description"],
                                             tournament_data["rounds_nb"],
                                             tournament_data["start_date"],
                                             tournament_data["end_date"],
                                             tournament_data["id"],
                                             tournament_data["nb_players"])

                for player_data in tournament_data["players"]:
                    player = self.select_player(player_data)
                    self.tournament.add_player_in_tournament(
                        player, player_data["score"], player_data["opponents"])

                for round_data in tournament_data["rounds"]:
                    self.tournament.round = Round(
                        round_data["round_number"], round_data["started_at"], round_data["ended_at"])
                    for match_data in round_data["matches"]:
                        player1 = self.select_player(match_data["player1"])
                        player2 = self.select_player(match_data["player2"])
                        player1_score = self.select_player(
                            match_data["player1_score"])
                        player2_score = self.select_player(
                            match_data["player2_score"])
                        round.add_match(player1, player2,
                                        player1_score, player2_score)

                return self.tournament

        def __str__(self):
            return f"{self.name} {self.location} {self.start_date}"
