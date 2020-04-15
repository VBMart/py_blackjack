from c_cards import Cards
from c_money import Money
import unittest


class TestCards(unittest.TestCase):

    def test_card(self):
        deck = Cards()
        deck.init_deck()
        self.assertNotEqual(None, deck.get_card_by_name('Ace'))
        self.assertEqual(None, deck.get_card_by_name('None'))
        card = deck.get_card_by_name('King')
        self.assertEqual(10, card.cost)
        self.assertEqual('King', card.name)

    def test_sum(self):
        deck = Cards()
        deck.init_deck()

        player_cards = Cards()
        player_cards.append(deck.get_card_by_name('Ace'))
        player_cards.append(deck.get_card_by_name('10'))
        self.assertEqual(21, player_cards.get_sum())

        player_cards = Cards()
        player_cards.append(deck.get_card_by_name('Ace'))
        player_cards.append(deck.get_card_by_name('10'))
        player_cards.append(deck.get_card_by_name('Ace'))
        self.assertEqual(12, player_cards.get_sum())

        player_cards = Cards()
        player_cards.append(deck.get_card_by_name('Jack'))
        player_cards.append(deck.get_card_by_name('Queen'))
        self.assertEqual(20, player_cards.get_sum())

    def test_money(self):
        money = Money()
        money.add(10)
        self.assertEqual(10, money.balance)
        res = money.try_to_remove(5)
        self.assertEqual(5, money.balance)
        self.assertEqual(True, res)
        res = money.try_to_remove(20)
        self.assertEqual(5, money.balance)
        self.assertEqual(False, res)

if __name__ == '__main__':
    unittest.main()
