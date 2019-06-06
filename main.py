import sys
import agent
import payoff

p = payoff.Payoff()
agents = [agent.Agent(0), agent.Agent(1), agent.Agent(2)]

#agents[0].strategy = 0
#agents[1].strategy = 1
#agents[2].strategy = 1

agents[0].update_state([0, 0])
agents[1].update_state([0, 0])
agents[2].update_state([0, 0])

#agents[0].set_reward(p.payoffs[agents[0].state])
#agents[1].set_reward(p.payoffs[agents[1].state])
#agents[2].set_reward(p.payoffs[agents[2].state])

#agents[0].intelligence.transition_matrix.loc[agents[0].state, 0] = 10
#agents[0].intelligence.transition_matrix.loc[agents[0].state, 1] = 7
#agents[0].intelligence.transition_matrix.loc[agents[0].state, 2] = 6


#print(agents[0].intelligence.transition_matrix.loc[agents[0].state, :])
#print(agents[0].intelligence.transition_matrix.loc[agents[0].state, :].max())


#print(agents[0].r, agents[1].r, agents[2].r)


#sys.exit()

for i in range(0, 1):

    agents[0].strategy = 0  # .play()
    agents[1].strategy = 0  # .play()
    agents[2].strategy = 2  # .play()

    print(agents[0].strategy, agents[1].strategy, agents[2].strategy)

    agents[0].update_state([agents[1].strategy, agents[2].strategy])
    agents[1].update_state([agents[0].strategy, agents[2].strategy])
    agents[2].update_state([agents[0].strategy, agents[1].strategy])

    agents[0].set_reward(p.payoffs[agents[0].state])
    agents[1].set_reward(p.payoffs[agents[1].state])
    agents[2].set_reward(p.payoffs[agents[2].state])

    agents[0].update_score()
    agents[1].update_score()
    agents[2].update_score()

    # print(agents[0].intelligence.transition_matrix.loc[agents[0].old_state, :])
    # print(agents[1].intelligence.transition_matrix.loc[agents[1].old_state, :])
    # print(agents[2].intelligence.transition_matrix.loc[agents[2].old_state, :])








