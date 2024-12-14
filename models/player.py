class Player:
    def __init__(self, first_name,last_name, birthday, id):
        self.name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.id = id

    def __str__(self):
        return f"{self.name} {self.last_name} {self.birthday} {self.id}"
    
    def __to_dict__(self):
        return {
            "name": self.name,
            "last_name": self.last_name,
            "birthday": self.birthday,
            "id": self.id
        }