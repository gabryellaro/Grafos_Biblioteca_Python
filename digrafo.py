from collections import deque
import heapq

class Digrafo:
    def __init__(self):
        '''
        Inicializa um digrafo vazio, mantendo um dicionário para armazenar as arestas,
        m para contar o número total de arestas, min_d para armazenar o menor grau,
        e max_d para armazenar o maior grau.
        '''
        self.digrafo = {}
        self.m = 0
        self.min_d = float('inf')
        self.max_d = 0

    def adicionar_arco(self, origem, destino, peso):
        '''
        Adiciona um arco ao digrafo com a origem, destino e peso fornecidos.
        Mantém também a contagem de arestas, o menor grau e o maior grau.
        '''
        if origem not in self.digrafo:
            self.digrafo[origem] = {}
        
        direcao = 'positivo' if origem < destino else 'negativo'
        self.digrafo[origem][destino] = (int(peso), direcao)
        
        self.m += 1
        self.min_d = min(self.min_d, len(self.digrafo[origem]))
        self.max_d = max(self.max_d, len(self.digrafo[origem]))

    def ler_arquivo(self, nome_arquivo):
        '''
        Lê um arquivo no formato específico (ignorando as 6 primeiras linhas),
        extraindo informações de arestas e adicionando ao digrafo.
        Retorna True se a operação foi bem-sucedida, False caso contrário.
        '''
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

    def obter_digrafo(self):
        #Imprime e retorna o digrafo, mostrando informações sobre cada arco.
        return dict(self.digrafo)

    def num_arestas(self):
        #Retorna o número total de arestas no digrafo.
        return len(self.digrafo)

    def num_vertices(self):
        #Retorna o número total de vértices no digrafo.
        return self.m

    def vizinhanca(self, v):
        #Retorna um conjunto dos vértices vizinhos ao vértice fornecido.
        return set(self.digrafo[v].keys()) if v in self.digrafo else set()

    def grau_vertice(self, v):
        #Retorna o grau do vértice fornecido (número de arestas incidentes).
        return len(self.digrafo[v]) if v in self.digrafo else 0

    def peso_aresta(self, uv):
        #Retorna o peso da aresta entre os vértices u e v, se existir; caso contrário, retorna None.
        u, v = uv
        return self.digrafo[u][v][0] if u in self.digrafo and v in self.digrafo[u] else None

    def menor_grau(self):
        #Retorna o menor grau de vértice no digrafo.
        return self.min_d

    def maior_grau(self):
        #Retorna o maior grau de vértice no digrafo.
        return self.max_d
    
    def bfs(self, v):
        '''
        Executa a busca em largura a partir do vértice fornecido no digrafo.
        Retorna distâncias e predecessores em relação a v.
        '''
        if v not in self.digrafo:
            print(f"O vértice {v} não está presente no digrafo.")
            return None

        d = {vertice: float('inf') for vertice in self.digrafo}
        pi = {vertice: None for vertice in self.digrafo}

        d[v] = 0

        fila = deque([v])

        while fila:
            atual = fila.popleft()

            for vizinho in self.vizinhanca(atual):
                if d[vizinho] == float('inf'):
                    d[vizinho] = d[atual] + 1
                    pi[vizinho] = atual
                    fila.append(vizinho)

        return d, pi
    
    def dfs(self, vertice):
        '''
        Executa a busca em profundidade a partir do vértice fornecido no digrafo.
        Retorna predecessores, tempos de início e fim da visita aos vértices.
        '''
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
        '''
        Executa o algoritmo de Bellman-Ford a partir do vértice fornecido no digrafo.
        Retorna distâncias mínimas e predecessores em relação a v.
        Lança uma exceção se o digrafo contiver um ciclo negativo.
        '''
        if v not in self.digrafo:
            print(f"O vértice {v} não está presente no digrafo.")
            return None

        d = {vertice: float('inf') for vertice in self.digrafo}
        pi = {vertice: None for vertice in self.digrafo}

        d[v] = 0

        for _ in range(self.num_vertices() - 1):
            for origem in self.digrafo:
                for destino in self.digrafo[origem]:
                    peso, _ = self.digrafo[origem][destino]
                    if d[origem] + peso < d[destino]:
                        d[destino] = d[origem] + peso
                        pi[destino] = origem

        for origem in self.digrafo:
            for destino in self.digrafo[origem]:
                peso, _ = self.digrafo[origem][destino]
                if d[origem] + peso < d[destino]:
                    raise ValueError("O grafo contém um ciclo negativo.")

        return d, pi

    def dijkstra(self, v):
        '''
        Executa o algoritmo de Dijkstra a partir do vértice fornecido no digrafo.
        Retorna distâncias mínimas e predecessores em relação a v.
        '''
        if v not in self.digrafo:
            print(f"O vértice {v} não está presente no digrafo.")
            return None

        d = {vertice: float('inf') for vertice in self.digrafo}
        pi = {vertice: None for vertice in self.digrafo}

        d[v] = 0

        fila_prioridade = [(0, v)]

        while fila_prioridade:
            dist_atual, atual = heapq.heappop(fila_prioridade)

            if dist_atual > d[atual]:
                continue

            for vizinho in self.vizinhanca(atual):
                peso, _ = self.digrafo[atual][vizinho]

                if d[atual] + peso < d[vizinho]:
                    d[vizinho] = d[atual] + peso
                    pi[vizinho] = atual
                    heapq.heappush(fila_prioridade, (d[vizinho], vizinho))

        return d, pi