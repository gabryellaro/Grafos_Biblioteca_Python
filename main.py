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
