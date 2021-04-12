"""
@Project Title: Optimization (minimization) with Simulated Annealing in Python for either Discrete or Continuous Problems
@Author: Jose-Alberto Salazar-Jimenez
@Email: jasj.1991@‼gmail.com
@Version: 01
"""

def obj_function(r):
    x = r[0]
    y = r[1]
    z = (x-2)**2+(y-3)**2 # objective function to optimize/minimize
    return z

def init_state():
    import numpy as np
    import random
    
    boundaries = [[-3,3,],[-3,3]] #boundaries, delimiting the set of solutions to a certain space
    number_dim = 2
    init_state = np.zeros((number_dim))
    for i in range(number_dim):
        init_state[i] = random.uniform(boundaries[i][0],boundaries[i][1]) # random initial state
    return init_state, boundaries