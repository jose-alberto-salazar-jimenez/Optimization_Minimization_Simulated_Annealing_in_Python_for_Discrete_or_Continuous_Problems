"""
@Project Title: Optimization (minimization) with Simulated Annealing in Python for either Discrete or Continuous Problems
@Author: Jose-Alberto Salazar-Jimenez
@Email: jasj.1991@‼gmail.com
@Version: 01
"""


def get_nodes():
    import pandas as pd

    file = "data_for_example_01_discrete.csv"
    data = pd.read_csv(file,header=0)
    #data = data.iloc[:50]  #Slicing dataset rom 0 to the row indicated [:x] 
    coordinates = list()
    
    for index, row in data.iterrows(): #transform dataFrame to a list of coordinates
        sub_coord = [row[1],row[2]]
        coordinates.append(sub_coord) #append each row to the coordinate list
        
    return coordinates


class tsp(object):
    def __init__(self, dist_func, close_loop=True):
        self.dist_func = dist_func
        self.close_loop = close_loop
    
    def dist(self, xy):
        # sequentially calculate distance between all tsp nodes
        dist = 0
        for i in range(len(xy)-1): 
            dist += self.dist_func(xy[i+1], xy[i])

        # close the tsp loop by calculating the distance 
        # between the first and last points
        if self.close_loop:
            dist += self.dist_func(xy[0], xy[-1])
        #print(dist)
        
        return dist