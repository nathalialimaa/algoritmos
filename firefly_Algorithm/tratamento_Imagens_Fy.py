import numpy as np
import random

# Simulação de uma imagem como uma matriz 10x10 com valores entre 0 e 1
image = np.random.random((10, 10))

# Função de custo para segmentação de imagem
def cost_function(threshold):
    binary_image = image > threshold
    reference_value = 0.5  # Valor de referência para a média da imagem binária
    return np.abs(binary_image.mean() - reference_value)

# Função de otimização usando Firefly Algorithm
def firefly_algorithm_image(num_fireflies, iterations, alpha=0.2, beta=1, gamma=1):
    fireflies = np.random.rand(num_fireflies)  # Inicializa vaga-lumes com thresholds aleatórios
    best_solution = fireflies[0]
    best_cost = cost_function(best_solution)

    for _ in range(iterations):
        for i in range(num_fireflies):
            for j in range(num_fireflies):
                if cost_function(fireflies[j]) < cost_function(fireflies[i]):  # Minimizar a função de custo
                    r = np.abs(fireflies[i] - fireflies[j])
                    beta_attraction = beta * np.exp(-gamma * r ** 2)
                    fireflies[i] = fireflies[i] + beta_attraction * (fireflies[j] - fireflies[i]) + alpha * (np.random.rand() - 0.5)

                    current_cost = cost_function(fireflies[i])
                    if current_cost < best_cost:
                        best_solution = fireflies[i]
                        best_cost = current_cost

    return best_solution

# Executa o algoritmo
best_threshold = firefly_algorithm_image(num_fireflies=20, iterations=100)
print(f'Melhor threshold para segmentação de imagem: {best_threshold}')
