import operator


class Player(object):
    def __init__(self, name, win_pile_size=0):
        self.win_pile = win_pile_size
        self.name = name

    def add(self, win_pile_size):
        self.win_pile += win_pile_size


def winner(player1, player2):
    return max(player1, player2, key=operator.attrgetter('win_pile'))
