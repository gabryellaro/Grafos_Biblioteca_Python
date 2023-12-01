from collections import deque, defaultdict
import heapq

class Grafo:
    def __init__(self):
        '''
        Inicializa um grafo representado por um dicionário padrão (defaultdict).
        A estrutura é grafo[origem][destino] = peso.
        '''
        self.grafo = defaultdict(dict)

    def adicionar_aresta(self, origem, destino, peso):
        '''
        Adiciona uma aresta ao grafo com a origem, destino e peso fornecidos.
        Os pesos são armazenados como inteiros.
        '''
        self.grafo[origem][destino] = int(peso)

    def ler_arquivo(self, nome_arquivo):
        '''
        Lê um arquivo no formato específico (ignorando as 6 primeiras linhas),
        extraindo informações de arestas e adicionando ao grafo.
        Retorna True se a operação foi bem-sucedida, False caso contrário.
        '''
        try:
            with open(nome_arquivo, 'r') as arquivo:
                for _ in range(6):
                    next(arquivo)
                for linha in arquivo:
                    dados = linha.split()
                    if len(dados) >= 4 and dados[0] == 'a':
                        self.adicionar_aresta(dados[1], dados[2], int(dados[3]))
            return True
        except Exception as e:
            print(f"Ocorreu um erro ao ler o arquivo: {e}")
            return False

    def obter_grafo(self):
        #Retorna uma cópia do grafo atual.
        return dict(self.grafo)

    def num_vertices(self):
        #Retorna o número de vértices no grafo.
        return len(self.grafo)

    def num_arestas(self):
        #Retorna o número total de arestas no grafo.
        return sum(len(v) for v in self.grafo.values())

    def vizinhanca(self, v):
        #Retorna uma lista dos vértices vizinhos ao vértice fornecido.
        return list(self.grafo[v].keys()) if v in self.grafo else []

    def grau_vertice(self, v):
        #Retorna o grau do vértice fornecido (número de arestas incidentes).
        return len(self.grafo[v]) if v in self.grafo else 0

    def peso_aresta(self, uv):
        #Retorna o peso da aresta entre os vértices u e v, se existir; caso contrário, retorna None.
        u, v = uv
        return self.grafo[u][v] if u in self.grafo and v in self.grafo[u] else None

    def menor_grau(self):
        #Retorna o menor grau de vértice no grafo.
        return min(len(v) for v in self.grafo.values()) if self.grafo else None

    def maior_grau(self):
        #Retorna o maior grau de vértice no grafo.
        return max(len(v) for v in self.grafo.values()) if self.grafo else None

    def bfs(self, v):
        '''
        Executa a busca em largura a partir do vértice fornecido no grafo.
        Retorna distâncias e predecessores em relação a v.
        '''
        if v not in self.grafo:
            print("Vértice não encontrado no grafo.")
            return None

        d = {vertice: float('inf') for vertice in self.grafo}
        pi = {vertice: None for vertice in self.grafo}
        d[v] = 0
        fila = deque([v])

        while fila:
            atual = fila.popleft()
            for vizinho in self.grafo[atual]:
                if d[vizinho] == float('inf'):
                    d[vizinho] = d[atual] + 1
                    pi[vizinho] = atual
                    fila.append(vizinho)

        return d, pi
    
    def dfs(self, vertice):
        '''
        Executa a busca em profundidade a partir do vértice fornecido no grafo.
        Retorna predecessores, tempos de início e fim da visita aos vértices.
        '''
        pi = {v: None for v in self.grafo}
        v_ini = {v: None for v in self.grafo}
        v_fim = {v: None for v in self.grafo}
        tempo = 0

        stack = [vertice]

        while stack:
            u = stack[-1]

            if v_ini[u] is None:
                tempo += 1
                v_ini[u] = tempo

            vizinho_encontrado = False
            for v in self.grafo[u]:
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
        '''
        Executa o algoritmo de Bellman-Ford a partir do vértice fornecido no grafo.
        Retorna distâncias e predecessores; lança uma exceção se houver ciclo negativo.
        '''
        d = {vertice: float('inf') for vertice in self.grafo}
        pi = {vertice: None for vertice in self.grafo}
        d[v] = 0

        for _ in range(len(self.grafo) - 1):
            for origem in self.grafo:
                for destino in self.grafo[origem]:
                    if d[origem] + self.grafo[origem][destino] < d[destino]:
                        d[destino] = d[origem] + self.grafo[origem][destino]
                        pi[destino] = origem

        for origem in self.grafo:
            for destino in self.grafo[origem]:
                if d[origem] + self.grafo[origem][destino] < d[destino]:
                    raise ValueError("O grafo contém um ciclo negativo")

        return d, pi

    def dijkstra(self, origem):
        '''
        Executa o algoritmo de Dijkstra a partir do vértice fornecido no grafo.
        Retorna distâncias e predecessores.
        '''
        distancias = {v: float('inf') for v in self.grafo}
        predecessores = {v: None for v in self.grafo}
        distancias[origem] = 0

        heap = [(0, origem)]

        while heap:
            dist_u, u = heapq.heappop(heap)

            if dist_u > distancias[u]:
                continue

            for v in self.grafo[u]:
                peso_uv = self.grafo[u][v]
                dist_v = distancias[u] + peso_uv

                if dist_v < distancias[v]:
                    distancias[v] = dist_v
                    predecessores[v] = u
                    heapq.heappush(heap, (dist_v, v))

        return distancias, predecessores