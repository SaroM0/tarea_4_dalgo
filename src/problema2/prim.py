import sys

def prim(adj_matrix):
    """
    Ejecuta el algoritmo de Prim en un grafo no dirigido representado por su matriz de adyacencias.
    
    Args:
        adj_matrix: Lista de listas que representa la matriz de adyacencias con pesos.
                   Un valor de 0 indica que no hay arista.
    
    Returns:
        El MST como una lista de aristas en el formato (u, v, peso).
    """
    # Se obtiene el número de vértices
    n = len(adj_matrix)
    
    # Se inicializa un arreglo para marcar los vértices ya seleccionados
    selected = [False] * n
    
    # Se inicializa el arreglo de claves con un valor muy alto (infinito)
    key = [sys.maxsize] * n
    
    # Se inicializa el arreglo de padres para reconstruir el MST
    parent = [-1] * n
    
    # Se establece la clave del primer vértice en 0 para comenzar desde él
    key[0] = 0
    
    # Se inicializa la lista que contendrá las aristas del MST
    mst = []
    
    # Se seleccionan n vértices
    for _ in range(n):
        # Se selecciona el vértice u con valor mínimo de clave que aún no ha sido incluido
        min_val = sys.maxsize
        u = -1
        for v in range(n):
            if not selected[v] and key[v] < min_val:
                min_val = key[v]
                u = v
        
        # Si no se encontró un vértice válido (grafo desconectado), se termina el algoritmo
        if u == -1:
            break
            
        # Se marca el vértice como seleccionado
        selected[u] = True
        
        # Se actualizan las claves de los vértices adyacentes
        for v in range(n):
            # Si hay una arista, el vértice no está seleccionado y el peso es menor que la clave actual
            if adj_matrix[u][v] != 0 and not selected[v] and adj_matrix[u][v] < key[v]:
                key[v] = adj_matrix[u][v]
                parent[v] = u
    
    # Se reconstruye el MST a partir del arreglo de padres
    for v in range(1, n):
        if parent[v] != -1:
            mst.append((parent[v], v, adj_matrix[parent[v]][v]))
    
    return mst

# Ejemplo de uso:
if __name__ == "__main__":
    # Se define una matriz de adyacencias de ejemplo
    adj_matrix = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0]
    ]
    
    # Se ejecuta el algoritmo de Prim
    mst = prim(adj_matrix)
    print("Árbol de expansión mínima (Prim):", mst)
    
    # Se calcula el peso total del MST
    total_weight = sum(weight for _, _, weight in mst)
    print(f"Peso total del MST: {total_weight}") 