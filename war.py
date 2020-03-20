from collections import deque
from deck import Deck
from random import choice, shuffle


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
        if choice([0, 1]):
            pot.reverse()
        # print('player 1 wins', pot)
        player1.extend(pot)
        pot.clear()

    elif card1 < card2:
        if choice([0, 1]):
            pot.reverse()
        # print('player 2 wins', pot)
        player2.extend(pot)
        pot.clear()

    else:
        war(player1, player2, pot)


def game(player1, player2):
    """Simulates one game of war and returns the winner."""
    while len(player1) > 0 and len(player2) > 0:
        battle(player1, player2)
        # print('player 1:', len(player1), '\tplayer 2:', len(player2), '\n')

    return 1 if len(player2) == 0 else 2


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
    wins1 = wins2 = 0

    n_ace_wins = {n: 0 for n in range(5)}
    n_ace_games = {n: 0 for n in range(5)}

    for _ in range(num_games):
        player1, player2 = deal()

        aces = len([card for card in player1 if card.rank == 'A'])
        n_ace_games[aces] += 1

        if game(player1, player2) == 1:
            wins1 += 1
            n_ace_wins[aces] += 1
        else:
            wins2 += 1

    print('Player 1 wins:', wins1)
    print('Player 2 wins:', wins2)

    for n in range(5):
        print(f'{n} aces: {n_ace_wins[n]/n_ace_games[n]:.3%}')


if __name__ == "__main__":
    main()
