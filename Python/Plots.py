# Plots.py

import numpy as np
import AntColonyOptimisation as ACO
import ParticleSwarmOptimisation as PSO

# ASO - Timing and Data Collection
import time
def run_aco_multiple_trials(num_trials, aco_params, max_iterations=100):
    efficiencies = []
    solution_qualities = []
    for _ in range(num_trials):
        start_time = time.time()
        aco = ACO.AntColonyOptimisation(**aco_params)
        best_solution, best_cost, _ = aco.run(max_iterations)  # Pass max_iterations here
        end_time = time.time()
        # Store efficiency (time) and solution quality (best cost)
        efficiencies.append(end_time - start_time)
        solution_qualities.append(best_cost)
    return efficiencies, solution_qualities

# PSO - Timing and Data Collection
def run_pso_multiple_trials(num_trials, pso_params):
    efficiencies = []
    solution_qualities = []
    for _ in range(num_trials):
        start_time = time.time()
        pso = PSO.ParticleSwarmOptimisation(**pso_params)
        best_values = pso.run()  # PSO returns best values at each iteration
        end_time = time.time()
        # Store efficiency (time) and solution quality (best value at last iteration)
        efficiencies.append(end_time - start_time)
        solution_qualities.append(best_values[-1]) 
    return efficiencies, solution_qualities

# Plotting - Efficiency Comparison
import matplotlib.pyplot as plt
def plot_efficiency(aco_efficiencies, pso_efficiencies):
    plt.figure(figsize=(10, 5))
    plt.boxplot([aco_efficiencies, pso_efficiencies], labels=["ACO", "PSO"])
    plt.title('Efficiency Comparison (Time Taken)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.show()

# Plotting - Solution Quality Comparison
def plot_solution_quality(aco_qualities, pso_qualities):
    plt.figure(figsize=(10, 5))
    plt.boxplot([aco_qualities, pso_qualities], labels=["ACO", "PSO"])
    plt.title('Solution Quality Comparison')
    plt.ylabel('Best Cost / Value')
    plt.grid(True)
    plt.show()

# Plotting - Convergence Rate Comparison
def plot_convergence(pso_best_values, aco_best_values):
    plt.figure(figsize=(10, 5))
    plt.plot(aco_best_values, label='ACO')
    plt.plot(pso_best_values, label='PSO')
    plt.title('Convergence Rate Comparison')
    plt.xlabel('Iteration')
    plt.ylabel('Best Value')
    plt.legend()
    plt.grid(True)
    plt.show()

aco_params = {
    "cities": np.array([
        [0, 0], [1, 5], [5, 3], [2, 2], [3, 6], [6, 0], [4, 4], [7, 1], [8, 7], [9, 2]
    ]),
    "num_ants": 10,
    "alpha": 1,
    "beta": 2,
    "rho": 0.1,
    "q": 100,
    "dynamic_exploration_rate": 0.8
}
pso_params = {
    "num_particles": 30,
    "inertia": 0.7,
    "cognitive": 1.5,
    "social": 2.0,
    "adaptive_social_influence": 1.0,
    "num_iterations": 100
}

# Example of usage
aco_efficiencies, aco_qualities = run_aco_multiple_trials(10, aco_params, max_iterations=100)
pso_efficiencies, pso_qualities = run_pso_multiple_trials(10, pso_params)

pso = PSO.ParticleSwarmOptimisation(**pso_params)
pso_best_values = pso.run()
aco = ACO.AntColonyOptimisation(**aco_params)
best_solution, best_distance, aco_best_values = aco.run(max_iterations=100)

plot_efficiency(aco_efficiencies, pso_efficiencies)
plot_solution_quality(aco_qualities, pso_qualities)
plot_convergence(pso_best_values, aco_best_values) # pso_best_values & aco_best_values are collected during runs

