class Card:
    def __init__(self, name, suit, cost):
        self.name = name
        self.suit = suit
        self.cost = cost

    def __str__(self):
        return f"[Name: {self.name}, suit: {self.suit}, cost: {self.cost}]"

    def is_card_by_name(self, name, suit):
        if self.name.lower() == name.lower() and self.suit == suit:
            return True
        else:
            return False
