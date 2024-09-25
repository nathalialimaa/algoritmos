import numpy as np

# Simulação de uma matriz de custos (onde sensores podem ser posicionados)
# Matriz representa a qualidade da cobertura em diferentes locais (valores mais altos são melhores)
cost_matrix = np.random.random((10, 10))  # Exemplo: 10x10 grade de possíveis locais

# Função para atualizar feromônio (diminui ao longo do tempo - evaporação)
def update_pheromone(pheromone_map, position, decay=0.1):
    pheromone_map[position] += 1
    pheromone_map *= (1 - decay)

# Função ACO para otimizar o posicionamento do sensor
def ant_colony_optimization(cost_matrix, num_ants, iterations):
    pheromone_map = np.zeros_like(cost_matrix)
    best_position = None
    best_cost = float('-inf')

    for _ in range(iterations):
        for _ in range(num_ants):
            # Simulação de formigas escolhendo um caminho (aleatório neste exemplo)
            position = (np.random.randint(0, cost_matrix.shape[0]), np.random.randint(0, cost_matrix.shape[1]))
            cost = cost_matrix[position]
            
            # Atualiza o melhor caminho encontrado
            if cost > best_cost:
                best_cost = cost
                best_position = position
            
            # Atualiza o feromônio
            update_pheromone(pheromone_map, position)
    
    return best_position, best_cost

# Executa o ACO para encontrar o melhor local para o sensor
best_position, best_cost = ant_colony_optimization(cost_matrix, num_ants=10, iterations=100)
print(f"Melhor posição para o sensor: {best_position}, Custo: {best_cost}")
