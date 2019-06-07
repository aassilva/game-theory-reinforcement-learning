class Payoff:

    def __init__(self):
        self.payoffs = None
        self.init_payoff_matrix()

    def init_payoff_matrix(self):
        self.payoffs = dict()

        self.payoffs[(0, 0, 0)] = 3
        self.payoffs[(1, 0, 0)] = 1
        self.payoffs[(2, 0, 0)] = 6

        self.payoffs[(0, 1, 0)] = 3
        self.payoffs[(1, 1, 0)] = 1
        self.payoffs[(2, 1, 0)] = 6

        self.payoffs[(0, 2, 0)] = 2
        self.payoffs[(1, 2, 0)] = 2
        self.payoffs[(2, 2, 0)] = 3

        self.payoffs[(0, 0, 1)] = 3
        self.payoffs[(1, 0, 1)] = 1
        self.payoffs[(2, 0, 1)] = 6

        self.payoffs[(0, 0, 2)] = 1
        self.payoffs[(1, 0, 2)] = 2
        self.payoffs[(2, 0, 2)] = 3

        self.payoffs[(0, 1, 1)] = 10
        self.payoffs[(1, 1, 1)] = 7
        self.payoffs[(2, 1, 1)] = 6

        self.payoffs[(0, 1, 2)] = 1
        self.payoffs[(1, 1, 2)] = 2
        self.payoffs[(2, 1, 2)] = 3

        self.payoffs[(0, 2, 1)] = 1
        self.payoffs[(1, 2, 1)] = 2
        self.payoffs[(2, 2, 1)] = 3

        self.payoffs[(0, 2, 2)] = 1
        self.payoffs[(1, 2, 2)] = 2
        self.payoffs[(2, 2, 2)] = 3