from company import Company
from bank import Bank


class World:

    def __init__(self, humans):

        self.humans = humans

        self.banks = [Bank(name="Bank One", money=800)]

        self.companies = [Company(name="Lebensmittel GmbH", money=100, salary=2, product_price=2),
                          Company("Lecker AG", money=200, salary=2, product_price=2)]
        self.players = self.banks + self.humans + self.companies

    def run(self, n):
        for i in range(n):
            for player in self.players:
                player.run()

    def count_money(self):
        return sum(p.money for p in self.players)

    def meta_data(self):
        print(" -- World --")
        print("Current money in circulation:", self.count_money())
        print(" --- Humans ---")
        for human in self.humans:
            print(human)
        print(" --- Banks --- ")
        for bank in self.banks:
            print(bank)
        print(" --- Companies --- ")
        for company in self.companies:
            print(company)

