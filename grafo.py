from collections import deque, defaultdict
import heapq

class Grafo:
    def __init__(self):
        """Inicializa um grafo vazio.
           Cada vértice é uma chave do dicionário 'grafo' e seu valor
           é outro dicionário que representa as arestas e seus respectivos pesos."""
        self.grafo = defaultdict(dict)

    def adicionar_arco(self, origem, destino, peso):
        """Adiciona uma aresta ao grafo.
           A aresta é representada como uma entrada no dicionário do vértice de origem,
           onde a chave é o vértice de destino e o valor é o peso."""
        self.grafo[origem][destino] = int(peso)

    def ler_arquivo(self, nome_arquivo):
        # Lê um arquivo de texto que contém os arcos do grafo e os adiciona ao grafo.
        try:
            with open(nome_arquivo, 'r') as arquivo:
                for _ in range(6):
                    next(arquivo)
                for linha in arquivo:
                    dados = linha.split()
                    if len(dados) >= 4 and dados[0] == 'a':
                        self.adicionar_arco(dados[1], dados[2], int(dados[3]))
            return True
        except Exception as e:
            print(f"Ocorreu um erro ao ler o arquivo: {e}")
            return False

    def obter_grafo(self):
        # Retorna o grafo como um dicionário padrão (não defaultdict).
        return dict(self.grafo)

    def num_vertices(self):
        # Retorna o número de vértices no grafo.
        return len(self.grafo)

    def num_arestas(self):
        # Retorna o número total de arestas no grafo.
        return sum(len(v) for v in self.grafo.values())

    def vizinhanca(self, v):
        # Retorna uma lista de todos os vértices adjacentes ao vértice v.
        return list(self.grafo[v].keys()) if v in self.grafo else []

    def grau_vertice(self, v):
        # Retorna o grau do vértice v, que é o número de arestas que incidem sobre ele.
        return len(self.grafo[v]) if v in self.grafo else 0

    def peso_aresta(self, uv):
        # Retorna o peso da aresta uv.
        u, v = uv
        return self.grafo[u][v] if u in self.grafo and v in self.grafo[u] else None

    def menor_grau(self):
        # Retorna o menor grau entre todos os vértices do grafo.
        return min(len(v) for v in self.grafo.values()) if self.grafo else None

    def maior_grau(self):
        # Retorna o maior grau entre todos os vértices do grafo.
        return max(len(v) for v in self.grafo.values()) if self.grafo else None

    def bfs(self, v):
        visitado = {x: False for x in self.grafo}
        distancia = {x: float('inf') for x in self.grafo}
        predecessor = {x: None for x in self.grafo}

        fila = deque()
        fila.append(v)
        visitado[v] = True
        distancia[v] = 0

        while fila:
            vertice = fila.popleft()
            for vizinho in self.grafo[vertice]:
                if not visitado[vizinho]:
                    fila.append(vizinho)
                    visitado[vizinho] = True
                    distancia[vizinho] = distancia[vertice] + 1
                    predecessor[vizinho] = vertice

        # Filtrar os resultados infinito e None
        distancia = {k: v for k, v in distancia.items() if v != float('inf')}
        predecessor = {k: v for k, v in predecessor.items() if v is not None}

        return distancia, predecessor

    def dfs(self, v):
        visitado = {x: False for x in self.grafo}
        predecessor = {x: None for x in self.grafo}
        tempo_inicio = {x: None for x in self.grafo}
        tempo_fim = {x: None for x in self.grafo}

        tempo = [0]  # Usamos uma lista para que o valor seja passado por referência

        def dfs_visit(vertice):
            visitado[vertice] = True
            tempo[0] += 1
            tempo_inicio[vertice] = tempo[0]

            for vizinho in self.grafo[vertice]:
                if not visitado[vizinho]:
                    predecessor[vizinho] = vertice
                    dfs_visit(vizinho)

            tempo[0] += 1
            tempo_fim[vertice] = tempo[0]

        dfs_visit(v)

        # Filtrar os resultados None
        predecessor = {k: v for k, v in predecessor.items() if v is not None}
        tempo_inicio = {k: v for k, v in tempo_inicio.items() if v is not None}
        tempo_fim = {k: v for k, v in tempo_fim.items() if v is not None}

        return predecessor, tempo_inicio, tempo_fim

    def bellman_ford(self, v):
        distancia = {x: float('inf') for x in self.grafo}
        predecessor = {x: None for x in self.grafo}

        distancia[v] = 0

        for _ in range(len(self.grafo) - 1):
            for vertice in self.grafo:
                for vizinho, peso in self.grafo[vertice].items():
                    if distancia[vertice] + peso < distancia[vizinho]:
                        distancia[vizinho] = distancia[vertice] + peso
                        predecessor[vizinho] = vertice

        for vertice in self.grafo:
            for vizinho, peso in self.grafo[vertice].items():
                if distancia[vertice] + peso < distancia[vizinho]:
                    print("O grafo contém um ciclo de peso negativo")
                    return None, None

        # Filtrar os resultados infinito e None
        distancia = {k: v for k, v in distancia.items() if v != float('inf')}
        predecessor = {k: v for k, v in predecessor.items() if v is not None}

        return distancia, predecessor

    def dijkstra(self, v):
        distancia = {x: float('inf') for x in self.grafo}
        predecessor = {x: None for x in self.grafo}

        distancia[v] = 0
        fila_prioridade = [(0, v)]

        while fila_prioridade:
            dist, vertice = heapq.heappop(fila_prioridade)
            if dist != distancia[vertice]:
                continue
            for vizinho, peso in self.grafo[vertice].items():
                distancia_alternativa = distancia[vertice] + peso
                if distancia_alternativa < distancia[vizinho]:
                    distancia[vizinho] = distancia_alternativa
                    predecessor[vizinho] = vertice
                    heapq.heappush(fila_prioridade, (distancia_alternativa, vizinho))

        # Filtrar os resultados infinito e None
        distancia = {k: v for k, v in distancia.items() if v != float('inf')}
        predecessor = {k: v for k, v in predecessor.items() if v is not None}

        return distancia, predecessor