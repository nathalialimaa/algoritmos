import numpy as np
from pyswarm import pso

# Simulação de dados capturados pelo sensor
sensor_data = np.random.random(100)

# Função de custo: ajustar o threshold e fator de escala
def cost_function(params):
    threshold, scaling_factor = params
    processed_data = sensor_data * scaling_factor
    return np.sum(np.abs(processed_data - threshold))  # Minimizar a diferença

# Limites dos parâmetros
lb = [0.1, 0.5]
ub = [1.0, 2.0]

# Executa o PSO
best_params, _ = pso(cost_function, lb, ub, swarmsize=20, maxiter=100)
print(f'Melhores parâmetros de ajuste: Threshold: {best_params[0]}, Fator de Escala: {best_params[1]}')
