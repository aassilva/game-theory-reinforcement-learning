import pandas as pd


class ArtificialIntelligence:

    def __init__(self):
        self.transition_matrix = None
        self.mount_transition_matrix()
        self.learning_rate = 0.5

    def mount_transition_matrix(self):
        """
        Strategy 0 -> To Command
        Strategy 1 -> To Cooperate
        Strategy 2 -> To Conspire
        """
        state_list = []

        estado_1 = (0, 0, 0)
        state_list.append(estado_1)
        estado_2 = (0, 0, 1)
        state_list.append(estado_2)
        estado_3 = (0, 0, 2)
        state_list.append(estado_3)

        estado_4 = (1, 0, 0)
        state_list.append(estado_4)
        estado_5 = (1, 0, 1)
        state_list.append(estado_5)
        estado_6 = (1, 0, 2)
        state_list.append(estado_6)

        estado_7 = (2, 0, 0)
        state_list.append(estado_7)
        estado_8 = (2, 0, 1)
        state_list.append(estado_8)
        estado_9 = (2, 0, 2)
        state_list.append(estado_9)

        estado_10 = (0, 1, 0)
        state_list.append(estado_10)
        estado_11 = (0, 1, 1)
        state_list.append(estado_11)
        estado_12 = (0, 1, 2)
        state_list.append(estado_12)

        estado_13 = (1, 1, 0)
        state_list.append(estado_13)
        estado_14 = (1, 1, 1)
        state_list.append(estado_14)
        estado_15 = (1, 1, 2)
        state_list.append(estado_15)

        estado_16 = (2, 1, 0)
        state_list.append(estado_16)
        estado_17 = (2, 1, 1)
        state_list.append(estado_17)
        estado_18 = (2, 1, 2)
        state_list.append(estado_18)

        estado_19 = (0, 2, 0)
        state_list.append(estado_19)
        estado_20 = (0, 2, 1)
        state_list.append(estado_20)
        estado_21 = (0, 2, 2)
        state_list.append(estado_21)

        estado_22 = (1, 2, 0)
        state_list.append(estado_22)
        estado_23 = (1, 2, 1)
        state_list.append(estado_23)
        estado_24 = (1, 2, 2)
        state_list.append(estado_24)

        estado_25 = (2, 2, 0)
        state_list.append(estado_25)
        estado_26 = (2, 2, 1)
        state_list.append(estado_26)
        estado_27 = (2, 2, 2)
        state_list.append(estado_27)

        acao_1 = 0
        acao_2 = 1
        acao_3 = 2

        # https://stackoverflow.com/questions/40186361/pandas-dataframe-with-tuple-of-strings-as-index
        d2 = [(0, 0, 0)]
        self.transition_matrix = pd.DataFrame(d2, columns=[acao_1, acao_2, acao_3], index=pd.MultiIndex.from_tuples(state_list))
