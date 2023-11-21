from grafo import *
g = Grafo()
if g.ler_arquivo("teste.gr"):
    print("Arquivo lido com sucesso!")
    print("Número de vértices:", g.n())
    print("Número de arestas:", g.m())
    print("Vizinhança do vértice v:", g.viz('2'))
    print("Grau do vértice v:", g.d('2'))
    print("Peso da aresta uv:", g.w(('27', '28')))
    print("Menor grau no grafo:", g.mind())
    print("Maior grafo no grafo:", g.maxd())
else:
    print("Falha ao ler o arquivo.")
def main():
    g = Grafo()
    if g.ler_arquivo('arquivo.gr'):
        print("Arquivo lido com sucesso!")
        print("Número de vértices:", g.n())
        print("Número de arestas:", g.m())
        print("Vizinhança do vértice v:", g.viz('v'))
        print("Grau do vértice v:", g.d('v'))
        print("Peso da aresta uv:", g.w(('u', 'v')))
        print("Menor grau no grafo:", g.mind())
        print("Maior grafo no grafo:", g.maxd())

        v = 'v'  # Substitua 'v' pelo vértice de origem desejado
        distancia, predecessor = g.bfs(v)
        print(f"Distâncias a partir de {v}:", distancia)
        print(f"Predecessores a partir de {v}:", predecessor)

        predecessor, tempo_inicio, tempo_fim = g.dfs(v)
        print(f"Tempos de início da visita a partir de {v}:", tempo_inicio)
        print(f"Tempos de término da visita a partir de {v}:", tempo_fim)

        distancia, predecessor = g.bf(v)
        print(f"Distâncias mínimas a partir de {v} (Bellman-Ford):", distancia)

        distancia, predecessor = g.dijkstra(v)
        print(f"Distâncias mínimas a partir de {v} (Dijkstra):", distancia)
    else:
        print("Falha ao ler o arquivo.")

if __name__ == "__main__":
    main()
