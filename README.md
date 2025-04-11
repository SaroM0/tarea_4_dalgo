# Tarea 4 - Grafos

Implementación de algoritmos de grafos como parte de la Tarea 4 del curso de Diseño y Análisis de Algoritmos.

## Autor

Santiago Rodriguez Mora - 202110332

## Estructura del proyecto

```
tarea_4/
│
├── src/
│   ├── problema2/
│   │   ├── kruskal.py     # Implementación de Kruskal con lista de adyacencias
│   │   └── prim.py        # Implementación de Prim con matriz de adyacencias
│   │
│   ├── problema3/
│   │   └── bipartite.py   # Verificación de grafo bipartito
│   │
│   ├── utils/
│   │   └── test_generator.py  # Generador de casos de prueba
│   │
│   └── main.py            # Programa principal
│
└── tests/                 # Casos de prueba generados
    ├── problema2/
    │   ├── kruskal/       # Casos de prueba para Kruskal
    │   └── prim/          # Casos de prueba para Prim
    │
    └── problema3/
        └── bipartite/     # Casos de prueba para verificación de bipartición
```

## Requisitos

- Python 3.6 o superior

## Uso

### Generar casos de prueba

Para generar 100 casos de prueba (valor por defecto):

```bash
python src/main.py 4
```

Para generar un número específico de casos:

```bash
python src/main.py 4 <numero_casos>
```

### Ejecutar algoritmo de Kruskal

```bash
python src/main.py 1 <archivo_prueba>
```

Por ejemplo:

```bash
python src/main.py 1 tests/problema2/kruskal/case_1.txt
```

### Ejecutar algoritmo de Prim

```bash
python src/main.py 2 <archivo_prueba>
```

Por ejemplo:

```bash
python src/main.py 2 tests/problema2/prim/case_1.txt
```

### Verificar si un grafo es bipartito

```bash
python src/main.py 3 <archivo_prueba>
```

Por ejemplo:

```bash
python src/main.py 3 tests/problema3/bipartite/case_1.txt
```

## Formato de los archivos de entrada

### Para Kruskal (Lista de adyacencias)

```
n
0: 1-4, 2-3
1: 0-4, 2-1, 3-2
...
```

Donde:

- `n` es el número de vértices
- Cada línea siguiente representa las aristas del vértice en formato "vecino-peso"

### Para Prim (Matriz de adyacencias)

```
n
0 4 3 0
4 0 1 2
3 1 0 4
0 2 4 0
```

Donde:

- `n` es el número de vértices
- Las siguientes `n` líneas representan la matriz de adyacencias

### Para verificación de grafo bipartito

```
n
1 3
0 2
1 3
0 2
```

Donde:

- `n` es el número de vértices
- Cada línea siguiente contiene los vecinos del vértice correspondiente

## Análisis de complejidad

### Kruskal

- Ordenamiento de aristas: O(m log m)
- Procesamiento de aristas con Union-Find: O(m α(n))
- Complejidad total: O(m log m)

### Prim

- Selección de vértice mínimo en cada iteración: O(n)
- Iteraciones: O(n)
- Complejidad total: O(n²)

### Verificación de grafo bipartito

- Recorrido BFS: O(n + m)
- Complejidad total: O(n + m)
