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
        wins, games = self.get_wins(), self.get_games()
        return f'{wins/games:.3%}' if games > 0 else 'N/A'

    def incre_wins(self):
        self.wins += 1

    def incre_games(self):
        self.games += 1
