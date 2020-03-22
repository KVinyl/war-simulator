from collections import deque
from deck import Deck
from deckstats import DeckStats
from random import choice, shuffle


data = DeckStats()


def rand_rev(deck):
    """Returns the deck in reversed order 50% of the time.
    Otherwise returns the deck unchanged.
    """
    if choice([0, 1]):
        deck.reverse()
    return deck


def war(deck1, deck2, pot, cards_down=3):
    """Players place their next {cards_down} cards to the table.
    If the players don't have enough cards, their last card will determine
    the winner of the war.
    """
    # print('WAR!')
    if len(deck1) == 0:
        deck1.append(pot.popleft())
    else:
        for _ in range(min(cards_down, len(deck1)-1)):
            pot.appendleft(deck1.popleft())

    if len(deck2) == 0:
        deck2.append(pot.pop())
    else:
        for _ in range(min(cards_down, len(deck2)-1)):
            pot.append(deck2.popleft())

    battle(deck1, deck2, pot)


def battle(deck1, deck2, pot=deque()):
    """Compares the top cards of each player.
    Player with the higher rank top card wins the played cards.
    Goes to war if tied.
    """
    card1, card2 = deck1.popleft(), deck2.popleft()
    pot.appendleft(card1)
    pot.append(card2)

    # print(card1.rank, 'vs', card2.rank)
    if card1 == card2:
        war(deck1, deck2, pot)

    else:
        win_deck = deck1 if card1 > card2 else deck2
        # player = "player 1" if card1 > card2 else "player 2"
        # print(player, "collects", pot)
        win_deck.extend(rand_rev(pot))
        pot.clear()


def game():
    """Simulates one game of war and returns the winner."""
    deck1, deck2 = deal()
    deck1_init = deck1.copy()

    data.add_games(deck1_init)

    while len(deck1) > 0 and len(deck2) > 0:
        battle(deck1, deck2)
        # print('player 1:', len(deck1), '\tplayer 2:', len(deck2), '\n')

    winner = 1 if len(deck2) == 0 else 2

    if winner == 1:
        data.add_wins(deck1_init)

    return winner


def deal():
    """Returns an evenly divided shuffle deck to two players."""
    deck = Deck()
    shuffle(deck)

    return [deque(deck[:26]), deque(deck[26:])]


def main():
    """Simulates multiple games of war.
    Displays winning percentage based on number of aces in
    player one's deck at the start of each game.
    """
    num_games = 10000
    for _ in range(num_games):
        game()

    data.display()


if __name__ == "__main__":
    main()
