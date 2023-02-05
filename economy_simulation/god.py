from human import Human

import numpy as np
import names


class God:

    def __init__(self):
        self.humans_iq_mean = 100
        self.humans_iq_standard_deviation = 15

        self.human_start_money_mean = 100
        self.human_start_money_standard_deviation = 10

    def crate_humans(self, n):
        iq_list = np.random.normal(self.humans_iq_mean, self.humans_iq_standard_deviation, n)
        money_list = np.random.normal(self.human_start_money_mean, self.human_start_money_standard_deviation, n)
        money_list = [x if x > 0 else 0 for x in money_list]
        name_list = [names.get_full_name() for _ in range(n)]
        return [Human(name=name_list[i], money=int(money_list[i]), iq=int(iq_list[i])) for i in range(n)]


