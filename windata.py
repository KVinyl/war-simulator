class WinData():
    def __init__(self, wins=0, games=0):
        assert games >= wins
        self.wins = wins
        self.games = games

    def get_wins(self):
        return self.wins

    def get_games(self):
        return self.games

    def win_pct(self):
        return f'{self.wins/self.games:.3%}'
