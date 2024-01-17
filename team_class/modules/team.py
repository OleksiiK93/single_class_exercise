class Team:
    def __init__(self, name, players, coach) -> None:
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, players_name):
        if players_name in self.players:
            return True
        else:
            return False
        
    def play_game(self, won):
        if won:
            self.points += 3
