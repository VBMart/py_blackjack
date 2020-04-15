from c_money import Money
from c_cards import Cards
from c_card import Card
from c_user_input import UserInput
import helper


class Game():
    def __init__(self, player_money=100):
        self.player_cards = Cards()
        self.croupier_cards = Cards()
        self.deck = Cards()
        self.deck.init_deck()
        self.player_money = Money(player_money)
        self.bet = 0

    def print_greeting_message(self):
        print('Hello')
        print('It\'s simple Black Jack game')
        print('Decks count: 1')

    def print_balance(self):
        print(f'Your balance is ${self.player_money.balance}')

    def print_cards(self):
        print('')
        print(f'Croupier cards ({self.croupier_cards.get_sum()}):')
        print(self.croupier_cards)

        print(f'Your cards ({self.player_cards.get_sum()}):')
        print(self.player_cards)

    def start_game(self):
        self.print_greeting_message()
        while True:
            print('-')
            self.print_balance()
            self.croupier_cards.clear()
            self.player_cards.clear()
            if self.player_money.balance > 0:
                self.bet = UserInput.get_valid_bet('Place your bet: ', self.player_money)
                if self.bet is None:
                    print('Game canceled')
                    break
                else:
                    self.player_money.try_to_remove(self.bet)
            else:
                print('You loose all your money')
                break

            self.deck.init_deck()
            self.croupier_cards.append(self.deck.pop_random_card())
            self.player_cards.append(self.deck.pop_random_card())
            self.player_cards.append(self.deck.pop_random_card())
            # Player's cards
            is_player_exit = False
            while True:
                self.print_cards()
                if self.player_cards.get_sum() >= 21:
                    print('You have enough score')
                    break
                print('You can hit one more card or stand.')
                print('0 - Stand')
                print('1 - Hit me')
                choose = UserInput.get_valid_int('Choose variant: ', 1, 0)
                if choose is None:
                    print('Game canceled')
                    is_player_exit = True
                    break
                elif choose == 1:
                    self.player_cards.append(self.deck.pop_random_card())
                elif choose == 0:
                    break

            if is_player_exit:
                break

            if self.player_cards.is_black_jack():
                print('You have Black Jack!')
                # Croupier have 10 or 11 score
                if self.croupier_cards.get_sum() >= 10:
                    print(f'Croupier scored {self.croupier_cards.get_sum()}.')
                    print(f'Your bet is: ${self.bet}')
                    print(f'You can win ${self.bet} or continue to get chance to win ${3 * self.bet // 2}')
                    print('0 - win now')
                    print('1 - continue')
                    choose = UserInput.get_valid_int('Choose variant: ', 1, 0)
                    if choose is None:
                        print('Game canceled')
                        is_player_exit = True
                        break
                    elif choose == 0:
                        print(f'You win ${self.bet}')
                        self.player_money.add(self.bet*2)
                        continue

            if is_player_exit:
                break

            if self.player_cards.get_sum() > 21:
                self.print_cards()
                print(f'You scored {self.player_cards.get_sum()}.')
                print('Croupier win.')
                continue

            # Croupier's cards:
            while self.croupier_cards.get_sum() < 17:
                self.croupier_cards.append(self.deck.pop_random_card())

            if self.croupier_cards.get_sum() > 21:
                self.print_cards()
                print(f'Croupier scored {self.croupier_cards.get_sum()}.')
                print(f'You win ${self.bet}')
                self.player_money.add(self.bet * 2)
                continue

            print('Final cards info:')
            self.print_cards()

            if self.croupier_cards.is_black_jack():
                print('Croupier have Black Jack!')
                if self.player_cards.is_black_jack():
                    print('You have Black Jack too. It\'s draw.')
                    print(f'You receive your ber: ${self.bet}')
                    self.player_money.add(self.bet)
                    continue
                else:
                    print('Croupier win.')
                    continue
            else:
                if self.croupier_cards.get_sum() > self.player_cards.get_sum():
                    print('Croupier win.')
                    continue
                elif self.croupier_cards.get_sum() < self.player_cards.get_sum():
                    print(f'You win ${self.bet}')
                    self.player_money.add(self.bet * 2)
                    continue
                else:
                    print('It\'s draw.')
                    print(f'You receive your ber: ${self.bet}')
                    self.player_money.add(self.bet)
                    continue
