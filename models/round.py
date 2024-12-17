from datetime import datetime


class Round:
    def __init__(self, number):
        self.number = number
        self.matches = []
        self.start_date = datetime.now()
        self.end_date = None
        self.name = f"Round {self.number}"

    def add_match(self, player1, player2, player1_score=None, player2_score=None):

        match = ([player1, player1_score], [player2, player2_score])
        self.matches.append(match)

    def end_round(self):
        self.end_date = datetime.now()

    def __str__(self):
        return f"{self.name} - {self.start_date}"

    def __to_dict__(self):

        round_dict = {
            "number": self.number,
            "name": self.name,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat() if self.end_date else None,
            "matches": []
        }

        for index, match in enumerate(self.matches):
            player1 = match[0][0].player.id
            player2 = match[1][0].player.id
            player1_score = match[0][1]
            player2_score = match[1][1]

            round_dict["matches"].append({
                "match": index+1,
                "player1": player1,
                "player2": player2,
                "player1_score": player1_score,
                "player2_score": player2_score
            })
        return round_dict
