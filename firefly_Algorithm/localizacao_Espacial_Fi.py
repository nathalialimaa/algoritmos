import numpy as np
import random

# Simulação de uma matriz de qualidade de sinal para posicionamento do sensor
quality_matrix = np.random.random((10, 10))

# Função de custo para calcular a intensidade da solução (qualidade do sinal)
def cost_function(position):
    x, y = int(position[0]), int(position[1])
    return quality_matrix[x, y]

# Função de atração entre vaga-lumes
def firefly_algorithm(quality_matrix, num_fireflies, iterations, alpha=0.2, beta=1, gamma=1):
    fireflies = np.random.rand(num_fireflies, 2) * 9  # Inicia vaga-lumes em posições aleatórias
    best_solution = fireflies[0]
    best_cost = cost_function(best_solution)

    for _ in range(iterations):
        for i in range(num_fireflies):
            for j in range(num_fireflies):
                if cost_function(fireflies[j]) > cost_function(fireflies[i]):
                    r = np.linalg.norm(fireflies[i] - fireflies[j])  # Distância entre vaga-lumes
                    beta_attraction = beta * np.exp(-gamma * r ** 2)  # Atração entre vaga-lumes
                    fireflies[i] = fireflies[i] + beta_attraction * (fireflies[j] - fireflies[i]) + alpha * (np.random.rand(2) - 0.5)

                    # Atualiza a melhor solução
                    current_cost = cost_function(fireflies[i])
                    if current_cost > best_cost:
                        best_solution = fireflies[i]
                        best_cost = current_cost

    return best_solution, best_cost

# Executa o algoritmo
best_position, best_cost = firefly_algorithm(quality_matrix, num_fireflies=20, iterations=100)
print(f'Melhor posição para o sensor: {best_position}, Qualidade do sinal: {best_cost}')
