from player import Player


class Human(Player):

    def __init__(self, name, money, iq):
        super().__init__(name=name, money=money)
        self.iq = iq

    def __str__(self):
        return super().info() + " iq: " + str(self.iq)

    def __repr__(self):
        return self.__str__()