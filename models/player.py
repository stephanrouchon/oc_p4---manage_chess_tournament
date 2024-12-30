class Player:
    def __init__(self, first_name, last_name, birthday, id):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.id = id
        self.name = f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.birthday} {self.id}"

    def __to_dict__(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birthdate": self.birthday,
            "id": self.id
        }
