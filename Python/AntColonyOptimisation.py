# AntColonyOptimisation.py

import numpy as np

class AntColonyOptimisation:
    def __init__(self, cities, num_ants, alpha, beta, rho, q, dynamic_exploration_rate):
        self.cities = cities
        self.num_ants = num_ants
        self.alpha = alpha  # Pheromone influence
        self.beta = beta  # Heuristic influence (1/distance)
        self.rho = rho  # Evaporation rate
        self.q = q  # Pheromone deposit factor
        self.dynamic_exploration_rate = dynamic_exploration_rate # Newly Identified Parameter - Dynamic Exploration Rate
        self.num_cities = len(cities)
        self.distances = self.calculate_distances(cities)
        self.pheromones = np.ones((self.num_cities, self.num_cities))
    def calculate_distances(self, cities):
        num_cities = len(cities)
        distances = np.zeros((num_cities, num_cities))
        for i in range(num_cities):
            for j in range(i + 1, num_cities):
                distances[i][j] = np.linalg.norm(cities[i] - cities[j])
                distances[j][i] = distances[i][j]
        return distances
    def dynamic_rate(self, iteration, max_iterations):
        return self.dynamic_exploration_rate * (1 - iteration / max_iterations)
    def run(self, max_iterations):
        best_distance = float('inf')
        best_solution = []
        best_distances = []
        for iteration in range(max_iterations):
            dynamic_alpha = self.alpha * self.dynamic_rate(iteration, max_iterations)
            solutions = self.construct_solutions(dynamic_alpha)
            self.update_pheromones(solutions)
            for solution, distance in solutions:
                if distance < best_distance:
                    best_distance = distance
                    best_solution = solution
            best_distances.append(best_distance)
            print(f"Iteration {iteration + 1}, Best Distance: {best_distance}")
        return best_solution, best_distance, best_distances
    def construct_solutions(self, dynamic_alpha):
        solutions = []
        for ant in range(self.num_ants):
            solution = [np.random.randint(self.num_cities)]
            for _ in range(self.num_cities - 1):
                next_city = self.select_next_city(solution, dynamic_alpha)
                solution.append(next_city)
            distance = self.calculate_total_distance(solution)
            solutions.append((solution, distance))
        return solutions
    def select_next_city(self, solution, dynamic_alpha):
        current_city = solution[-1]
        probabilities = []
        for city in range(self.num_cities):
            if city not in solution:
                prob = (self.pheromones[current_city][city] ** dynamic_alpha) * (1 / self.distances[current_city][city]) ** self.beta
                probabilities.append((city, prob))
        total_prob = sum([p for _, p in probabilities])
        if total_prob == 0:
            return np.random.choice([city for city in range(self.num_cities) if city not in solution])
        probabilities = [(city, p / total_prob) for city, p in probabilities]
        next_city = max(probabilities, key=lambda x: x[1])[0]
        return next_city
    def calculate_total_distance(self, solution):
        return sum([self.distances[solution[i]][solution[i + 1]] for i in range(len(solution) - 1)]) + self.distances[solution[-1]][solution[0]]
    def update_pheromones(self, solutions):
        self.pheromones *= (1 - self.rho)
        for solution, distance in solutions:
            pheromone_deposit = self.q / distance
            for i in range(len(solution) - 1):
                self.pheromones[solution[i]][solution[i + 1]] += pheromone_deposit
            self.pheromones[solution[-1]][solution[0]] += pheromone_deposit
