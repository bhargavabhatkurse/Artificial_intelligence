import random
import math

# Function to calculate the total distance of a tour
def calculate_distance(tour, distance_matrix):
    total_distance = 0
    n = len(tour)
    for i in range(n):
        j = (i + 1) % n
        total_distance += distance_matrix[tour[i]][tour[j]]
    return total_distance

# Function to generate a random initial tour
def generate_initial_tour(n):
    tour = list(range(0,n))
    random.shuffle(tour)
    return tour

# Function to generate a random neighbor by swapping two cities in the tour
def generate_neighbor(tour):
    n = len(tour)
    i = random.randint(0, n-1)
    j = random.randint(0, n-1)
    tour[i], tour[j] = tour[j], tour[i] #swapping two cities
    return tour

# Function to perform Simulated Annealing for TSP
def simulated_annealing(distance_matrix, initial_temperature, final_temperature, alpha):
    n = len(distance_matrix)
   
    current_temperature = initial_temperature
    current_tour = generate_initial_tour(n)

    best_tour = list(current_tour)
    current_distance = calculate_distance(current_tour, distance_matrix)
    best_distance = current_distance

    while current_temperature > final_temperature:
        neighbor_tour = generate_neighbor(current_tour)
        neighbor_distance = calculate_distance(neighbor_tour, distance_matrix)

        cost = current_distance - neighbor_distance
        # Check if the neighbor tour is better or accept it with a probability
        if cost>0 or random.uniform(0, 1) < math.exp((cost) / current_temperature):
            current_tour = list(neighbor_tour)
            current_distance = neighbor_distance

        # Update the best tour if the current tour is better
        if neighbor_distance < best_distance:
            best_tour = list(current_tour)
            best_distance = neighbor_distance

        # Decrease the temperature
        current_temperature *= alpha

    return best_tour, best_distance


def generate_distance_matrix(n):
    distance_matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(0)  # Distance from a city to itself is 0
            else:
                row.append(random.randint(1, 100))  # Generate random distances between 1 and 100
        distance_matrix.append(row)
    return distance_matrix

cities = 30
distance_matrix = generate_distance_matrix(cities)
for row in distance_matrix:
    print(row)


initial_temperature = 1000
final_temperature = 0.1
alpha = 0.99

best_tour, best_distance = simulated_annealing(distance_matrix, initial_temperature, final_temperature, alpha)
print("\nBest tour:", best_tour)
print("Best distance:", best_distance)
