from models.player import Player
from models.tournament import Tournament
from faker import Faker


fake = Faker()

def fake_player(nombre, tournament):
    
    for i in range(nombre):
        fake_name = fake.first_name()
        fake_last_name = fake.last_name()
        fake_birthday = fake.date_of_birth(minimum_age=18, maximum_age=80)
        fake_id = fake.random_int(min=1, max=1000)
        player = Player(fake_name, fake_last_name, fake_birthday, fake_id)
        tournament.add_player(player)


tournament = Tournament("Tournoi de test", "2021-12-12", "2021-12-13", "Lyon")

fake_player(8, tournament)

tournament.add_round()
tournament.toss()
print(tournament.rounds[0])
for match in tournament.rounds[0].matches:
    print(f"{match[0][0].player.name} vs  {match[1][0].player.name} : {match[0][1]} - {match[1][1]}")

tournament.set_result(1, "1")
tournament.set_result(2, "2")
tournament.set_result(3, "3")
tournament.set_result(4, "1")

for player in tournament.tournament_players:
   
    print(f"{player.player.name} - {player.score} - {player.opponents}")

tournament.rounds[-1].end_round()
tournament.add_round()
tournament.toss()
for match in tournament.rounds[1].matches:
    print(f"{match[0][0].player.name} vs  {match[1][0].player.name} : {match[0][1]} - {match[1][1]}")

tournament.set_result(1, "1")
tournament.set_result(2, "2")
tournament.set_result(3, "3")
tournament.set_result(4, "1")

tournament.rounds[-1].end_round()
tournament.add_round()
tournament.toss()
for match in tournament.rounds[1].matches:
    print(f"{match[0][0].player.name} vs  {match[1][0].player.name} : {match[0][1]} - {match[1][1]}")
    
tournament.set_result(1, "1")
tournament.set_result(2, "2")
tournament.set_result(3, "3")
tournament.set_result(4, "1")
    
tournament.rounds[-1].end_round()
tournament.add_round()
tournament.toss()
for match in tournament.rounds[1].matches:
    print(f"{match[0][0].player.name} vs  {match[1][0].player.name} : {match[0][1]} - {match[1][1]}")
    
tournament.set_result(1, "1")
tournament.set_result(2, "2")
tournament.set_result(3, "3")
tournament.set_result(4, "1")

for match in tournament.rounds[1].matches:
    print(f"{match[0][0].player.name} vs  {match[1][0].player.name} : {match[0][1]} - {match[1][1]}")


for player in tournament.tournament_players:
   
    print(f"{player.player.name} - {player.score} - {player.opponents}")