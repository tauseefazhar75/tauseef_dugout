class Player:
    # constructor
    def __init__(self, player_id, name, role, franchise, credits):
        self.player_id = player_id
        self.name = name
        self.role = role
        self.franchise = franchise
        self.credits = credits

class FantasyTeam:
    """A fantasy XI picked by one person."""
    def __init__(self, team_name, owner):
        self.team_name = team_name
        self.owner = owner
        self.players = []
        self.captain = None
        self.vice_captain = None

    def add_player(self, player):
        self.players.append(player)

    def total_credits(self):
        total = 0
        for player in self.players:
            total = total + player.credits
        return total

    def count_by_role(self):
        counts = {"WK" : 0, "BAT" : 0, "AR" : 0, "BOWL" : 0}
        for player in self.players:
            counts[player.role] = counts[player.role] + 1
        return counts

    def __str__(self):
        return f"{self.name} ({self.franchise}, {self.role}, {self.credits} cr)"

# object
babar = Player("P089" , "Babar Azam" , "BAT" , "Peshawar Zalmi" , 10.5)
rizwan = Player("P122" , "Mohammad Rizwan" , "WK" , "Rawalpindiz" , 10.5)
fakhar = Player("P056" , "Fakhar Zaman" , "BAT" , "Lahore Qalandars" , 8.5)
saim = Player("P012" , "Saim Ayub" , "AR" , "Hyderabad Kingsmen" , 10.5)
shaheen = Player("P068" , "Shaheen Afridi" , "BOWL" , "Lahore Qalandars" , 10.5)
hasan = Player("P046" , "Hasan Ali" , "BOWL" , "Karachi Kings" , 10)

for player in [babar, rizwan, fakhar, saim, shaheen, hasan]:
    print(player)