# ACO - Travelling Salesman Problem.py

import numpy as np
import matplotlib.pyplot as plt # pip install matplotlib
import AntColonyOptimisation as ACO

# Cities coordinates (for TSP)
cities = np.array([
    [0, 0], [1, 5], [5, 3], [2, 2], [3, 6], [6, 0], [4, 4], [7, 1], [8, 7], [9, 2]
])
# ACO parameters
num_ants = 10
alpha = 1
beta = 2
rho = 0.1
q = 100
dynamic_exploration_rate = 0.8
max_iterations = 100
aco = ACO.AntColonyOptimisation(cities, num_ants, alpha, beta, rho, q, dynamic_exploration_rate)
best_solution, best_distance = aco.run(max_iterations)
# Plotting the best route
best_route = np.array([cities[city] for city in best_solution + [best_solution[0]]])
plt.plot(best_route[:, 0], best_route[:, 1], marker='o', color='b')
plt.title(f"Best Route Found (Distance: {best_distance:.2f})")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()
