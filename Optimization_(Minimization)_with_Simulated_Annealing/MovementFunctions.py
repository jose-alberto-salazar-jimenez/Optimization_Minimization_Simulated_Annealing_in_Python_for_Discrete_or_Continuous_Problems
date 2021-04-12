"""
@Project Title: Optimization (minimization) with Simulated Annealing in Python for either Discrete or Continuous Problems
@Author: Jose-Alberto Salazar-Jimenez
@Email: jasj.1991@‼gmail.com
@Version: 01
"""


def combinatorial_movement(current_state,boundaries=None,damping=None): #random iterator
    """
    Swaps a 'random' quantity of nodes along the given 'current state' (catesian plane?)
    """
    from random import randint
    candidate_state = list(current_state)
    #i = random.randint(1, self.N - 1) # if you wannt the first node to be fixed 
    #l = random.randint(2, self.N - 1) # if you wannt the first node to be fixed 
    i = randint(0, len(current_state)-1)
    l = randint(1, len(current_state)-1)  
    candidate_state[i:(i+l)] = reversed(candidate_state[i:(i+l)])
    return candidate_state


def continuous_movement(current_state,boundaries=None,damping=1):
    """
    Perturbs the 'current state' by a 'small random' amount
    """
    from random import random, uniform
    #neighbor = [item + ((random() - 0.5) * self.damping) for item in self.current_state]
    #candidate_state = [i + 0.1*(random.random() - 0.5) for i in current_state]
    #print(neighbor)
    candidate_state = []
    # clip to upper and lower bounds
    #print(damping)
    if boundaries:
        for i in range(len(current_state)):
            lower_boundary, upper_boundary = boundaries[i]  
            candidate_state.append(current_state[i]+0.1*damping*(uniform(lower_boundary,upper_boundary)))
            #candidate_state.append(current_state[i]+0.1*damping*(random()-0.5))
            candidate_state[i] = min(max(candidate_state[i], lower_boundary), upper_boundary)
    else:
        candidate_state = [i + 0.1*(random()-0.5) for i in current_state]   
    return candidate_state