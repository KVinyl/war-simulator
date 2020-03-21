from collections import Counter, namedtuple
from deck import Deck
from windata import WinData


class DeckStats():
    """Records total wins and total games of the quantity
    of the card rank in the initial deck"""

    ranks = list('AKQJT') + [str(n) for n in range(9, 1, -1)]
    counts = list(range(5))

    def __init__(self):
        self._data = {rank: {count: WinData() for count in self.counts}
                      for rank in self.ranks}

    def add_games(self, deck):
        self._card_count = Counter({rank: 0 for rank in self.ranks})
        self._card_count.update([card.rank for card in deck])

        for rank, count in self._card_count.items():
            self._data[rank][count].games += 1

    def add_wins(self, deck):
        self._card_count = Counter({rank: 0 for rank in self.ranks})
        self._card_count.update([card.rank for card in deck])

        for rank, count in self._card_count.items():
            self._data[rank][count].wins += 1

    def get_wins(self, rank, count):
        return self._data[rank][count].get_wins()

    def get_games(self, rank, count):
        return self._data[rank][count].get_games()

    def get_win_pct(self, rank, count):
        return self._data[rank][count].win_pct()

    def display(self):
        header = ['(Rank, Count)', 'Wins', 'Games', 'Win Pct']
        data_table = [header]
        for rank in self.ranks:
            for count in self.counts:
                rc = (rank, count)
                row = [rc, self.get_wins(*rc), self.get_games(*rc),
                       self.get_win_pct(*rc)]

                data_table.append([str(cell) for cell in row])

        for row in data_table:
            print('\t'.join(row))
