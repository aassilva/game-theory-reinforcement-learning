import numpy as np
import pandas as pd

q_matrix = np.empty([27, 3], dtype=object)
state_list = []


estado_1 = ("comandar", "comandar", "comandar")
state_list.append(estado_1)
estado_2 = ("comandar", "comandar", "cooperar")
state_list.append(estado_2)
estado_3 = ("comandar", "comandar", "conspirar")
state_list.append(estado_3)

estado_4 = ("cooperar", "comandar", "comandar")
state_list.append(estado_4)
estado_5 = ("cooperar", "comandar", "cooperar")
state_list.append(estado_5)
estado_6 = ("cooperar", "comandar", "conspirar")
state_list.append(estado_6)

estado_7 = ("conspirar", "comandar", "comandar")
state_list.append(estado_7)
estado_8 = ("conspirar", "comandar", "cooperar")
state_list.append(estado_8)
estado_9 = ("conspirar", "comandar", "conspirar")
state_list.append(estado_9)

estado_10 = ("comandar", "cooperar", "comandar")
state_list.append(estado_10)
estado_11 = ("comandar", "cooperar", "cooperar")
state_list.append(estado_11)
estado_12 = ("comandar", "cooperar", "conspirar")
state_list.append(estado_12)

estado_13 = ("cooperar", "cooperar", "comandar")
state_list.append(estado_13)
estado_14 = ("cooperar", "cooperar", "cooperar")
state_list.append(estado_14)
estado_15 = ("cooperar", "cooperar", "conspirar")
state_list.append(estado_15)

estado_16 = ("conspirar", "cooperar", "comandar")
state_list.append(estado_16)
estado_17 = ("conspirar", "cooperar", "cooperar")
state_list.append(estado_17)
estado_18 = ("conspirar", "cooperar", "conspirar")
state_list.append(estado_18)

estado_19 = ("comandar", "conspirar", "comandar")
state_list.append(estado_19)
estado_20 = ("comandar", "conspirar", "cooperar")
state_list.append(estado_20)
estado_21 = ("comandar", "conspirar", "conspirar")
state_list.append(estado_21)

estado_22 = ("cooperar", "conspirar", "comandar")
state_list.append(estado_22)
estado_23 = ("cooperar", "conspirar", "cooperar")
state_list.append(estado_23)
estado_24 = ("cooperar", "conspirar", "conspirar")
state_list.append(estado_24)

estado_25 = ("conspirar", "conspirar", "comandar")
state_list.append(estado_25)
estado_26 = ("conspirar", "conspirar", "cooperar")
state_list.append(estado_26)
estado_27 = ("conspirar", "conspirar", "conspirar")
state_list.append(estado_27)

acao_1 = "comandar"
acao_2 = "cooperar"
acao_3 = "conspirar"

d2 = [(0,0,0)]
dfObj = pd.DataFrame(d2, columns=[acao_1,acao_2,acao_3], index=state_list)
indexNamesArr = dfObj.index.values

print(dfObj.loc["(comandar, comandar, comandar)", :])

#print(indexNamesArr[0])



