from collections import deque, defaultdict
import heapq

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

class DiGrafo:
    def __init__(self):
        # Inicializa o dicionário que irá armazenar o grafo
        self.grafo = {}
        # Inicializa o número de arestas como 0
        self.m = 0
        # Inicializa o menor grau como infinito
        self.min_d = float('inf')
        # Inicializa o maior grau como 0

    def adicionar_aresta(self, inicio, fim, peso, direcao=None):
        # Verifica se o vértice de início já existe no grafo
        if inicio not in self.grafo:
            # Se não existir, adiciona o vértice de início ao grafo
            self.grafo[inicio] = {}
        # Se a direção não for fornecida, determina a direção com base nos valores dos vértices
        if direcao is None:
            direcao = 'a' if inicio < fim else 'b'
        # Adiciona a aresta ao vértice de início no grafo
        # A aresta é representada como um dicionário, onde a chave é o vértice de fim e o valor é uma tupla contendo o peso e a direção
        self.grafo[inicio][fim] = (peso, direcao)
        # Incrementa o número de arestas
        self.m += 1
        # Atualiza o menor e o maior grau se necessário
        self.min_d = min(self.min_d, len(self.grafo[inicio]))
        self.max_d = max(self.max_d, len(self.grafo[inicio]))

    def ler_arquivo(self, nome_arquivo):
        # Abre o arquivo para leitura
        with open(nome_arquivo, 'r') as arquivo:
            # Ignora as seis primeiras linhas do arquivo
            for _ in range(6):
                next(arquivo)
            # Lê cada linha do arquivo a partir da sétima linha
            for linha in arquivo:
                # Divide a linha em uma lista de dados
                dados = linha.split()
                # Adiciona a aresta ao grafo
                self.adicionar_aresta(dados[1], dados[2], dados[3], dados[0])

    def aresta_positiva(self, inicio, fim):
        # Verifica se o vértice de início existe no grafo e se o vértice de fim é uma aresta do vértice de início
        # Se existir, retorna True se a direção da aresta é positiva e False caso contrário
        return inicio in self.grafo and fim in self.grafo[inicio] and self.grafo[inicio][fim][1] == 'a'

    def obter_grafo(self):
        # Retorna o grafo
        return self.grafo

    def n(self):
        # Retorna o número de vértices do grafo
        return len(self.grafo)

    def m(self):
        # Retorna o número de arestas do grafo
        return self.m

    def viz(self, v):
        # Retorna a vizinhança do vértice v
        return set(self.grafo[v].keys()) if v in self.grafo else set()

    def d(self, v):
        # Retorna o grau do vértice v
        return len(self.grafo[v]) if v in self.grafo else 0

    def w(self, uv):
        # Retorna o peso da aresta uv
        u, v = uv
        return self.grafo[u][v][0] if u in self.grafo and v in self.grafo[u] else None

    def mind(self):
        # Retorna o menor grau presente no grafo
        return self.min_d

    def maxd(self):
        # Retorna o maior grau presente no grafo
        return self.max_d #eu passei por aqui >:D 

    def menu(g):
        while True:
            print("1. Obter número de vértices e arestas")
            print("2. Obter vizinhança de um vértice")
            print("3. Obter grau de um vértice")
            print("4. Obter peso de uma aresta")
            print("5. Obter menor grau do grafo")
            print("6. Obter maior grau do grafo")
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                print(g.n())
                print(g.m())
            elif opcao == "2":
                v = input("Digite o vértice: ")
                print(g.viz(v))
            elif opcao == "3":
                v = input("Digite o vértice: ")
                print(g.d(v))
            elif opcao == "4":
                uv = input("Digite a aresta no formato 'u v': ").split()
                print(g.w(uv))
            elif opcao == "6":
                print(g.mind())
            elif opcao == "":
                print(g.maxd())
            elif opcao == "0":
                break
            else:
                print("Opção inválida. Tente novamente.")
