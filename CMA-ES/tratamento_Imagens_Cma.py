import cma
import numpy as np

# Simulação de uma imagem como uma matriz 10x10 com valores entre 0 e 1
image = np.random.random((10, 10))

# Função de custo: otimizar o threshold de segmentação de imagem
def cost_function(threshold):
    # Aplica o threshold para criar uma imagem binária
    binary_image = image > threshold
    # Queremos que a média da imagem binária seja próxima de 0.5 (água e solo equilibrados)
    reference_value = 0.5
    return np.abs(binary_image.mean() - reference_value)  # Minimizar a diferença em relação ao valor de referência

# Executa o CMA-ES para otimização do threshold
es = cma.CMAEvolutionStrategy([0.5], 0.2)  # Inicializa o algoritmo com threshold inicial em 0.5 e sigma de 0.2
while not es.stop():
    thresholds = es.ask()  # Gera novos thresholds
    es.tell(thresholds, [cost_function(th) for th in thresholds])  # Avalia cada threshold usando a função de custo
    es.logger.add()

# Melhor solução encontrada
best_threshold = es.result.xbest
print(f'Melhor threshold para segmentação de imagem: {best_threshold}')
