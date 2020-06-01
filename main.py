import random
from deck import Deck
from player import Player, winner
from card import compare


def snap(number_of_packs):
    deck = Deck.merge(number_of_packs)
    deck.shuffle()
    players = [Player('player 1'), Player('player 2')]
    prev = None
    center_pile = 0

    while deck.cards:
        curr = deck.draw()
        center_pile += 1
        print("--------------")
        print(curr)
        print(prev)
        try:
            match = compare(curr, prev)
        except AttributeError:
            match = False

        if match:
            player = random.choice(players)
            player.add(center_pile)
            center_pile = 0
            print(player.name)
            print("SNAP")

        prev = curr

    return winner(players[0], players[1])


if __name__ == '__main__':
    packs = None
    while type(packs) != int:
        try:
            packs = int(input('Please Enter the number of packs to use: ').strip())
        except ValueError:
            print('Enter a valid number')

    winner = snap(packs)
    print(winner.name)
