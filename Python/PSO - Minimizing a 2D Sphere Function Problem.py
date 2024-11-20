# PSO - Minimising 2D Sphere Function Problem.py

import matplotlib.pyplot as plt # pip install matplotlib
import ParticleSwarmOptimisation as PSO

# PSO parameters
num_particles = 30
inertia = 0.7
cognitive = 1.5
social = 2.0
adaptive_social_influence = 1.0
num_iterations = 100
# Initialise and run PSO
pso = PSO.ParticleSwarmOptimisation(num_particles, inertia, cognitive, social, adaptive_social_influence, num_iterations)
best_values = pso.run()
# Plotting convergence over iterations
plt.plot(best_values, label='Best Value')
plt.title('PSO with Adaptive Social Influence: Convergence Plot')
plt.xlabel('Iteration')
plt.ylabel('Best Value')
plt.legend()
plt.grid(True)
plt.show()
