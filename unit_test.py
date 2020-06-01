import unittest
from card import Card, compare
from deck import Deck
from player import Player, winner


class TestCard(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("heart", "9")
        self.card2 = Card("spade", "9")
        self.card3 = Card("spade", "J")

    def test_compare(self):
        self.assertTrue(compare(self.card1, self.card2))
        self.assertTrue(compare(self.card3, self.card2))
        self.assertFalse(compare(self.card1, self.card3))


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck1 = Deck()
        self.deck2 = Deck.merge(2)
        self.deck3 = Deck.merge(1)

    def test_init(self):
        self.assertEqual(self.deck1.cards.__len__(), 52)
        self.assertEqual(self.deck2.cards.__len__(), 104)
        self.assertEqual(self.deck3.cards.__len__(), 52)

    def test_draw(self):
        self.deck1.draw()
        self.assertEqual(self.deck1.cards.__len__(), 51)


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("player1")
        self.player2 = Player("player2")

    def test_add(self):
        self.player1.add(5)
        self.player2.add(6)
        self.assertEqual(self.player1.win_pile, 5)
        self.assertEqual(self.player2.win_pile, 6)

    def test_winner(self):
        self.assertTrue(winner(self.player1, self.player2).__eq__(self.player2))


if __name__ == '__main__':
    unittest.main()
