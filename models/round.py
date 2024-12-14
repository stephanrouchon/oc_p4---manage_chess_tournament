from datetime import datetime

class Round:
    def __init__(self, number):
        self.number = number
        self.matches = []
        self.start_date = datetime.now()
        self.end_date = None
        self.name = f"Round {self.number}"
    
    def __str__(self):
        return f"{self.name} - {self.start_date}"
    
    def __to_dict__(self):
        return {
            "number": self.number,
            "matches": self.matches,
            "start_date": self.start_date,
            "end_date": self.end_date,
        }
    


