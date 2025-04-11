import random
import os

def generate_random_weighted_graph(n, edge_probability=0.5, min_weight=1, max_weight=100):
    """
    Genera un grafo aleatorio con pesos.
    
    Args:
        n: Número de vértices.
        edge_probability: Probabilidad de que exista una arista entre dos vértices.
        min_weight: Peso mínimo de una arista.
        max_weight: Peso máximo de una arista.
        
    Returns:
        Tupla (lista_adyacencias, matriz_adyacencias)
    """
    # Se inicializa la lista de adyacencias
    adj_list = {i: [] for i in range(n)}
    
    # Se inicializa la matriz de adyacencias con ceros
    adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    # Se generan las aristas aleatorias
    for i in range(n):
        for j in range(i+1, n):  # Solo se consideran pares (i,j) donde i < j
            # Se decide aleatoriamente si existirá una arista entre i y j
            if random.random() < edge_probability:
                # Se genera un peso aleatorio para la arista
                weight = random.randint(min_weight, max_weight)
                
                # Se agrega la arista a la lista de adyacencias (en ambas direcciones para grafo no dirigido)
                adj_list[i].append((j, weight))
                adj_list[j].append((i, weight))
                
                # Se agrega la arista a la matriz de adyacencias (en ambas direcciones para grafo no dirigido)
                adj_matrix[i][j] = weight
                adj_matrix[j][i] = weight
    
    return adj_list, adj_matrix

def generate_connected_graph(n, min_weight=1, max_weight=100):
    """
    Genera un grafo conexo aleatorio.
    
    Args:
        n: Número de vértices.
        min_weight: Peso mínimo de una arista.
        max_weight: Peso máximo de una arista.
        
    Returns:
        Tupla (lista_adyacencias, matriz_adyacencias)
    """
    # Se inicializa la lista de adyacencias
    adj_list = {i: [] for i in range(n)}
    
    # Se inicializa la matriz de adyacencias con ceros
    adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    # Se asegura la conexión generando un árbol aleatorio
    vertices = list(range(n))
    random.shuffle(vertices)
    
    # El primer vértice estará solo inicialmente
    connected = {vertices[0]}
    not_connected = set(vertices[1:])
    
    # Se conecta cada vértice con al menos un vértice ya conectado
    while not_connected:
        v = not_connected.pop()
        u = random.choice(list(connected))
        
        # Se genera un peso aleatorio para la arista
        weight = random.randint(min_weight, max_weight)
        
        # Se agrega la arista a la lista de adyacencias
        adj_list[u].append((v, weight))
        adj_list[v].append((u, weight))
        
        # Se agrega la arista a la matriz de adyacencias
        adj_matrix[u][v] = weight
        adj_matrix[v][u] = weight
        
        connected.add(v)
    
    # Se agregan aristas adicionales aleatoriamente
    edge_probability = random.uniform(0.1, 0.3)  # Probabilidad de agregar aristas adicionales
    
    for i in range(n):
        for j in range(i+1, n):
            # No se consideran las aristas ya existentes
            if adj_matrix[i][j] == 0 and random.random() < edge_probability:
                weight = random.randint(min_weight, max_weight)
                
                adj_list[i].append((j, weight))
                adj_list[j].append((i, weight))
                
                adj_matrix[i][j] = weight
                adj_matrix[j][i] = weight
    
    return adj_list, adj_matrix

def generate_bipartite_graph(n, edge_probability=0.5, min_weight=1, max_weight=100):
    """
    Genera un grafo bipartito aleatorio.
    
    Args:
        n: Número de vértices.
        edge_probability: Probabilidad de que exista una arista entre dos vértices de diferentes conjuntos.
        min_weight: Peso mínimo de una arista.
        max_weight: Peso máximo de una arista.
        
    Returns:
        Tupla (lista_adyacencias, particiones)
    """
    # Se dividen los vértices en dos conjuntos
    part_a = set(range(0, n // 2))
    part_b = set(range(n // 2, n))
    
    # Se inicializa la lista de adyacencias
    adj_list = {i: [] for i in range(n)}
    
    # Se generan aristas solo entre vértices de diferentes conjuntos
    for i in part_a:
        for j in part_b:
            if random.random() < edge_probability:
                # Para grafos no ponderados en el problema de bipartición
                adj_list[i].append(j)
                adj_list[j].append(i)
    
    return adj_list, (part_a, part_b)

def generate_non_bipartite_graph(n, edge_probability=0.5):
    """
    Genera un grafo que definitivamente no es bipartito.
    
    Args:
        n: Número de vértices (debe ser al menos 3).
        edge_probability: Probabilidad de aristas adicionales.
        
    Returns:
        Lista de adyacencias del grafo.
    """
    if n < 3:
        raise ValueError("El número de vértices debe ser al menos 3 para un grafo no bipartito")
    
    # Se inicializa la lista de adyacencias
    adj_list = {i: [] for i in range(n)}
    
    # Se agrega un ciclo impar (triángulo) al grafo
    for i in range(3):
        adj_list[i].append((i + 1) % 3)
        adj_list[(i + 1) % 3].append(i)
    
    # Se agregan aristas adicionales aleatoriamente
    for i in range(n):
        for j in range(i + 1, n):
            if j not in adj_list[i] and random.random() < edge_probability:
                adj_list[i].append(j)
                adj_list[j].append(i)
    
    return adj_list

def save_test_cases(test_dir, n_cases=100):
    """
    Genera y guarda casos de prueba para los algoritmos implementados.
    
    Args:
        test_dir: Directorio donde se guardarán los casos de prueba.
        n_cases: Número de casos a generar.
    """
    # Se crean directorios si no existen
    os.makedirs(os.path.join(test_dir, "problema2"), exist_ok=True)
    os.makedirs(os.path.join(test_dir, "problema3"), exist_ok=True)
    
    # Se generan casos para Kruskal
    kruskal_dir = os.path.join(test_dir, "problema2", "kruskal")
    os.makedirs(kruskal_dir, exist_ok=True)
    
    # Se generan casos para Prim
    prim_dir = os.path.join(test_dir, "problema2", "prim")
    os.makedirs(prim_dir, exist_ok=True)
    
    # Se generan casos para verificación de grafo bipartito
    bipartite_dir = os.path.join(test_dir, "problema3", "bipartite")
    os.makedirs(bipartite_dir, exist_ok=True)
    
    # Se generan casos de diferentes tamaños
    sizes = [10, 20, 50, 100, 200, 500, 1000]
    
    for i in range(n_cases):
        # Se selecciona un tamaño aleatorio
        n = random.choice(sizes)
        
        # Se generan grafos aleatorios
        adj_list, adj_matrix = generate_random_weighted_graph(n, edge_probability=0.3)
        
        # Se guarda caso para Kruskal (lista de adyacencias)
        with open(os.path.join(kruskal_dir, f"case_{i+1}.txt"), "w") as f:
            f.write(f"{n}\n")
            for v in range(n):
                edges = []
                for neighbor, weight in adj_list.get(v, []):
                    edges.append(f"{neighbor}-{weight}")
                f.write(f"{v}: {', '.join(edges)}\n")
        
        # Se guarda caso para Prim (matriz de adyacencias)
        with open(os.path.join(prim_dir, f"case_{i+1}.txt"), "w") as f:
            f.write(f"{n}\n")
            for row in adj_matrix:
                f.write(" ".join(map(str, row)) + "\n")
        
        # Se decide aleatoriamente si generar un grafo bipartito o no
        is_bipartite = random.choice([True, False])
        
        if is_bipartite:
            bipartite_adj_list, partitions = generate_bipartite_graph(n, edge_probability=0.3)
        else:
            bipartite_adj_list = generate_non_bipartite_graph(n, edge_probability=0.2)
            partitions = None
        
        # Se guarda caso para verificación de grafo bipartito
        with open(os.path.join(bipartite_dir, f"case_{i+1}.txt"), "w") as f:
            f.write(f"{n}\n")
            for v in range(n):
                neighbors = bipartite_adj_list.get(v, [])
                f.write(" ".join(map(str, neighbors)) + "\n")
            
            # Se escribe si el grafo es bipartito o no (para verificación)
            f.write(f"IS_BIPARTITE: {is_bipartite}\n")
            if is_bipartite:
                f.write(f"PARTITION_A: {sorted(list(partitions[0]))}\n")
                f.write(f"PARTITION_B: {sorted(list(partitions[1]))}\n")

if __name__ == "__main__":
    # Ejemplo de uso
    save_test_cases("tests", n_cases=10)
    print("Se han generado 10 casos de prueba para cada problema.") 