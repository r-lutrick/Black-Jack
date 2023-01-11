from deck_model import Deck


class Hand:
    def __init__(self):
        self.cards = []

    def hit(self):
        self.cards.append(Deck.deal_card())

    def total(self):
        val = 0
        for card in self.cards:
            if card.rank == 'ace':
                if ((val + 11) > 21):
                    val += 1
                else:
                    val += 11
            elif not type(card.rank) == int:
                val += 10
            else:
                val += int(card.rank)
        return val
