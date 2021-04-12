"""
@Project Title: Optimization (minimization) with Simulated Annealing in Python for either Discrete or Continuous Problems
@Author: Jose-Alberto Salazar-Jimenez
@Email: jasj.1991@‼gmail.com
@Version: 01
"""

import matplotlib.pyplot as plt


def visualize_combinatorial_state(state, title):
    h = [] #horintal axis
    v = [] #vertial axis
    plt.figure(dpi=128)
    for i in range(len(state)):
        h.append(state[i][0])
        v.append(state[i][1])
    plt.plot(h, v, color='tab:blue', marker='o')
    plt.plot(h[0], v[0],color='tab:red',marker='o',markersize=8)
    plt.plot(h[0], v[0],color='white',marker='x',markersize=4)
    plt.plot(h[1], v[1], color='tab:orange',marker='o',markersize=8)   
    plt.xlabel('x-coordinates')
    plt.ylabel('y-coordinates')
    plt.title(title)
    plt.savefig(title+'.png', dpi=128)
    plt.show()
    
    
"""    
def visualize_continuous_state(state, boundaries, title):
    # peding development... for ploting 2d and 3d objective functions
    return None
"""

def visualize_cost_history(cost_hist, title):
    plt.plot(cost_hist) 
    plt.ylabel('cost')
    plt.xlabel('iteration')
    plt.title(title)
    plt.savefig(title+'.png', dpi=128)
    plt.show()

