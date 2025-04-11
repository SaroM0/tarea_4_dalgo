from collections import deque

def is_bipartite(graph, n):
    """
    Determina si un grafo dado (en forma de lista de adyacencias) es bipartito.
    
    Args:
        graph: Diccionario que representa el grafo en formato de lista de adyacencias.
               Formato: {vertice: [vecino1, vecino2, ...], ...}
        n: Número de vértices.
        
    Returns:
        Tupla (es_bipartito: bool, particiones: (set, set) o None)
        Si el grafo es bipartito, retorna los dos conjuntos disjuntos de vértices.
    """
    # Se inicializa un diccionario para almacenar el color asignado a cada vértice
    colors = {}
    
    # Se inicializan las particiones como conjuntos vacíos
    partitions = (set(), set())
    
    # Se procesa cada componente (en caso de que el grafo no sea conexo)
    for start in range(n):
        if start not in colors:
            # Se asigna el color 0 al vértice inicial
            colors[start] = 0
            partitions[0].add(start)
            
            # Se inicializa una cola para el recorrido BFS
            queue = deque([start])
            
            # Se realiza un recorrido BFS
            while queue:
                u = queue.popleft()
                
                # Se visitan todos los vecinos del vértice actual
                for v in graph.get(u, []):
                    if v not in colors:
                        # Se asigna el color opuesto al vecino no visitado
                        colors[v] = 1 - colors[u]
                        partitions[colors[v]].add(v)
                        queue.append(v)
                    elif colors[v] == colors[u]:
                        # Se encontró un conflicto: el grafo no es bipartito
                        return (False, None)
    
    # Si no se encontraron conflictos, el grafo es bipartito
    return (True, partitions)

def print_bipartite_result(result, partitions):
    """
    Imprime el resultado de la verificación de bipartición.
    
    Args:
        result: Boolean indicando si el grafo es bipartito.
        partitions: Tupla con los dos conjuntos de vértices si el grafo es bipartito.
    """
    if result:
        print("El grafo ES bipartito.")
        print(f"Conjunto A: {sorted(list(partitions[0]))}")
        print(f"Conjunto B: {sorted(list(partitions[1]))}")
    else:
        print("El grafo NO es bipartito.")

# Ejemplo de uso:
if __name__ == "__main__":
    # Ejemplo de grafo bipartito (ciclo par)
    bipartite_graph = {
        0: [1, 3],
        1: [0, 2],
        2: [1, 3],
        3: [0, 2]
    }
    
    # Ejemplo de grafo no bipartito (ciclo impar)
    non_bipartite_graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1]
    }
    
    print("Ejemplo 1 (ciclo par):")
    result, parts = is_bipartite(bipartite_graph, 4)
    print_bipartite_result(result, parts)
    
    print("\nEjemplo 2 (ciclo impar):")
    result, parts = is_bipartite(non_bipartite_graph, 3)
    print_bipartite_result(result, parts) 