from card import Card
import random


class Deck(object):
    def __init__(self, cards=None):
        if cards is None:
            cards = [Card(suit, value)
                     for suit in Card.SUITS
                     for value in Card.VALUES]
        self.cards = cards

    def __add__(self, other):
        return self.__class__(self.cards + other.cards)

    @classmethod
    def merge(cls, num):
        return sum((cls() for _ in range(num)), cls([]))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop(0)
