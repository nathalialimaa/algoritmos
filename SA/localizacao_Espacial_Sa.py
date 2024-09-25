import numpy as np
import random
import math

# Função de custo para o posicionamento do sensor
def cost_function(position):
    x, y = position
    return -quality_matrix[x, y]  # Negativo para maximizar a qualidade

# Simulated Annealing para otimização de localização
def simulated_annealing(initial_temp, cooling_rate, iterations, initial_position):
    current_position = initial_position
    current_cost = cost_function(current_position)
    temp = initial_temp
    best_position = current_position
    best_cost = current_cost

    for _ in range(iterations):
        new_position = (current_position[0] + random.randint(-1, 1), current_position[1] + random.randint(-1, 1))
        new_position = (max(0, min(new_position[0], 9)), max(0, min(new_position[1], 9)))
        new_cost = cost_function(new_position)

        if new_cost > current_cost or random.uniform(0, 1) < math.exp((current_cost - new_cost) / temp):
            current_position = new_position
            current_cost = new_cost

        if current_cost > best_cost:
            best_position = current_position
            best_cost = current_cost

        temp *= cooling_rate

