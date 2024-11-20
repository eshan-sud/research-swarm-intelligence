# ParticleSwarmOptimisation.py

import numpy as np

class Particle:
    def __init__(self, position, velocity, personal_best, inertia, cognitive, social):
        self.position = position
        self.velocity = velocity
        self.personal_best = personal_best
        self.inertia = inertia
        self.cognitive = cognitive
        self.social = social

class ParticleSwarmOptimisation:
    def __init__(self, num_particles, inertia, cognitive, social, adaptive_social_influence, num_iterations):
        self.num_particles = num_particles
        self.inertia = inertia
        self.cognitive = cognitive
        self.social = social
        self.adaptive_social_influence = adaptive_social_influence # Newly Identified Parameter - Adaptive Social Influence
        self.num_iterations = num_iterations
        self.particles = self.initialise_particles()
        self.global_best_position = np.random.uniform(-10, 10, 2)
        self.global_best_value = float('inf')
    def initialise_particles(self):
        particles = []
        for _ in range(self.num_particles):
            position = np.random.uniform(-10, 10, 2)
            velocity = np.random.uniform(-1, 1, 2)
            personal_best = position
            particles.append(Particle(position, velocity, personal_best, self.inertia, self.cognitive, self.social))
        return particles
    def objective_function(self, position):
        return np.sum(position ** 2)  # Sphere function
    def adaptive_social(self, iteration):
        return self.social * (iteration / self.num_iterations) * self.adaptive_social_influence
    def update_particles(self, iteration):
        for particle in self.particles:
            r1, r2 = np.random.rand(2)
            # Adaptive social influence increases over time
            social_influence = self.adaptive_social(iteration)
            inertia_component = particle.inertia * particle.velocity
            cognitive_component = particle.cognitive * r1 * (particle.personal_best - particle.position)
            social_component = social_influence * r2 * (self.global_best_position - particle.position)
            # Update velocity and position
            particle.velocity = inertia_component + cognitive_component + social_component
            particle.position += particle.velocity
            # Update personal best
            if self.objective_function(particle.position) < self.objective_function(particle.personal_best):
                particle.personal_best = particle.position
    def update_global_best(self):
        for particle in self.particles:
            current_value = self.objective_function(particle.position)
            if current_value < self.global_best_value:
                self.global_best_value = current_value
                self.global_best_position = particle.position
    def run(self):
        best_values = []
        for iteration in range(self.num_iterations):
            self.update_particles(iteration)
            self.update_global_best()
            best_values.append(self.global_best_value)
            print(f"Iteration {iteration + 1}, Best Value: {self.global_best_value}")
        return best_values

