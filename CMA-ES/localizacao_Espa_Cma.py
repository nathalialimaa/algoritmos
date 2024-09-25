import cma
import numpy as np

# Simulação de uma matriz de qualidade de sinal
quality_matrix = np.random.random((10, 10))

# Função de custo para otimizar a localização
def cost_function(position):
    x, y = int(position[0]), int(position[1])
    return -quality_matrix[x, y]  # Maximizar a qualidade (negativo para CMA-ES)

# Executa o CMA-ES
es = cma.CMAEvolutionStrategy([5, 5], 0.5)  # Inicializa o algoritmo com ponto médio [5,5] e sigma de 0.5
while not es.stop():
    solutions = es.ask()
    es.tell(solutions, [cost_function(x) for x in solutions])
    es.logger.add()

best_solution = es.result.xbest
print(f'Melhor posição para o sensor: {best_solution}')
