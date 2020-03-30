class WinData():
    def __init__(self, wins=0, games=0):
        assert games >= wins
        self.wins = wins
        self.games = games

    def win_pct(self):
        return f'{self.wins/self.games:.3%}' if self.games > 0 else 'N/A'

    def incre_wins(self):
        self.wins += 1

    def incre_games(self):
        self.games += 1
