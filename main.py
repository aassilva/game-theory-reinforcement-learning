import agent
import payoff

agents = [agent.Agent(0), agent.Agent(1), agent.Agent(2)]

agents[0].update_state([0, 0])
agents[1].update_state([0, 0])
agents[2].update_state([0, 0])

for i in range(0, 1):

    agents[0].play()
    agents[1].play()
    agents[2].play()

    agents[0].update_state([agents[1].strategy, agents[2].strategy])
    agents[1].update_state([agents[0].strategy, agents[2].strategy])
    agents[2].update_state([agents[0].strategy, agents[1].strategy])

    print(agents[0].strategy, agents[1].strategy, agents[2].strategy)

    print(agents[0].state)
    print(agents[1].state)
    print(agents[2].state)

    if agents[2].strategy == 0:
        scores = payoff.payoff_matrix_01[agents[0].strategy][agents[1].strategy]
    elif agents[2].strategy == 1:
        scores = payoff.payoff_matrix_02[agents[0].strategy][agents[1].strategy]
    elif agents[2].strategy == 2:
        scores = payoff.payoff_matrix_03[agents[0].strategy][agents[1].strategy]

    # print(agents[0].transition_matrix.loc[state, :])

    for j, agent in enumerate(agents):
        agents[j].update_score(scores[j])

    print(agents[0].transition_matrix.loc[agents[0].state, :])
    print(agents[1].transition_matrix.loc[agents[1].state, :])
    print(agents[2].transition_matrix.loc[agents[2].state, :])









