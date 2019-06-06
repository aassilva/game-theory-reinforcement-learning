import random
from artificial_intelligence import ArtificialIntelligence


class Agent:

    def __init__(self, id):
        print("...: Agent %d ready to rock :..." % id)
        self.id = id
        self.strategy = random.randint(0, 2)
        self.intelligence = ArtificialIntelligence()
        self.epsilon = 0.1
        self.r = 0
        self.discount_rate = 0.9

        self.state = ()
        self.old_state = ()

    # https://moodle.inf.ufrgs.br/pluginfile.php/133906/mod_resource/content/1/marl.pdf
    def play(self):
        possibilities = self.intelligence.transition_matrix.loc[self.state, :]


        self.strategy = 1
        return self.strategy

    def set_reward(self, r):
        self.r = r
    # https://www.freecodecamp.org/news/an-introduction-to-q-learning-reinforcement-learning-14ac0b4493cc/
    def update_score(self):
        curr_q = self.intelligence.transition_matrix.loc[self.old_state, self.strategy]
        new_q = (1-self.intelligence.learning_rate) * curr_q + self.intelligence.learning_rate * \
                (self.r + self.discount_rate * self.q_max())

        self.intelligence.transition_matrix.loc[self.old_state, self.strategy] = new_q

    def q_max(self):
        future_state = self.intelligence.transition_matrix.loc[self.state, :]
        return future_state.max()

    def update_state(self, states):
        state_aux = [self.strategy]
        self.old_state = self.state

        for s in states:
            state_aux.append(s)

        self.state = tuple(state_aux)

