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

    def __count(self, deck):
        self._card_count = Counter({rank: 0 for rank in self.ranks})
        self._card_count.update([card.rank for card in deck])

    def __increment(self, func):
        for rank, count in self._card_count.items():
            getattr(self._data[rank][count], func)()

    def add_wins(self, deck):
        self.__count(deck)
        self.__increment('incre_wins')

    def add_games(self, deck):
        self.__count(deck)
        self.__increment('incre_games')

    def wins(self, rank, count):
        return self._data[rank][count].get_wins()

    def games(self, rank, count):
        return self._data[rank][count].get_games()

    def win_pct(self, rank, count):
        return self._data[rank][count].win_pct()

    def display(self):
        header = ['Rank', 'Count', 'Wins', 'Games', 'Win Pct']
        data_table = [header]
        for rank in self.ranks:
            for count in self.counts:
                rc = (rank, count)
                row = [*rc, self.wins(*rc), self.games(*rc),
                       self.win_pct(*rc)]

                if count > 0:
                    row[0] = ''
                else:
                    data_table.append([])

                data_table.append([str(cell) for cell in row])

        for row in data_table:
            print('\t'.join(row))
