import numpy as np

#Third Commanding
payoff_matrix_01 = np.empty([3, 3], dtype=object)

#Command
payoff_matrix_01[0][0] = [3, 3, 3] # Command
payoff_matrix_01[0][1] = [3, 1, 3] # Coop
payoff_matrix_01[0][2] = [2, 6, 2] # Conspire

#Coop
payoff_matrix_01[1][0] = [1, 3, 3] # Command
payoff_matrix_01[1][1] = [1, 1, 10] # Coop
payoff_matrix_01[1][2] = [2, 6, 2] # Conspire

#Conspire
payoff_matrix_01[2][0] = [6, 2, 2] # Command
payoff_matrix_01[2][1] = [6, 2, 2] # Coop
payoff_matrix_01[2][2] = [3, 3, 2] # Conspire

# --------------------------------------------- #

# Third Cooperating
payoff_matrix_02 = np.empty([3, 3], dtype=object)

# Command
payoff_matrix_02[0][0] = [3, 3, 1] # Command
payoff_matrix_02[0][1] = [10, 1, 1] # Coop
payoff_matrix_02[0][2] = [2, 6, 2] # Conspire

# Coop
payoff_matrix_02[1][0] = [1, 10, 1] # Command
payoff_matrix_02[1][1] = [7, 7, 7] # Coop
payoff_matrix_02[1][2] = [2, 6, 2] # Conspire

# Conspire
payoff_matrix_02[2][0] = [6, 2, 2] # Command
payoff_matrix_02[2][1] = [6, 2, 2] # Coop
payoff_matrix_02[2][2] = [3, 3, 2] # Conspire

# --------------------------------------------- #

# Third Conspiring
payoff_matrix_03 = np.empty([3, 3], dtype=object)

# Command
payoff_matrix_03[0][0] = [2, 2, 6] # Command
payoff_matrix_03[0][1] = [2, 2, 6] # Coop
payoff_matrix_03[0][2] = [2, 3, 3] # Conspire

# Coop
payoff_matrix_03[1][0] = [2, 2, 6] # Command
payoff_matrix_03[1][1] = [2, 2, 6] # Coop
payoff_matrix_03[1][2] = [2, 3, 3] # Conspire

# Conspire
payoff_matrix_03[2][0] = [3, 2, 3] # Command
payoff_matrix_03[2][1] = [3, 2, 3] # Coop
payoff_matrix_03[2][2] = [3, 3, 3] # Conspire
