from card_model import Card
import random


class Deck:
    def __init__(self):
        suits = ["spades", "hearts", "clubs", "diamonds"]
        ranks = ['ace', '2', '3', '4', '5', '6', '7',
                 '8', '9', '10', 'jack', 'queen', 'king']
        self.cards = []

        # Build deck using Card class
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def __repr__(self):
        return f'Deck of {self.count()} cards'

    def count(self):
        return len(self.cards)

    def deal_card(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)
        return self
