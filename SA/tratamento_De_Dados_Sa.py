import numpy as np
import random
import math

# Simulação dos dados capturados pelos sensores
sensor_data = np.random.random(100)

# Função de custo: otimizar threshold e fator de escala para tratar os dados do sensor
def cost_function(params):
    threshold, scaling_factor = params
    processed_data = sensor_data * scaling_factor
    # Queremos minimizar a diferença entre os dados processados e um threshold esperado
    return np.sum(np.abs(processed_data - threshold))

# Função de simulated annealing para otimização
def simulated_annealing_data(initial_temp, cooling_rate, iterations, initial_params):
    current_params = initial_params
    current_cost = cost_function(current_params)
    temp = initial_temp
    best_params = current_params
    best_cost = current_cost

    for _ in range(iterations):
        # Gera novos parâmetros ajustando um pequeno valor
        new_params = [current_params[0] + random.uniform(-0.1, 0.1), current_params[1] + random.uniform(-0.1, 0.1)]
        new_params = [max(0.1, min(new_params[0], 1.0)), max(0.5, min(new_params[1], 2.0))]
        new_cost = cost_function(new_params)

        # Aceita nova solução com base na probabilidade do simulated annealing
        if new_cost < current_cost or random.uniform(0, 1) < math.exp((current_cost - new_cost) / temp):
            current_params = new_params
            current_cost = new_cost

        # Atualiza a melhor solução encontrada
        if current_cost < best_cost:
            best_params = current_params
            best_cost = current_cost

        # Resfria a temperatura
        temp *= cooling_rate

    return best_params

# Parâmetros iniciais: threshold e fator de escala
initial_params = [0.5, 1.0]

# Executa o simulated annealing
best_params = simulated_annealing_data(1000, 0.95, 1000, initial_params)
print(f'Melhores parâmetros para o ajuste dos dados: Threshold: {best_params[0]}, Fator de Escala: {best_params[1]}')
