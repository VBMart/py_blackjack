from c_card import Card
import helper
import random


class Cards:
    def __init__(self):
        self.items = []

    def init_deck(self):
        self.items = []
        for suit in helper.suits:
            for ct in helper.card_types:
                card = Card(ct['name'], suit, ct['cost'])
                self.items.append(card)

    def __str__(self):
        ret = ''
        for card in self.items:
            ret += str(card) + "\n"
        return ret

    def get_sum(self):
        cards_sum = 0
        ace_count = 0
        for card in self.items:
            cards_sum += card.cost
            if card.cost == 11:
                ace_count += 1
        if cards_sum > 21:
            cards_sum -= ace_count * 10
        return cards_sum

    def is_black_jack(self):
        return self.get_sum() == 21 and len(self.items) == 2

    def get_card_by_name(self, name, suit=helper.suits[0]):
        return next((card for card in self.items if card.is_card_by_name(name, suit)), None)

    def append(self, card):
        self.items.append(card)

    def pop_random_card(self):
        cnt = len(self.items)
        card_pos = random.randint(0, cnt-1)
        return self.items.pop(card_pos)

    def clear(self):
        self.items.clear()
