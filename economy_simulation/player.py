

class Player:

    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.demands = 0
        self.debts = 0

    def info(self):
        info = self.name + " : " + str(self.money) + "€   +"
        return info + str(self.demands) + "€   -" + str(self.debts) + "€"

    def run(self):
        pass
