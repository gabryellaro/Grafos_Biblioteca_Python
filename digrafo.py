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
        if v not in self.digrafo:
            print("Vértice não encontrado no digrafo.")
            return None

        d = {vertice: float('inf') for vertice in self.digrafo}
        pi = {vertice: None for vertice in self.digrafo}
        d[v] = 0
        fila = deque([v])

        while fila:
            atual = fila.popleft()
            for vizinho in self.digrafo[atual]:
                if d[vizinho] == float('inf'):
                    d[vizinho] = d[atual] + 1
                    pi[vizinho] = atual
                    fila.append(vizinho)

        return d, pi

    def dfs(self, vertice):
        pi = {v: None for v in self.digrafo}
        v_ini = {v: None for v in self.digrafo}
        v_fim = {v: None for v in self.digrafo}
        tempo = 0

        stack = [vertice]

        while stack:
            u = stack[-1]

            if v_ini[u] is None:
                tempo += 1
                v_ini[u] = tempo

            vizinho_encontrado = False
            for v in self.digrafo[u]:
                if v_ini[v] is None:
                    pi[v] = u
                    stack.append(v)
                    vizinho_encontrado = True
                    break

            if not vizinho_encontrado:
                stack.pop()
                tempo += 1
                v_fim[u] = tempo

        return pi, v_ini, v_fim

    def bellman_ford(self, v):
        d = {vertice: float('inf') for vertice in self.digrafo}
        pi = {vertice: None for vertice in self.digrafo}
        d[v] = 0

        for _ in range(len(self.digrafo) - 1):
            for origem in self.digrafo:
                for destino in self.digrafo[origem]:
                    if d[origem] + self.digrafo[origem][destino][0] < d[destino]:
                        d[destino] = d[origem] + self.digrafo[origem][destino][0]
                        pi[destino] = origem

        for origem in self.digrafo:
            for destino in self.digrafo[origem]:
                if d[origem] + self.digrafo[origem][destino][0] < d[destino]:
                    raise ValueError("O digrafo contém um ciclo negativo")

        return d, pi

    def dijkstra(self, origem):
        distancias = {v: float('inf') for v in self.digrafo}
        predecessores = {v: None for v in self.digrafo}
        distancias[origem] = 0

        heap = [(0, origem)]

        while heap:
            dist_u, u = heapq.heappop(heap)

            if dist_u > distancias[u]:
                continue

            for v in self.digrafo[u]:
                peso_uv, _ = self.digrafo[u][v]
                dist_v = distancias[u] + peso_uv

                if dist_v < distancias[v]:
                    distancias[v] = dist_v
                    predecessores[v] = u
                    heapq.heappush(heap, (dist_v, v))

        return distancias, predecessores