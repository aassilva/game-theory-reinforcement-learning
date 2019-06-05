import random
from artificial_intelligence import ArtificialIntelligence


class Agent:

    def __init__(self, id):
        print("...: Agent %d ready to rock :..." % id)
        self.id = id
        self.strategy = 0
        self.intelligence = ArtificialIntelligence()

        self.state = ()

    def play(self):
        self.strategy = random.randint(0, 2)
        return self.strategy

    def update_score(self, score):
        #self.transition_matrix.loc[self.state, self.strategy] = score
        old_q = self.intelligence.transition_matrix.loc[self.state, :]

    def update_state(self, states):
        state_aux = [self.strategy]

        for s in states:
            state_aux.append(s)

        self.state = tuple(state_aux)

