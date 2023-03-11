from hand_model import Hand


class Player:

    def __init__(self, data):
        self.name = data['name']
        self.hand = Hand()
        self.total = self.hand.total()
        self.turn = True

    def stay(self):
        self.turn = False

    def display_hand(self):
        for card in self.hand.cards:
            print(card)
