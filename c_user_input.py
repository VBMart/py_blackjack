from c_money import Money


class UserInput():
    def __init__(self):
        pass

    @staticmethod
    def get_valid_int(question, v_max=None, v_min=None):
        while True:
            inp = input('[Type \'-\' to cancel] ' + question)
            if inp == '-':
                return None
            try:
                res = int(inp)
            except:
                pass
            else:
                if v_max is not None:
                    if v_max < res:
                        print(f'Too big value. Max: {v_max}')
                        res = None
                if v_min is not None:
                    if v_min > res:
                        print(f'Too small value. Min: {v_min}')
                        res = None
                if res is not None:
                    return res

    @staticmethod
    def get_valid_bet(question, money):
        return UserInput.get_valid_int(question, money.balance)


