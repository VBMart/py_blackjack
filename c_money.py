import helper


class Money():
    def __init__(self, balance=0):
        self.balance = balance

    def add(self, value):
        self.balance += value

    def try_to_remove(self, value):
        if self.balance >= value:
            self.balance -= value
            return True
        else:
            return False
