import cma
import numpy as np

# Simulação dos dados do sensor
sensor_data = np.random.random(100)

# Função de custo para ajustar os dados
def cost_function(params):
    threshold, scaling_factor = params
    processed_data = sensor_data * scaling_factor
    return np.sum(np.abs(processed_data - threshold))  # Minimizar a diferença

# Executa o CMA-ES
es = cma.CMAEvolutionStrategy([0.5, 1.0], 0.2) 
