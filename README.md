# Optimization (Minimization) with Simulated Annealing in Python for either Discrete or Continuous Problems

**Version 1.0**

This code is meant to solve optimization (minimization) problems, through a Simulated Annealing approach, were (1) the shortest path (discrete problems), as on the well-known Traveling Salesman Problem (on a set order coordinates or points), or (2) a global mininum (continuos problem) from an mathematical equation, has to be found.

The code is comprehended of the following files:
- **main.py**, where the whole algorithm is run.
- **SimulatedAnnealing.py**, here is where the simulated annealing algorithm resides.
- **DistanceFunctions.py**, funtions used to calculate the distance among points/nodes related to the "objective function" (at the moment, in version 1.0, there's only one function available, more will be added in future versions).
- **MovementFunctions.py**, with two types of movements functions, (1) combinatorial (for discrete problems), and (2) "continuous" (for continuous problems).
- **PlottingSA.py**, used to plot the "best state found" after the annealing process, and the "cost history" related to the objective function.

The algorithm works as follows:
- The user must define the **objective function** to be optimize (considering also, the importing method for the data  (if required) and/or boundaries (if required also).
- Then, from **main.py**, run the annealing process by calling **Simulated Annealing.py**, and finally, some plottings could be also displayed/saved using **PlottingSA.py**.

Take a look on how the two examples in **main.py** ("example_01_discrete" and "example_02_continuous") are defined.

Also, the user could modify **DistanceFunction.py** and/or **MovementFunction.py**, in order to tune the algorithm to the problem in question.


Note:
- Depending on the values for the "stoping" parameters (initial temperature, and max iterations), one could not get shortest path / the global minimum, because the algorithm could stop early. This requires certain experimentation from the user, in order to get the best possible result.

---

## Developer
- Jose Alberto Salazar Jiménez <jasj.1991@gmail.com>

---

## Final Comments
- Feel free to use this code on your own projects, just be sure to reference the source.
- Also, if you find any bugs or have suggestions about enhancements, or questions about any part of the code, please share them with me.

---

## References

Some of others people work I obtained ideas from:
- [Simulated Annealing algorithm to solve Travelling Salesman Problem in Python](https://github.com/chncyhn/simulated-annealing-tsp/blob/master/README.md)
- [Effective Simulated Annealing with Python](https://nathanrooy.github.io/posts/2020-05-14/simulated-annealing-with-python/)
- [simple simulated annealing](https://www.youtube.com/watch?v=T28fr9wDZrg&t=1s&ab_channel=SolvingOptimizationProblems)
- [Python Code of Simulated Annealing Optimization Algorithm](https://www.youtube.com/watch?v=T28fr9wDZrg&t=1s&ab_channel=SolvingOptimizationProblems)
- [Generalized Simulated Annealing](https://www.intechopen.com/books/computational-optimization-in-engineering-paradigms-and-applications/generalized-simulated-annealing)

I highly recommend to check them out as they have brillant solutions for other kinds of problems.

---

Thanks.
