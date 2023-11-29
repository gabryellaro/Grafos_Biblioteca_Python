from collections import deque
import heapq

class Digrafo:
    def __init__(self):
        """Inicializa um digrafo direcionado vazio,
        o número de arcos como 0 e os graus mínimo e máximo
        como infinito e 0, respectivamente."""
        self.digrafo = {}
        self.m = 0
        self.min_d = float('inf')
        self.max_d = 0

    def adicionar_arco(self, origem, destino, peso):
        """Adiciona um arco ao digrafo com um peso e uma direção
        (positiva se 'origem' < 'destino', negativa caso contrário).
        Atualiza o número de arcos e os graus mínimo e máximo."""
        if origem not in self.digrafo:
            self.digrafo[origem] = {}
        # Define a direção com base na ordem dos vértices
        direcao = 'positivo' if origem < destino else 'negativo'
        self.digrafo[origem][destino] = (int(peso), direcao)
        self.m += 1
        self.min_d = min(self.min_d, len(self.digrafo[origem]))
        self.max_d = max(self.max_d, len(self.digrafo[origem]))

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

    def aresta_positiva(self, origem, destino):
        # Verifica se o arco de 'origem' para 'destino' existe e é positivo.
        return origem in self.digrafo and destino in self.digrafo[origem] and self.digrafo[origem][destino][1] == 'a'

    def obter_digrafo(self):
        # Imprime todos os arcos do grafo com seus pesos e direções e retorna o digrafo.
        for origem in self.digrafo:
            for destino in self.digrafo[origem]:
                peso, direcao = self.digrafo[origem][destino]
                print(f"Aresta de {origem} para {destino} com peso {peso} e direção {direcao}")
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
        visitado = {x: False for x in self.digrafo}
        distancia = {x: float('inf') for x in self.digrafo}
        predecessor = {x: None for x in self.digrafo}

        fila = deque()
        fila.append(v)
        visitado[v] = True
        distancia[v] = 0

        while fila:
            vertice = fila.popleft()
            for vizinho in self.digrafo[vertice]:
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
        visitado = {x: False for x in self.digrafo}
        predecessor = {x: None for x in self.digrafo}
        tempo_inicio = {x: None for x in self.digrafo}
        tempo_fim = {x: None for x in self.digrafo}

        tempo = [0]  # Usamos uma lista para que o valor seja passado por referência

        def dfs_visit(vertice):
            visitado[vertice] = True
            tempo[0] += 1
            tempo_inicio[vertice] = tempo[0]

            for vizinho in self.digrafo[vertice]:
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
        distancia = {x: float('inf') for x in self.digrafo}
        predecessor = {x: None for x in self.digrafo}

        distancia[v] = 0

        for _ in range(len(self.digrafo) - 1):
            for vertice in self.digrafo:
                for vizinho, (peso, _) in self.digrafo[vertice].items():
                    if distancia[vertice] + peso < distancia[vizinho]:
                        distancia[vizinho] = distancia[vertice] + peso
                        predecessor[vizinho] = vertice

        for vertice in self.digrafo:
            for vizinho, (peso, _) in self.digrafo[vertice].items():
                if distancia[vertice] + peso < distancia[vizinho]:
                    print("O digrafo contém um ciclo de peso negativo")
                    return None, None

        # Filtrar os resultados infinito e None
        distancia = {k: v for k, v in distancia.items() if v != float('inf')}
        predecessor = {k: v for k, v in predecessor.items() if v is not None}

        return distancia, predecessor

    def dijkstra(self, v):
        distancia = {x: float('inf') for x in self.digrafo}
        predecessor = {x: None for x in self.digrafo}

        distancia[v] = 0
        fila_prioridade = [(0, v)]

        while fila_prioridade:
            dist, vertice = heapq.heappop(fila_prioridade)
            if dist != distancia[vertice]:
                continue
            for vizinho, (peso, _) in self.digrafo[vertice].items():
                distancia_alternativa = distancia[vertice] + peso
                if distancia_alternativa < distancia[vizinho]:
                    distancia[vizinho] = distancia_alternativa
                    predecessor[vizinho] = vertice
                    heapq.heappush(fila_prioridade, (distancia_alternativa, vizinho))

        # Filtrar os resultados infinito e None
        distancia = {k: v for k, v in distancia.items() if v != float('inf')}
        predecessor = {k: v for k, v in predecessor.items() if v is not None}

        return distancia, predecessor