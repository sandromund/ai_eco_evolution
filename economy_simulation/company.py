from player import Player


class Company(Player):

    def __init__(self, name, money, salary, product_price):
        super().__init__(name=name, money=money)
        self.salary = salary
        self.product_price = product_price

        self.production_per_employer = 1

        self.products_in_stock = 0

        self.customers = []
        self.employers = []

        self.costs = 0
        self.sales = 0
        self.profit = 0

    def pay_employers(self):
        for employer in self.employers:
            if self.money - self.salary >= 0:
                employer.money += self.salary
                self.money -= self.salary
            else:
                self.employers.remove(employer)
                #print(str(self) + " - OUT OF MONEY")

    def produce_products(self):
        self.products_in_stock += len(self.employers) * self.production_per_employer

    def sell_products(self):
        for customer in self.customers:
            if customer.money - self.product_price >= 0:
                if self.products_in_stock > 0:
                    self.products_in_stock -= 1
                    customer.money -= self.product_price
                    self.money += self.product_price

    def run(self):
        self.costs = len(self.employers) * self.salary
        self.sales = len(self.customers) * self.product_price
        self.profit = self.sales - self.costs

        self.pay_employers()
        self.produce_products()
        self.sell_products()

    def __str__(self):
        s = " customers: " + str(len(self.customers)) + " employers: " + str(len(self.employers))
        return super().info() + " sales: " + str(self.sales) + " costs: " + str(self.costs) + " profit: " + str(
            self.profit) + s

    def __repr__(self):
        return self.__str__()

