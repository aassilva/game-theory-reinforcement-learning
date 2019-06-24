import pandas as pd

import agent
import payoff

# Payoff matrix for all states
p = payoff.Payoff()

# Number of rounds (it implies the computational time)
nr = 10000

agents = [agent.Agent(0), agent.Agent(1), agent.Agent(2)]

agent0_choice = []
agent1_choice = []
agent2_choice = []

d2 = [(0, 0, 0)]
strat_stats = pd.DataFrame(d2, columns=[0,1,2], index=[0,1,2])

agents[0].update_state([0, 0])
agents[1].update_state([0, 0])
agents[2].update_state([0, 0])

for i in range(0, nr):

    agents[0].play()
    agents[1].play()
    agents[2].play()

    # Saving the strategy choices by agents (quantity analysis)
    strat_stats.loc[0, agents[0].strategy] += 1
    strat_stats.loc[1, agents[1].strategy] += 1
    strat_stats.loc[2, agents[2].strategy] += 1

    # Saving the strategy choice by generation (convergence analysis)
    agent0_choice.append(agents[0].strategy)
    agent1_choice.append(agents[1].strategy)
    agent2_choice.append(agents[2].strategy)

    agents[0].update_state([agents[1].strategy, agents[2].strategy])
    agents[1].update_state([agents[0].strategy, agents[2].strategy])
    agents[2].update_state([agents[0].strategy, agents[1].strategy])

    agents[0].set_reward(p.payoffs[agents[0].state])
    agents[1].set_reward(p.payoffs[agents[1].state])
    agents[2].set_reward(p.payoffs[agents[2].state])

    agents[0].update_score()
    agents[1].update_score()
    agents[2].update_score()

cvg = open('agent0_report.txt', "w")
cvg.write("i\tchoice\n")

for i, choice in enumerate(agent0_choice):
    cvg.write(str(i)+"\t")
    cvg.write("{0:.2f}".format(choice))
    cvg.write("\n")

cvg.close()

cvg = open('agent1_report.txt', "w")
cvg.write("i\tchoice\n")

for i, choice in enumerate(agent1_choice):
    cvg.write(str(i)+"\t")
    cvg.write("{0:.2f}".format(choice))
    cvg.write("\n")

cvg.close()

cvg = open('agent2_report.txt', "w")
cvg.write("i\tchoice\n")

for i, choice in enumerate(agent2_choice):
    cvg.write(str(i)+"\t")
    cvg.write("{0:.2f}".format(choice))
    cvg.write("\n")

cvg.close()

strat_stats.to_csv(r'occurr.csv')
