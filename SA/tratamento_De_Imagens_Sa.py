import numpy as np
import random
import math

# Simulação de uma imagem como uma matriz 10x10 com valores entre 0 e 1
image = np.random.random((10, 10))

# Função de custo: otimizar o threshold de segmentação de imagem
def cost_function(threshold):
    # Cria uma imagem binária usando o threshold
    binary_image = image > threshold
    # Queremos que a média da imagem binária seja próxima de um valor de referência (0.5)
    reference_value = 0.5
    return np.abs(binary_image.mean() - reference_value)

# Função de simulated annealing para otimização de threshold de imagem
def simulated_annealing_image(initial_temp, cooling_rate, iterations, initial_threshold):
    current_threshold = initial_threshold
    current_cost = cost_function(current_threshold)
    temp = initial_temp
    best_threshold = current_threshold
    best_cost = current_cost

    for _ in range(iterations):
        # Gera um novo threshold ajustando um pequeno valor
        new_threshold = current_threshold + random.uniform(-0.1, 0.1)
        new_threshold = max(0.1, min(new_threshold, 0.9))  # Garante que o threshold fique entre 0.1 e 0.9
        new_cost = cost_function(new_threshold)

        # Aceita nova solução com base na probabilidade do simulated annealing
        if new_cost < current_cost or random.uniform(0, 1) < math.exp((current_cost - new_cost) / temp):
            current_threshold = new_threshold
            current_cost = new_cost

        # Atualiza a melhor solução encontrada
        if current_cost < best_cost:
            best_threshold = current_threshold
            best_cost = current_cost

        # Resfria a temperatura
        temp *= cooling_rate

    return best_threshold

# Threshold inicial
initial_threshold = 0.5

# Executa o simulated annealing
best_threshold = simulated_annealing_image(1000, 0.95, 1000, initial_threshold)
print(f'Melhor threshold para segmentação: {best_threshold}')
