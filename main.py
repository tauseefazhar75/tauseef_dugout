class Player:
    #constructor 
    def __init__(self, player_id, name, role, franchise, credits):
        self.player_id = player_id
        self.name = name
        self.role = role
        self.franchise = franchise
        self.credits = credits

    def __str__(self):
        return f"{self.name} ({self.franchise}, {self.role},{self.credits} cr)"

# def __str__(self):
#     return (
#         f"Player Id : {self.player_id}\n",
#         f"Player Name : {self.name}\n",
#         f"Player Role : {self.role}\n",
#         f"Franchise Name : {self.franchise}\n",
#         f"Player Credits : {self.credits}cr\n"
#     )

# object
babar = Player("P089", "Babar Azam", "Batter", "Peshawer Zalmi", 10.5)
print (babar)
# info check krny k liya

# print(babar.name)
# print(babar.franchise)
# print(babar.credits)


rizwan = Player("P090", "Mohammad Rizwan", "Wicket Keeper", "Multan Sultans", 9.5)
print(rizwan)

shaheen = Player("P099", "Shaheen Afridi", "Bowler", "Lahore Qalandars", 9.5)
print(shaheen)

sahibzada = Player("P098", "Sahibzada Farhan", "Batter", "Quetta Gladiators", 8.5)
print(sahibzada)

shadab = Player("P097", "Shadab Khan", "All Rounder", "Islamabad United", 9.0)
print(shadab)
