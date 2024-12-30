from datetime import datetime
import random
import uuid

from models.round import Round
from models.tournament_players import TournamentPlayer

WIN_POINT = 1
LOOSE_POINT = 0
DRAW_POINT = 0.5


class Tournament:
    """create tournament
    """
    def __init__(self, name, location, description, nb_rounds=4, nb_players=8, id=None):
        self.name = name
        self.location = location
        self.description = description
        self.id = uuid.uuid4() if id is None else id
        self.nb_rounds = nb_rounds
        self.nb_players = nb_players
        self.rounds = []
        self.tournament_players = []
        self.start_date = datetime.now()
        self.end_date = None

    def add_player_in_tournament(self, player):
        """add player in tournament

        Args:
            player (_type_): object

        Returns:
            _type_: object
        """

        tournament_player = TournamentPlayer(player)
        self.tournament_players.append(tournament_player)
        return tournament_player

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

    def set_result(self, match, result):
        index_match = match - 1
        player1 = self.rounds[-1].matches[index_match][0][0]
        player2 = self.rounds[-1].matches[index_match][1][0]
        player1.opponents.append(player2.player.id)
        player2.opponents.append(player1.player.id)

        if result == 1:
            self.rounds[-1].matches[index_match][0][1] = WIN_POINT
            self.rounds[-1].matches[index_match][1][1] = LOOSE_POINT
            player1.score += WIN_POINT
        if result == 2:
            self.rounds[-1].matches[index_match][0][1] = LOOSE_POINT
            self.rounds[-1].matches[index_match][1][1] = WIN_POINT
            player2.score += WIN_POINT
        if result == 3:
            self.rounds[-1].matches[index_match][0][1] = DRAW_POINT
            self.rounds[-1].matches[index_match][1][1] = DRAW_POINT
            player1.score += DRAW_POINT
            player2.score += DRAW_POINT

    def change_pair(self, pairs, blocked_player, sorted_players):
        for i, [player1, player2] in enumerate(pairs):
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

    def end_round(self):
        self.rounds[-1].end_date = datetime.now()

    def end_tournament(self):
        self.end_date = datetime.now()

    def __str__(self):
        return f"{self.name} - {self.location} - {self.start_date} - {self.rounds} rounds"

    def __repr__(self):
        return f"{self.name} - {self.location} - {self.start_date} - {self.rounds} rounds"

    def __to_dict__(self):
        return {
            "name": self.name,
            "location": self.location,
            "description": self.description,
            "nb_rounds": self.nb_rounds,
            "nb_players": self.nb_players,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat() if self.end_date else None,
            "id": str(self.id),
            "players": [player.__to_dict__() for player in self.tournament_players],
            "rounds": [round.__to_dict__() for round in self.rounds],
        }
