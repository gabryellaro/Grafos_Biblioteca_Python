from collections import deque, defaultdict
import heapq
import sys

class Grafo:
    def __init__(self):
        self.grafo = defaultdict(dict)

    def adicionar_arco(self, origem, destino, peso):
        self.grafo[origem][destino] = int(peso)

    def ler_arquivo(self, arquivo):
        try:
            with open(arquivo, 'r') as f:
                linhas = f.readlines()[7:]
                for linha in linhas:
                    partes = linha.split()
                    if partes[0] == 'a':
                        origem = partes[1]
                        destino = partes[2]
                        peso = partes[3]
                        self.adicionar_arco(origem, destino, peso)
            return True
        except Exception as e:
            print(f"Ocorreu um erro ao ler o arquivo: {e}")
            return False

    def obter_grafo(self):
        return dict(self.grafo)

    def n(self):
        return len(self.grafo)

    def m(self):
        return sum(len(v) for v in self.grafo.values())

    def viz(self, v):
        return list(self.grafo[v].keys()) if v in self.grafo else []

    def d(self, v):
        return len(self.grafo[v]) if v in self.grafo else 0

    def w(self, uv):
        u, v = uv
        return self.grafo[u][v] if u in self.grafo and v in self.grafo[u] else None

    def mind(self):
        return min(len(v) for v in self.grafo.values()) if self.grafo else None

    def maxd(self):
        return max(len(v) for v in self.grafo.values()) if self.grafo else None

    def bfs(self, v):
        visitado = {x: False for x in self.grafo}
        distancia = {x: float('inf') for x in self.grafo}
        predecessor = {x: None for x in self.grafo}

        distancia[v] = 0
        visitado[v] = True
        fila = deque([v])

        while fila:
            u = fila.popleft()
            for vizinho in self.grafo[u]:
                if not visitado[vizinho]:
                    fila.append(vizinho)
                    visitado[vizinho] = True
                    distancia[vizinho] = distancia[u] + 1
                    predecessor[vizinho] = u

        return distancia, predecessor

    def dfs(self, v):
        visitado = {x: False for x in self.grafo}
        predecessor = {x: None for x in self.grafo}
        tempo_inicio = {x: None for x in self.grafo}
        tempo_fim = {x: None for x in self.grafo}
        tempo = [0]

        def dfs_visit(u):
            tempo[0] += 1
            tempo_inicio[u] = tempo[0]
            visitado[u] = True

            for vizinho in self.grafo[u]:
                if not visitado[vizinho]:
                    predecessor[vizinho] = u
                    dfs_visit(vizinho)

            tempo[0] += 1
            tempo_fim[u] = tempo[0]

        dfs_visit(v)
        return predecessor, tempo_inicio, tempo_fim

    def bf(self, v):
        distancia = {x: float('inf') for x in self.grafo}
        predecessor = {x: None for x in self.grafo}
        distancia[v] = 0

        for _ in range(len(self.grafo) - 1):
            for u in self.grafo:
                for vizinho, peso in self.grafo[u].items():
                    if distancia[u] + peso < distancia[vizinho]:
                        distancia[vizinho] = distancia[u] + peso
                        predecessor[vizinho] = u

        for u in self.grafo:
            for vizinho, peso in self.grafo[u].items():
                if distancia[u] + peso < distancia[vizinho]:
                    print("Grafo contém um ciclo de peso negativo")
                    return None, None

        return distancia, predecessor

    def dijkstra(self, v):
        distancia = {x: float('inf') for x in self.grafo}
        predecessor = {x: None for x in self.grafo}
        distancia[v] = 0

        fila_prioridade = [(0, v)]
        while fila_prioridade:
            dist_u, u = heapq.heappop(fila_prioridade)
            if dist_u != distancia[u]:
                continue

            for vizinho, peso in self.grafo[u].items():
                dist_v = distancia[u] + peso
                if dist_v < distancia[vizinho]:
                    distancia[vizinho] = dist_v
                    predecessor[vizinho] = u
                    heapq.heappush(fila_prioridade, (dist_v, vizinho))

        return distancia, predecessor
