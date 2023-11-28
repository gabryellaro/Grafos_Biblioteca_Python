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
        # Lê um arquivo de texto que contém os arcos do digrafo e os adiciona ao grafo.
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
        """Realiza uma busca em largura (Breadth-First Search - BFS) a partir do vértice v.
        Retorna dois dicionários: 'distancia', que contém a distância de v a cada vértice,
        e 'predecessor', que contém o predecessor de cada vértice na árvore de busca."""
        visitado = {x: False for x in self.grafo}
        distancia = {x: float('inf') for x in self.grafo}
        predecessor = {x: None for x in self.grafo}

        fila = deque([v])
        visitado[v] = True
        distancia[v] = 0

        while fila:
            u = fila.popleft()
            for vizinho in self.grafo[u]:
                if not visitado[vizinho]:
                    fila.append(vizinho)
                    visitado[vizinho] = True
                    distancia[vizinho] = distancia[u] + 1
                    predecessor[vizinho] = u

        return distancia, predecessor

    def dfs_visita(self, v, visitado, predecessor, tempo_inicio, tempo_fim, tempo):
        """Função auxiliar para a busca em profundidade (Depth-First Search - DFS).
           Visita recursivamente todos os vértices do grafo."""
        visitado[v] = True
        tempo += 1
        tempo_inicio[v] = tempo

        for vizinho in self.grafo[v]:
            if not visitado[vizinho]:
                predecessor[vizinho] = v
                tempo = self.dfs_visita(vizinho, visitado, predecessor, tempo_inicio, tempo_fim, tempo)

        tempo += 1
        tempo_fim[v] = tempo

        return tempo

    def dfs(self, v):
        """Realiza uma busca em profundidade (Depth-First Search - DFS) a partir do vértice v.
        Retorna três dicionários: 'predecessor', que contém o predecessor de cada vértice na árvore de busca,
        e 'tempo_inicio' e 'tempo_fim', que contêm os tempos de início e fim da visita a cada vértice, respectivamente."""
        visitado = {x: False for x in self.grafo}
        predecessor = {x: None for x in self.grafo}
        tempo_inicio = {x: float('inf') for x in self.grafo}
        tempo_fim = {x: float('inf') for x in self.grafo}

        tempo = 0
        for vertice in self.grafo:
            if not visitado[vertice]:
                tempo = self.dfs_visita(vertice, visitado, predecessor, tempo_inicio, tempo_fim, tempo)

        return predecessor, tempo_inicio, tempo_fim

    def bellman_ford(self, v):
        """Implementa o algoritmo de Bellman-Ford a partir do vértice v.
        Retorna dois dicionários: 'distancia', que contém a distância de v a cada vértice,
        e 'predecessor', que contém o predecessor de cada vértice no caminho mínimo."""
        distancia = {x: float('inf') for x in self.grafo}
        predecessor = {x: None for x in self.grafo}
        distancia[v] = 0

        for _ in range(len(self.grafo) - 1):
            for u in self.grafo:
                for vizinho, peso in self.grafo[u].items():
                    if distancia[u] + peso < distancia[vizinho]:
                        distancia[vizinho] = distancia[u] + peso
                        predecessor[vizinho] = u

        return distancia, predecessor

    def djikstra(self, v):
        """Implementa o algoritmo de Djikstra a partir do vértice v.
        Retorna dois dicionários: 'distancia', que contém a distância de v a cada vértice,
        e 'predecessor', que contém o predecessor de cada vértice no caminho mínimo."""
        distancia = {x: float('inf') for x in self.grafo}
        predecessor = {x: None for x in self.grafo}
        distancia[v] = 0

        fila_prioridade = [(0, v)]
        while fila_prioridade:
            dist_u, u = heapq.heappop(fila_prioridade)
            if dist_u != distancia[u]:
                continue
            for vizinho, peso in self.grafo[u].items():
                alternativa = distancia[u] + peso
                if alternativa < distancia[vizinho]:
                    distancia[vizinho] = alternativa
                    predecessor[vizinho] = u
                    heapq.heappush(fila_prioridade, (alternativa, vizinho))

            return distancia, predecessor