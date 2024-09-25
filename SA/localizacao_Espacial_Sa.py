import numpy as np
import random
import math

# Exemplo de matriz de qualidade (10x10)
quality_matrix = np.random.rand(10, 10)

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

        # Limitar o valor máximo do argumento para math.exp
        delta_cost = current_cost - new_cost
        if new_cost > current_cost or random.uniform(0, 1) < math.exp(min(delta_cost / temp, 700)):  # 700 é um valor seguro
            current_position = new_position
            current_cost = new_cost

        if current_cost > best_cost:
            best_position = current_position
            best_cost = current_cost

        temp *= cooling_rate

    return best_position, best_cost

# Parâmetros do algoritmo
initial_temp = 1000
cooling_rate = 0.95
iterations = 1000
initial_position = (5, 5)

# Executar o algoritmo
best_position, best_cost = simulated_annealing(initial_temp, cooling_rate, iterations, initial_position)

# Mostrar os resultados
print("Melhor posição:", best_position)
print("Melhor custo (qualidade):", -best_cost)  # Negativo para mostrar a qualidade real
