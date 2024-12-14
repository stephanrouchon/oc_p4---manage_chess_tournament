from datetime import datetime
import random

from oc_p4.models.round import Round
from oc_p4.models.tournament_players import TournamentPlayer


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

    def add_player(self, player):
        tournament_player = TournamentPlayer(player)
        self.tournament_players.append(tournament_player)

    def add_round(self):
        self.rounds.append(Round(len(self.rounds) + 1))
    
    def toss(self):
        random.shuffle(self.tournament_players)
        if len(self.rounds) == 1:
            self.first_toss()
        else:
            self.other_toss()

    def first_toss(self):
        for i in range(0, len(self.tournament_players), 2):
            self.rounds[0].add_match(self.tournament_players[i], self.tournament_players[i + 1])

    def other_toss(self):
        sorted_players = self.sorted_players_by_score()
        pairs = []
        while sorted_players:
            player1 = sorted_players.pop(0)
            player2 = next((player for player in sorted_players if player not in player1.opponents), None)
            if player2:
                pairs.append((player1, player2))
                sorted_players.remove(player2)
            else:
                if not self.change_pair(pairs, player1, sorted_players):
                    raise Exception("No possible pair")
        
        for pair in pairs:
            self.rounds[-1].add_match(pair[0], pair[1])

    def change_pair(self, pairs, blocked_player, sorted_players):
        for i,[player1, player2] in enumerate(pairs):
            if player2 and blocked_player not in player1.opponents:
                pairs[i] = (player1, blocked_player)
                sorted_players.append(player2)
                return True
            elif player2 and blocked_player not in player2.opponents:
                pairs[i] = (player2, blocked_player)
                sorted_players.append(player1)
                return True
        return False

    def sorted_players_by_score(self):
        return sorted(self.tournament_players, key=lambda x: x.score, reverse=True)

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