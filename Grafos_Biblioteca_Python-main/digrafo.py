from collections import deque, defaultdict
import heapq

class DidiGrafo:
    def __init__(self):
        """Inicializa um digrafo direcionado vazio,
        o número de arcos como 0 e os graus mínimo e máximo
        como infinito e 0, respectivamente."""
        self.digrafo = {}
        self.m = 0
        self.min_d = float('inf')
        self.max_d = 0

    def adicionar_arco(self, inicio, fim, peso):
        """Adiciona um arco ao digrafo com um peso e uma direção
        (positiva se 'inicio' < 'fim', negativa caso contrário).
        Atualiza o número de arcos e os graus mínimo e máximo."""
        if inicio not in self.digrafo:
            self.digrafo[inicio] = {}
        # Define a direção com base na ordem dos vértices
        direcao = 'positivo' if inicio < fim else 'negativo'
        self.digrafo[inicio][fim] = (int(peso), direcao)
        self.m += 1
        self.min_d = min(self.min_d, len(self.digrafo[inicio]))
        self.max_d = max(self.max_d, len(self.digrafo[inicio]))

    def ler_arquivo(self, nome_arquivo):
        # Lê um arquivo de texto que contém os arcos do digrafo e os adiciona ao grafo.
        with open(nome_arquivo, 'r') as arquivo:
            for _ in range(6):
                next(arquivo)
            for linha in arquivo:
                dados = linha.split()
                if len(dados) >= 4 and dados[0] == 'a':
                    self.adicionar_arco(dados[1], dados[2], int(dados[3]))

    def aresta_positiva(self, inicio, fim):
        # Verifica se o arco de 'inicio' para 'fim' existe e é positivo.
        return inicio in self.digrafo and fim in self.digrafo[inicio] and self.digrafo[inicio][fim][1] == 'a'

    def obter_digrafo(self):
        # Imprime todos os arcos do grafo com seus pesos e direções e retorna o digrafo.
        for inicio in self.digrafo:
            for fim in self.digrafo[inicio]:
                peso, direcao = self.digrafo[inicio][fim]
                print(f"Aresta de {inicio} para {fim} com peso {peso} e direção {direcao}")
        return self.digrafo

    def num_arestas(self):
        # Retorna o número de vértices no digrafo.
        return len(self.digrafo)

    def num_vertices(self):
        # Retorna o número de arcos no digrafo.
        return self.m

    def vizinhanca(self, v):
        # Retorna um conjunto de todos os vértices adjacentes ao vértice v.
        return set(self.digrafo[v].keys()) if v in self.digrafo else set()

    def grau_vertice(self, v):
        # Retorna o grau do vértice v, que é o número de arcos que incidem sobre ele.
        return len(self.digrafo[v]) if v in self.digrafo else 0

    def peso_aresta(self, uv):
        # Retorna o peso do arco uv.
        u, v = uv
        return self.digrafo[u][v][0] if u in self.digrafo and v in self.digrafo[u] else None

    def menor_grau(self):
        # Retorna o menor grau entre todos os vértices do digrafo.
        return self.min_d

    def maior_grau(self):
        # Retorna o maior grau entre todos os vértices do digrafo.
        return self.max_d
    
    def bfs(self, v):
        """Realiza uma busca em largura (Breadth-First Search - BFS) a partir do vértice v.
        Retorna dois dicionários: 'distancia', que contém a distância de v a cada vértice,
        e 'predecessor', que contém o predecessor de cada vértice na árvore de busca."""
        visitado = {x: False for x in self.digrafo}
        distancia = {x: float('inf') for x in self.digrafo}
        predecessor = {x: None for x in self.digrafo}

        fila = deque([v])
        visitado[v] = True
        distancia[v] = 0

        while fila:
            u = fila.popleft()
            for vizinho in self.digrafo[u]:
                if not visitado[vizinho]:
                    fila.append(vizinho)
                    visitado[vizinho] = True
                    distancia[vizinho] = distancia[u] + 1
                    predecessor[vizinho] = u

        return distancia, predecessor

    def dfs_visita(self, v, visitado, predecessor, tempo_inicio, tempo_fim, tempo):
        """Função auxiliar para a busca em profundidade (Depth-First Search - DFS).
           Visita recursivamente todos os vértices do digrafo."""
        visitado[v] = True
        tempo += 1
        tempo_inicio[v] = tempo

        for vizinho in self.digrafo[v]:
            if not visitado[vizinho]:
                predecessor[vizinho] = v
                tempo = self.dfs_visitaa(vizinho, visitado, predecessor, tempo_inicio, tempo_fim, tempo)

        tempo += 1
        tempo_fim[v] = tempo

        return tempo

    def dfs(self, v):
        """Realiza uma busca em profundidade (Depth-First Search - DFS) a partir do vértice v.
        Retorna três dicionários: 'predecessor', que contém o predecessor de cada vértice na árvore de busca,
        e 'tempo_inicio' e 'tempo_fim', que contêm os tempos de início e fim da visita a cada vértice, respectivamente."""
        visitado = {x: False for x in self.digrafo}
        predecessor = {x: None for x in self.digrafo}
        tempo_inicio = {x: float('inf') for x in self.digrafo}
        tempo_fim = {x: float('inf') for x in self.digrafo}

        tempo = 0
        for vertice in self.digrafo:
            if not visitado[vertice]:
                tempo = self.dfs_visitaa(vertice, visitado, predecessor, tempo_inicio, tempo_fim, tempo)

        return predecessor, tempo_inicio, tempo_fim

    def bellman_ford(self, v):
        """Implementa o algoritmo de Bellman-Ford a partir do vértice v.
        Retorna dois dicionários: 'distancia', que contém a distância de v a cada vértice,
        e 'predecessor', que contém o predecessor de cada vértice no caminho mínimo."""
        distancia = {x: float('inf') for x in self.digrafo}
        predecessor = {x: None for x in self.digrafo}
        distancia[v] = 0

        for _ in range(len(self.digrafo) - 1):
            for u in self.digrafo:
                for vizinho, (peso, direcao) in self.digrafo[u].items():
                    if distancia[u] + peso < distancia[vizinho]:
                        distancia[vizinho] = distancia[u] + peso
                        predecessor[vizinho] = u

        return distancia, predecessor

    def djikstra(self, v):
        """Implementa o algoritmo de Djikstra a partir do vértice v.
        Retorna dois dicionários: 'distancia', que contém a distância de v a cada vértice,
        e 'predecessor', que contém o predecessor de cada vértice no caminho mínimo."""
        distancia = {x: float('inf') for x in self.digrafo}
        predecessor = {x: None for x in self.digrafo}
        distancia[v] = 0

        fila_prioridade = [(0, v)]
        while fila_prioridade:
            dist_u, u = heapq.heappop(fila_prioridade)
            if dist_u != distancia[u]:
                continue
            for vizinho, (peso, direcao) in self.digrafo[u].items():
                alternativa = distancia[u] + peso
                if alternativa < distancia[vizinho]:
                    distancia[vizinho] = alternativa
                    predecessor[vizinho] = u
                    heapq.heappush(fila_prioridade, (alternativa, vizinho))

        return distancia, predecessor