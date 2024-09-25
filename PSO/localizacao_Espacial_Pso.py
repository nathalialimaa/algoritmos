import numpy as np
from pyswarm import pso

# Simulação de uma matriz de qualidade de sinal para cada posição (quanto maior, melhor o sinal)
quality_matrix = np.random.random((10, 10))  # Exemplo: 10x10 grade de possíveis locais

# Função de custo: buscamos a posição com o melhor sinal (maior valor)
def cost_function(params):
    x, y = int(params[0]), int(params[1])
    return -quality_matrix[x, y]  # Queremos maximizar o valor, então usamos o negativo

# Limites da área de busca (10x10 matriz)
lb = [0, 0]
ub = [9, 9]

# Executa o PSO
best_position, _ = pso(cost_function, lb, ub, swarmsize=20, maxiter=100)
print(f'Melhor posição encontrada para o sensor: {best_position}')
