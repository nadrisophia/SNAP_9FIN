from collections import namedtuple


class Card(namedtuple('Card', 'suit value')):
    SUITS = ('hearts', 'diamonds', 'clubs', 'spades')
    VALUES = ('ACE', '2', '3', '4', '5', '6',
              '7', '8', '9', '10', 'J', 'Q', 'K'
              )


def compare(card1, card2):
    return card1.suit == card2.suit or card1.value == card2.value
