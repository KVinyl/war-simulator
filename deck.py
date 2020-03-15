from collections import namedtuple

Card = namedtuple('Card', ['rank', 'suit'])


class Deck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = list('SDCH')

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __setitem__(self, position, card):
        self._cards[position] = card

    def __getitem__(self, position):
        return self._cards[position]
