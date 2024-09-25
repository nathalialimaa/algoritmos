import numpy as np
import random

# Simulação dos dados do sensor
sensor_data = np.random.random(100)

# Função de custo para ajustar os dados dos sensores
def cost_function(params):
    threshold, scaling_factor = params
    processed_data = sensor_data * scaling_factor
    return np.sum(np.abs(processed_data - threshold))

# Função de otimização usando Firefly Algorithm
def firefly_algorithm_data(num_fireflies, iterations, alpha=0.2, beta=1, gamma=1):
    fireflies = np.random.rand(num_fireflies, 2)  # Inicializa vaga-lumes com parâmetros aleatórios (threshold, scaling factor)
    best_solution = fireflies[0]
    best_cost = cost_function(best_solution)

    for _ in range(iterations):
        for i in range(num_fireflies):
            for j in range(num_fireflies):
                if cost_function(fireflies[j]) < cost_function(fireflies[i]):  # Minimizar a função de custo
                    r = np.linalg.norm(fireflies[i] - fireflies[j])
                    beta_attraction = beta * np.exp(-gamma * r ** 2)
                    fireflies[i] = fireflies[i] + beta_attraction * (fireflies[j] - fireflies[i]) + alpha * (np.random.rand(2) - 0.5)

                    current_cost = cost_function(fireflies[i])
                    if current_cost < best_cost:
                        best_solution = fireflies[i]
                        best_cost = current_cost

    return best_solution

# Executa o algoritmo
best_params = firefly_algorithm_data(num_fireflies=20, iterations=100)
print(f'Melhores parâmetros de ajuste: Threshold: {best_params[0]}, Fator de Escala: {best_params[1]}')
