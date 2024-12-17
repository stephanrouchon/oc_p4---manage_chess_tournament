from views import create_tournament_view
from models.tournament import Tournament


class CreateTournamentController():
    def __init__(self):
        self.view = create_tournament_view.CreateTournamentView()

    def create_tournament(self):
        name = self.view.get_name()
        location = self.view.get_location()
        rounds_nb = self.view.get_rounds_nb()
        description = self.view.get_description()
        nb_players = self.view.get_nb_players()
        self.tournament = Tournament(name, location, description, rounds_nb, nb_players=nb_players)
        self.tournament.save_tournament_to_json()
        self.view.display_tournament(self.tournament)
        return self.tournament
