class UnionFind:
    """Estructura de datos Union-Find con compresión de caminos y unión por rango."""
    def __init__(self, n):
        # Se inicializa cada vértice como su propio padre
        self.parent = [i for i in range(n)]
        # Se inicializa el rango de cada conjunto en 0
        self.rank = [0] * n

    def find(self, i):
        # Se busca la raíz de i con compresión de caminos
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        # Se unen dos conjuntos utilizando la técnica de unión por rango
        root_i = self.find(i)
        root_j = self.find(j)
        
        # Si ya están en el mismo conjunto, no se realiza ninguna acción
        if root_i == root_j:
            return False
        
        # Se une el árbol de menor rango al de mayor rango
        if self.rank[root_i] < self.rank[root_j]:
            self.parent[root_i] = root_j
        else:
            self.parent[root_j] = root_i
            # Si ambos árboles tienen el mismo rango, se incrementa el rango del resultado
            if self.rank[root_i] == self.rank[root_j]:
                self.rank[root_i] += 1
        return True

def kruskal(graph, n):
    """
    Ejecuta el algoritmo de Kruskal en un grafo no dirigido.
    
    Args:
        graph: Diccionario que representa el grafo en formato de lista de adyacencias.
               Formato: {vertice: [(vecino, peso), ...], ...}
        n: Número de vértices.
        
    Returns:
        Una lista de aristas en el MST en el formato (u, v, peso).
    """
    # Se extraen las aristas del grafo, evitando duplicados
    edges = []
    for u in graph:
        for v, weight in graph[u]:
            # Solo se agrega una vez cada arista para grafos no dirigidos
            if u < v:
                edges.append((u, v, weight))
    
    # Se ordenan las aristas por peso en orden creciente
    edges.sort(key=lambda edge: edge[2])
    
    # Se inicializa la estructura Union-Find
    uf = UnionFind(n)
    
    # Se inicializa la lista que contendrá las aristas del MST
    mst = []
    
    # Se procesan las aristas en orden de peso creciente
    for u, v, weight in edges:
        # Si al unir los vértices no se forma un ciclo, se agrega la arista al MST
        if uf.union(u, v):
            mst.append((u, v, weight))
            
            # Si ya se tienen n-1 aristas, se ha completado el MST
            if len(mst) == n - 1:
                break
                
    return mst

# Ejemplo de uso:
if __name__ == "__main__":
    # Se define un grafo de ejemplo
    graph = {
        0: [(1, 4), (2, 3)],
        1: [(0, 4), (2, 1), (3, 2)],
        2: [(0, 3), (1, 1), (3, 4)],
        3: [(1, 2), (2, 4)]
    }
    n = 4
    
    # Se ejecuta el algoritmo de Kruskal
    mst_edges = kruskal(graph, n)
    print("Árbol de expansión mínima (Kruskal):", mst_edges)
    
    # Se calcula el peso total del MST
    total_weight = sum(weight for _, _, weight in mst_edges)
    print(f"Peso total del MST: {total_weight}") 