class Card:

    def __init__(self, suit, string_val, point_val):

        self.suit = suit
        self.string_val = string_val

        if point_val > 10 and string_val != "Ace":
            self.point_val = 10
        else:
            self.point_val = point_val

    def card_info(self):
        print(f"{self.string_val}_of_{self.suit}")
