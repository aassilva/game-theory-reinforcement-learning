import payoff
import agent

agents = [agent.Agent(1), agent.Agent(2), agent.Agent(3)]


if agents[2].play() == 0:
    scores = payoff.payoff_matrix_01[agents[0].play()][agents[1].play()]
elif agents[2].play() == 1:
    scores = payoff.payoff_matrix_02[agents[0].play()][agents[1].play()]
elif agents[2].play() == 2:
    scores = payoff.payoff_matrix_03[agents[0].play()][agents[1].play()]


for i, agent in enumerate(agents):
    agents[i].update_score(scores[i])

    print(agent.score)


