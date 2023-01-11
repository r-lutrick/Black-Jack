class Dealer (Player):
    def __init__(self, name):
        super().__init__(name)

    def hit(self, card):
        # Logic for dealer based on current hand value
        if (card.point_val == 1):
            temp_total = self.total + 11
            if (temp_total <= 21):
                card.point_val = 11

        self.hand.append(card)
        self.turn = True
        return self
