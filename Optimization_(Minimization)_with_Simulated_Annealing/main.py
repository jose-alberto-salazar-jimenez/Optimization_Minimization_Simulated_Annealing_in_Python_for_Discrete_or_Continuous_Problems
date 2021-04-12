
"""
@Project Title: Optimization (minimization) with Simulated Annealing in Python for either Discrete or Continuous Problems
@Author: Jose-Alberto Salazar-Jimenez
@Email: jasj.1991@‼gmail.com
@Version: 01

References:
https://github.com/chncyhn/simulated-annealing-tsp/blob/master/README.md
https://nathanrooy.github.io/posts/2020-05-14/simulated-annealing-with-python/
https://github.com/nathanrooy/simulated-annealing/blob/master/simulated_annealing/sa.py
https://www.intechopen.com/books/computational-optimization-in-engineering-paradigms-and-applications/generalized-simulated-annealing
https://www.youtube.com/watch?v=T28fr9wDZrg&t=1s&ab_channel=SolvingOptimizationProblems
"""

# required
from SimulatedAnnealing import SimulatedAnnealing as SimAnn
from DistanceFunctions import euclidean_dist
from MovementFunctions import combinatorial_movement as comb_mvt
from MovementFunctions import continuous_movement as cont_mvt

# for examples
from example_01_discrete import get_nodes, tsp
from example_02_continuous import obj_function, init_state


def example_01_discrete():
    coordinates = get_nodes()
    tsp_dist = tsp(dist_func=euclidean_dist,close_loop=True).dist
    sa = SimAnn(tsp_dist,coordinates,mvt_type='Combinatorial', movt_func=comb_mvt)
    sa.annealing_process()
    sa.visualize_state() 
    sa.visualize_cost_history()
    return None

def example_02_continuous():
    obj_func = obj_function
    state_zero,boundaries = init_state()  
    sa = SimAnn(obj_func, state_zero, mvt_type='Continuous', boundaries=boundaries, T=4, max_iter=5000, movt_func=cont_mvt)
    sa.annealing_process()
    sa.visualize_cost_history()
    return None


if __name__ == "__main__":
    example_01_discrete()  # lowest cost (shortest path) should be lower than 975 (lowest obtained experiments was around 880)
    #example_02_continuous() # lowest cost (global minimum) is 0.0 