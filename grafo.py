class Grafo:
    def __init__(self):
        self.grafo = {}

    def adicionar_arco(self, origem, destino, peso):
        if origem not in self.grafo:
            self.grafo[origem] = {}
        self.grafo[origem][destino] = int(peso)

    def ler_arquivo(self, arquivo):
        try:
            with open(arquivo, 'r') as f:
                linhas = f.readlines()[7:]  # Ignora as 7 primeiras linhas do cabeçalho
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
        return self.grafo

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
