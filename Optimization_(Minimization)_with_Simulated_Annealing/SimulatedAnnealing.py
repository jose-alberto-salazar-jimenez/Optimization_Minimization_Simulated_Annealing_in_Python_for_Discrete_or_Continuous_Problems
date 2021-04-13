"""
@Project Title: Optimization (minimization) with Simulated Annealing in Python for either Discrete or Continuous Problems
@Author: Jose-Alberto Salazar-Jimenez
@Email: jasj.1991@‼gmail.com
@Version: 01
"""

import math, random, time
import PlottingSA as plot

start_time = time.time() #starting time of execution

class SimulatedAnnealing(object):
    
    def __init__(self, obj_function, state_zero, mvt_type, T=-1, alpha=-1, stop_T=-1, max_iter=-1, boundaries=None ,movt_func=None):
        
        # initial conditions
        self.T = len(state_zero) if T <= 0 else T
        self.max_T = self.T
        self.stop_T = 1e-5 if stop_T <= 0 else stop_T
        self.alpha = 0.999 if alpha <= 0 else alpha 
        self.max_iter = 3*len(state_zero)**3 if max_iter==-1 else max_iter # max_iter expression obtained empirically
        self.count_iter = 1
        self.best_iter = 1
        self.obj_function = obj_function
        self.mvt_type = mvt_type
        self.boundaries = boundaries
        random.shuffle(state_zero)
        self.initial_state = state_zero
        self.initial_cost = obj_function(self.initial_state)
        self.current_state = self.initial_state
        self.current_cost = self.initial_cost
        self.best_state = self.current_state
        self.lowest_cost = self.current_cost
        self.mvt_func = movt_func 
        self.sa_hist = [[self.count_iter,self.T,self.current_cost,1]] #data of iterations,temperatures, costs, probabilities
        
    #---------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------  
  
    def annealing_process(self):
        """
        Executes the 'Simulated Annealing' process/algorithm
        """
        print('SIMULATED ANNEALING OPTIMIZATION (MINIMIZATION)... Initiating Proces')
        
        while self.T >= self.stop_T and self.count_iter < self.max_iter: 
            candidate_state = self.mvt_func(self.current_state,self.boundaries,self.T)
            candidate_cost = self.obj_function(candidate_state)
            #print(candidate_cost)
                        
            """
            Probability to accept a candidate solution, if its worse than current solution.
            Following: exp^[-abs(candidate solution path - current solution path)/Temperature]
            Based on the Boltzmann distribution from Statistical mechanics
            """
            acceptance_probability = self.safe_exp(-abs(candidate_cost-self.current_cost)/self.T)
            
            if candidate_cost < self.current_cost:
                self.current_cost = candidate_cost
                self.current_state = candidate_state
            
            #This condition helps avoiding getting stocked into a 'local minimum' by considering the possibility of accepting a 'worst/longer' path
            else: 
                if random.random() < acceptance_probability:
                    self.current_cost = candidate_cost
                    self.current_state =  candidate_state
                
            if candidate_cost < self.lowest_cost:
                self.lowest_cost = candidate_cost
                self.best_state = candidate_state
                self.best_iter = self.count_iter
            
            self.T *= self.alpha
            self.count_iter += 1
            self.sa_hist.append([self.count_iter,self.T,self.current_cost,acceptance_probability])
            
        return self.print_results()
 
    #---------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------    
        
    def safe_exp(self, x):
        try: 
            return math.exp(x)
        except: 
            return 0
    
    #---------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------
    
    def print_results(self):
        '''
        Print/Display relevant used conditions and obtained results.
        '''
        #print('--> Movement Type:',self.mvt_type)
        print(f'--> Initial temperature:            {self.max_T:.3f}')
        print(f'--> Final temperature:               {self.T:.3f}')
        print('--> Total number of iterations: ', self.count_iter)
        print('--> Interations at lowest cost:  ',self.best_iter)
        print('--> Initial (random state) cost: ', round(self.initial_cost,3))
        print('--> Lowest cost obtained:         ', round(self.lowest_cost,3))
        if self.mvt_type == 'Combinatorial':
            ratio = 100*(self.initial_cost-self.lowest_cost)/self.initial_cost
            print(f'--> Ratio from initial cost:       {ratio: .3f}%')
        end_time = time.time() #ending time of execution
        print('--> Total Annealing Time (in seconds):    ', round(end_time-start_time, 3))
        print('--> Best State Found: ',self.best_state)
    #---------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------
    
    def visualize_state(self):
        """
        Runs 'PlottingSA..visualize_combinatorial_state in order to visualize the paths among the points
        """
        if self.mvt_type == 'Combinatorial':
            plot.visualize_combinatorial_state(self.initial_state, title='initial random state')
            plot.visualize_combinatorial_state(self.best_state, title='best state found')
        """
        # pending development
        if self.mvt_type == 'Continouus':
            plot.visualize_continuous_state(self.best_state)
        """
        
    def visualize_cost_history(self):
        """
        Plot the fitness cost through iterations.
        """
        cost_hist = []
        for element in self.sa_hist:
          cost_hist.append(element[2]) 
        plot.visualize_cost_history(cost_hist, title='cost history')
