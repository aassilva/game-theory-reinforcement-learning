import random


class Agent:

    def __init__(self, id):
        print("...: Agent %d ready to rock :..." % id)
        self.id = id
        self.total_score = 0.0
        self.score = 0.0
        self.strategy = 0
        self.q_score = 0.0

    def play(self):
        self.strategy = random.randint(0, 2)
        return self.strategy

    def update_score(self, score):
        self.total_score += score
        self.score = score
