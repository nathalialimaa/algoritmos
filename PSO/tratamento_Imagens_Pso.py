import numpy as np
from skimage import filters
from pyswarm import pso

# Simulação de uma imagem (10x10 matriz com valores entre 0 e 1)
image = np.random.random((10, 10))

# Função de custo: aplicar threshold e comparar com um valor de referência
def cost_function(params):
    threshold = params[0]
    binary_image = image > threshold
    reference_value = 0.5  # Exemplo de valor esperado para separar água e solo
    return np.sum(np.abs(binary_image.mean() - reference_value))  # Minimizar diferença

# Limites para o threshold
lb = [0.1]
ub = [0.9]

# Executa o PSO
best_threshold, _ = pso(cost_function, lb, ub, swarmsize=20, maxiter=100)
print(f'Melhor threshold para segmentação: {best_threshold}')
