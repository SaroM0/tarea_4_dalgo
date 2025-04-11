import sys
import os
import time

# Se importan los módulos correspondientes a los algoritmos implementados
from src.problema2.kruskal import kruskal
from src.problema2.prim import prim
from src.problema3.bipartite import is_bipartite, print_bipartite_result

def load_graph_adjacency_list(filename):
    """
    Carga un grafo desde un archivo en formato de lista de adyacencias.
    
    Args:
        filename: Ruta al archivo.
    
    Returns:
        Tupla (grafo, número de vértices)
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
        
        n = int(lines[0].strip())
        
        graph = {}
        for i in range(1, n+1):
            if i-1 < len(lines):
                line = lines[i-1].strip()
                if ":" in line:
                    vertex, edges = line.split(":", 1)
                    vertex = int(vertex.strip())
                    graph[vertex] = []
                    
                    if edges.strip():
                        for edge in edges.strip().split(","):
                            edge = edge.strip()
                            if "-" in edge:
                                neighbor, weight = edge.split("-", 1)
                                graph[vertex].append((int(neighbor.strip()), int(weight.strip())))
    
    return graph, n

def load_graph_adjacency_matrix(filename):
    """
    Carga un grafo desde un archivo en formato de matriz de adyacencias.
    
    Args:
        filename: Ruta al archivo.
    
    Returns:
        Tupla (matriz de adyacencias, número de vértices)
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
        
        n = int(lines[0].strip())
        
        matrix = []
        for i in range(1, n+1):
            if i-1 < len(lines):
                row = list(map(int, lines[i].strip().split()))
                matrix.append(row)
    
    return matrix, n

def load_bipartite_graph(filename):
    """
    Carga un grafo para verificación de bipartición desde un archivo.
    
    Args:
        filename: Ruta al archivo.
    
    Returns:
        Tupla (grafo, número de vértices)
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
        
        n = int(lines[0].strip())
        
        graph = {}
        for i in range(1, n+1):
            if i < len(lines):
                neighbors = list(map(int, lines[i].strip().split()))
                graph[i-1] = neighbors
    
    return graph, n

def run_kruskal_test(test_file):
    """
    Ejecuta el algoritmo de Kruskal en un archivo de prueba.
    
    Args:
        test_file: Ruta al archivo de prueba.
    """
    print(f"\nEjecutando Kruskal en {test_file}...")
    
    graph, n = load_graph_adjacency_list(test_file)
    
    start_time = time.time()
    mst = kruskal(graph, n)
    end_time = time.time()
    
    total_weight = sum(weight for _, _, weight in mst)
    
    print(f"MST encontrado con {len(mst)} aristas")
    print(f"Peso total del MST: {total_weight}")
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")

def run_prim_test(test_file):
    """
    Ejecuta el algoritmo de Prim en un archivo de prueba.
    
    Args:
        test_file: Ruta al archivo de prueba.
    """
    print(f"\nEjecutando Prim en {test_file}...")
    
    matrix, n = load_graph_adjacency_matrix(test_file)
    
    start_time = time.time()
    mst = prim(matrix)
    end_time = time.time()
    
    total_weight = sum(weight for _, _, weight in mst)
    
    print(f"MST encontrado con {len(mst)} aristas")
    print(f"Peso total del MST: {total_weight}")
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")

def run_bipartite_test(test_file):
    """
    Ejecuta la verificación de grafo bipartito en un archivo de prueba.
    
    Args:
        test_file: Ruta al archivo de prueba.
    """
    print(f"\nVerificando bipartición en {test_file}...")
    
    graph, n = load_bipartite_graph(test_file)
    
    start_time = time.time()
    result, partitions = is_bipartite(graph, n)
    end_time = time.time()
    
    print_bipartite_result(result, partitions)
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")

def main():
    """
    Función principal que permite ejecutar los algoritmos implementados.
    """
    if len(sys.argv) < 2:
        print("Uso: python main.py <opción> [archivo]")
        print("Opciones:")
        print("  1: Ejecutar Kruskal")
        print("  2: Ejecutar Prim")
        print("  3: Verificar grafo bipartito")
        print("  4: Generar casos de prueba")
        return
    
    option = sys.argv[1]
    
    if option == "1":
        if len(sys.argv) < 3:
            print("Se requiere un archivo para ejecutar Kruskal.")
            return
        run_kruskal_test(sys.argv[2])
    
    elif option == "2":
        if len(sys.argv) < 3:
            print("Se requiere un archivo para ejecutar Prim.")
            return
        run_prim_test(sys.argv[2])
    
    elif option == "3":
        if len(sys.argv) < 3:
            print("Se requiere un archivo para verificar bipartición.")
            return
        run_bipartite_test(sys.argv[2])
    
    elif option == "4":
        from src.utils.test_generator import save_test_cases
        n_cases = 100
        if len(sys.argv) > 2:
            try:
                n_cases = int(sys.argv[2])
            except ValueError:
                print("El número de casos debe ser un entero.")
                return
        
        print(f"Generando {n_cases} casos de prueba...")
        save_test_cases("tests", n_cases)
        print("Casos de prueba generados correctamente.")
    
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main() 