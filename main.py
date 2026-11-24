class Player:
    # constructor
    def __init__(self, player_id, name, role, franchise, credits):
        self.player_id = player_id
        self.name = name
        self.role = role
        self.franchise = franchise
        self.credits = credits

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