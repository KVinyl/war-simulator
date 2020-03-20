class Card():
    ranks = [str(n) for n in range(2, 10)] + list('TJQKA')
    rank_tran = {rank: n for n, rank in enumerate(ranks, 2)}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self._numrank = self.rank_tran[rank]

    def __eq__(self, other):
        return self._numrank == other._numrank

    def __ne__(self, other):
        return self._numrank != other._numrank

    def __lt__(self, other):
        return self._numrank < other._numrank

    def __gt__(self, other):
        return self._numrank > other._numrank

    def __repr__(self):
        return f'Card({self.rank}, {self.suit})'
