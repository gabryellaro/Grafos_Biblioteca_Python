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
        """Executa a busca em largura a partir do vértice v."""
        if v not in self.digrafo:
            print(f"O vértice {v} não está presente no digrafo.")
            return None

        # Inicializa listas para armazenar distâncias e predecessores
        d = {vertice: float('inf') for vertice in self.digrafo}
        pi = {vertice: None for vertice in self.digrafo}

        # Marca o vértice de origem como visitado
        d[v] = 0

        # Fila para rastrear os vértices a serem visitados
        fila = deque([v])

        while fila:
            atual = fila.popleft()

            for vizinho in self.vizinhanca(atual):
                if d[vizinho] == float('inf'):
                    # Se o vizinho ainda não foi visitado
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
        """Executa o algoritmo de Bellman-Ford a partir do vértice v."""
        if v not in self.digrafo:
            print(f"O vértice {v} não está presente no digrafo.")
            return None

        # Inicializa listas para armazenar distâncias e predecessores
        d = {vertice: float('inf') for vertice in self.digrafo}
        pi = {vertice: None for vertice in self.digrafo}

        # Marca o vértice de origem como visitado
        d[v] = 0

        # Relaxa todas as arestas repetidamente |V| - 1 vezes
        for _ in range(self.num_vertices() - 1):
            for origem in self.digrafo:
                for destino in self.digrafo[origem]:
                    peso, _ = self.digrafo[origem][destino]
                    if d[origem] + peso < d[destino]:
                        d[destino] = d[origem] + peso
                        pi[destino] = origem

        # Verifica ciclos negativos
        for origem in self.digrafo:
            for destino in self.digrafo[origem]:
                peso, _ = self.digrafo[origem][destino]
                if d[origem] + peso < d[destino]:
                    print("O grafo contém um ciclo negativo.")
                    return None

        return d, pi

    def dijkstra(self, v):
        """Executa o algoritmo de Dijkstra a partir do vértice v."""
        if v not in self.digrafo:
            print(f"O vértice {v} não está presente no digrafo.")
            return None

        # Inicializa listas para armazenar distâncias e predecessores
        d = {vertice: float('inf') for vertice in self.digrafo}
        pi = {vertice: None for vertice in self.digrafo}

        # Marca o vértice de origem como visitado
        d[v] = 0

        # Fila de prioridade para processar vértices com menor distância primeiro
        fila_prioridade = [(0, v)]

        while fila_prioridade:
            dist_atual, atual = heapq.heappop(fila_prioridade)

            if dist_atual > d[atual]:
                # Ignora processamento se a distância atual já não é a menor
                continue

            for vizinho in self.vizinhanca(atual):
                peso, _ = self.digrafo[atual][vizinho]

                if d[atual] + peso < d[vizinho]:
                    # Relaxa a aresta se encontrar um caminho mais curto
                    d[vizinho] = d[atual] + peso
                    pi[vizinho] = atual
                    heapq.heappush(fila_prioridade, (d[vizinho], vizinho))

        return d, pi