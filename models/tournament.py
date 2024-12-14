from datetime import datetime


class Tournament:
    def __init__(self, name, location, description, nb_rounds=4, nb_players=8):
        self.name = name
        self.location = location
        self.description = description
        self.nb_rounds = nb_rounds
        self.rounds = []
        self.tournament_players = []
        self.start_date = datetime.now()
        self.end_date = None

    def __str__(self):
        return f"{self.name} - {self.location} - {self.date} - {self.rounds} rounds"

    def __repr__(self):
        return f"{self.name} - {self.location} - {self.date} - {self.rounds} rounds"
    
    def __to_dict__(self):
        return {
            "name": self.name,
            "location": self.location,
            "description": self.description,
            "nb_rounds": self.nb_rounds,
            "rounds": self.rounds,
            "players": self.tournament_players,
            "start_date": self.start_date,
            "end_date": self.end_date
        }