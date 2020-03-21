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


def war(player1, player2, pot, cards_down=3):
    """Players place their next {cards_down} cards to the table.
    If the players don't have enough cards, their last card will determine
    the winner of the war.
    """
    # print('WAR!')
    if len(player1) == 0:
        player1.append(pot.popleft())
    else:
        for _ in range(min(cards_down, len(player1)-1)):
            pot.appendleft(player1.popleft())

    if len(player2) == 0:
        player2.append(pot.pop())
    else:
        for _ in range(min(cards_down, len(player2)-1)):
            pot.append(player2.popleft())
    battle(player1, player2, pot)


def battle(player1, player2, pot=deque()):
    """Compares the top cards of each player.
    Player with the higher rank top card wins the played cards.
    Goes to war if tied.
    """
    card1, card2 = player1.popleft(), player2.popleft()
    pot.appendleft(card1)
    pot.append(card2)

    # print(card1.rank, 'vs', card2.rank)
    if card1 > card2:
        # print('player 1 wins', pot)
        player1.extend(rand_rev(pot))
        pot.clear()

    elif card1 < card2:
        # print('player 2 wins', pot)
        player2.extend(rand_rev(pot))
        pot.clear()

    else:
        war(player1, player2, pot)


def game():
    """Simulates one game of war and returns the winner."""
    player1, player2 = deal()
    player1_init = player1.copy()

    data.add_games(player1_init)

    while len(player1) > 0 and len(player2) > 0:
        battle(player1, player2)
        # print('player 1:', len(player1), '\tplayer 2:', len(player2), '\n')

    winner = 1 if len(player2) == 0 else 2

    if winner == 1:
        data.add_wins(player1_init)

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
