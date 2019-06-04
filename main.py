import payoff
import agent
import sys

agents = [agent.Agent(0), agent.Agent(1), agent.Agent(2)]

scores = None


for i in range(0, 10):

    agents[0].play()
    agents[1].play()
    agents[2].play()

    if agents[2].strategy == 0:
        scores = payoff.payoff_matrix_01[agents[0].strategy][agents[1].strategy]
    elif agents[2].strategy == 1:
        scores = payoff.payoff_matrix_02[agents[0].strategy][agents[1].strategy]
    elif agents[2].strategy == 2:
        scores = payoff.payoff_matrix_03[agents[0].strategy][agents[1].strategy]

    try: 
        for j, agent in enumerate(agents):
            agents[j].update_score(scores[j])
    except TypeError:
        for j, agent in enumerate(agents):
            print(agents[j].strategy)
        print(scores)
        sys.exit()

print(agents[0].score, agents[0].total_score)
print(agents[1].score, agents[1].total_score)
print(agents[2].score, agents[2].total_score)









