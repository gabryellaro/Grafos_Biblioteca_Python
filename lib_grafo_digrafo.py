from grafo import * #importa a classe grafo
from digrafo import * #importa a classe digrafo

def menu_grafo(g):
    '''
    Implementa um menu interativo para operações em um grafo não direcionado.
    Permite ao usuário escolher entre diversas operações, como adicionar aresta, calcular graus,
    executar algoritmos de busca, entre outros.
    '''
    while True:
        print("==========================")
        print("1.Adicionar arco")
        print("2.N° de vertices")
        print("3.N° de arestas")
        print("4.Vizinhanca de um vertice")
        print("5.Grau de um vertice")
        print("6.Peso de uma aresta")
        print("7.Menor grau")
        print("8.Maior grau")
        print("9.BFS")
        print("10.DFS")
        print("11.Bellman Ford")
        print("12.Djikstra")
        print("13.Imprimir Grafo")
        print("0.SAIR")
        print("==========================")
        opcao = input("Escolha uma opção: ")
        if opcao=='0':
            break
        elif opcao=='1':
            origem = input("Digite o vértice de origem: ")
            destino = input("Digite o vértice de destino: ")
            peso = input("Digite o peso da aresta: ")
            g.adicionar_aresta(origem, destino, peso)
        elif opcao=='2':
            print(g.num_vertices())
        elif opcao=='3':
            print(g.num_arestas())
        elif opcao=='4':
            v = input("Digite o vértice: ")
            print(g.vizinhanca(v))
        elif opcao=='5':
            v = input("Digite o vértice: ")
            print(g.grau_vertice(v))
        elif opcao=='6':
            uv = input("Digite a aresta no formato 'u v': ")
            print(g.peso_aresta(tuple(uv.split())))
        elif opcao=='7':
            print(g.menor_grau())
        elif opcao=='8':
            print(g.maior_grau())
        elif opcao=='9':
            v = input("Digite o vértice de origem para BFS: ")
            print(g.bfs(v))
        elif opcao=='10':
            v = input("Digite o vértice de origem para DFS: ")
            print(g.dfs(v))
        elif opcao=='11':
            v = input("Digite o vértice de origem para Bellman Ford: ")
            print(g.bellman_ford(v))
        elif opcao=='12':
            v = input("Digite o vértice de origem para Djikstra: ")
            print(g.dijkstra(v))
        elif opcao=='13':
            print(g.obter_grafo())
        else:
            print("Opção Inválida!")

def menu_digrafo(d):
    '''
    Implementa um menu interativo para operações em um digrafo direcionado.
    Permite ao usuário escolher entre diversas operações, como adicionar arco, calcular graus,
    executar algoritmos de busca, entre outros.
    '''
    while True:
        print("==========================")
        print("1.Adicionar arco")
        print("2.N° de vertices")
        print("3.N° de arestas")
        print("4.Vizinhanca de um vertice")
        print("5.Grau de um vertice")
        print("6.Peso de uma aresta")
        print("7.Menor grau")
        print("8.Maior grau")
        print("9.BFS")
        print("10.DFS")
        print("11.Bellman Ford")
        print("12.Djikstra")
        print("13.Imprimir Digrafo")
        print("0.SAIR")
        print("==========================")
        opcao = input("Escolha uma opcao: ")
        if opcao=='0':
            break
        elif opcao=='1':
            origem = input("Digite o vertice de origem: ")
            destino = input("Digite o vertice de destino: ")
            peso = input("Digite o peso da aresta: ")
            d.adicionar_arco(origem, destino, peso)
        elif opcao=='2':
            print(d.num_vertices())
        elif opcao=='3':
            print(d.num_arestas())
        elif opcao=='4':
            v = input("Digite o vértice: ")
            print(d.vizinhanca(v))
        elif opcao=='5':
            v = input("Digite o vértice: ")
            print(d.grau_vertice(v))
        elif opcao=='6':
            uv = input("Digite a aresta no formato 'u v': ")
            print(d.peso_aresta(tuple(uv.split())))
        elif opcao=='7':
            print(d.menor_grau())
        elif opcao=='8':
            print(d.maior_grau())
        elif opcao=='9':
            v = input("Digite o vértice de origem para BFS: ")
            print(d.bfs(v))
        elif opcao=='10':
            v = input("Digite o vértice de origem para DFS: ")
            print(d.dfs(v))
        elif opcao=='11':
            v = input("Digite o vértice de origem para Bellman Ford: ")
            print(d.bellman_ford(v))
        elif opcao=='12':
            v = input("Digite o vértice de origem para Djikstra: ")
            print(d.dijkstra(v))
        elif opcao=='13':
            print(d.obter_digrafo())
        else:
            print("Opção Inválida!")

def testes(d):
    # a) Calcula e imprime o menor grau do digrafo
    mind = d.menor_grau()
    print(f'a) Valor de G.mind: {mind}')

    # b) Calcula e imprime o maior grau do digrafo
    maxd = d.maior_grau()
    print(f'b) Valor de G.maxd: {maxd}')

    # c) Encontra e imprime um caminho BFS a partir de um vértice com grau maior ou igual a 10
    caminho_10 = None
    for vertice in d.digrafo:
        if d.grau_vertice(vertice) >= 10:
            caminho_10 = d.bfs(vertice)
            break
    print(f'c) Caminho com uma quantidade de arestas maior ou igual a 10: {caminho_10}')

    # d) Encontra e imprime um ciclo DFS a partir de um vértice com grau maior ou igual a 5
    ciclo_5 = None
    for vertice in d.digrafo:
        if d.grau_vertice(vertice) >= 5:
            ciclo_5 = d.dfs(vertice)
            break
    print(f'd) Ciclo com uma quantidade de arestas maior ou igual a 5: {ciclo_5}')

    # e) Calcula e imprime o vértice mais distante do vértice 129 e a distância entre eles usando Dijkstra
    distancias_129, predecessores = d.dijkstra("129")

    # Filtra vértices alcançáveis (distância diferente de infinito)
    vertices_alcancaveis = [vertice for vertice, distancia in distancias_129.items() if distancia != float('inf')]
    predecessores_alcancaveis = {vertice: predecessores[vertice] for vertice in vertices_alcancaveis}

    # Encontra o vértice mais distante e calcula a quantidade de arestas no caminho
    vertice_mais_distante = max(predecessores_alcancaveis, key=lambda v: distancias_129[v])
    quantidade_arestas = 0
    atual = vertice_mais_distante
    while atual is not None:
        quantidade_arestas += 1
        atual = predecessores[atual]
    print(f"e) Vértice mais distante de 129: {vertice_mais_distante}, Distância: {quantidade_arestas}.")
