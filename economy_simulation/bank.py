from player import Player
from loan import Loan


class Bank(Player):

    def __init__(self, name, money):
        super().__init__(name=name, money=money)
        self.db = {}
        self.interest_charges = 0.05
        self.reserves_percent = 10

    def give_loan(self, human, amount, duration):
        if (self.money / self.reserves_percent) * 100 < self.money + self.demands:
            print(human.name, "kann kein Kredit gegeben werden.")
            return False
        loan = Loan(debtor=human, creditor=self, amout=amount,
                    duration=duration, interest_charges=self.interest_charges)
        # self.money -= amount
        self.db[human.name] = loan
        self.demands += amount

        human.debts += amount
        human.money += amount

    def __str__(self):
        return super().info()

    def __repr__(self):
        return self.__str__()