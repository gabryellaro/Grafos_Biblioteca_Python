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
        print("4.Vizinhanca de um v")
        print("5.Grau de um v")
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
        print("4.Vizinhanca de um v")
        print("5.Grau de um v")
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
            origem = input("Digite o v de origem: ")
            destino = input("Digite o v de destino: ")
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
    # Caso de Teste a) O valor de G.mind
    print("a) O valor de G.min_d:", d.menor_grau())

    # Caso de Teste b) O valor de G.maxd
    print("b) O valor de G.max_d:", d.maior_grau())

    # Caso de Teste c) Um caminho com uma qtde. de arestas maior ou igual a 10
    caminho_com_10_arestas = None

    for vertice_inicial in d.digrafo:
        distancias, predecessores = d.bfs(vertice_inicial)

        # Encontrar um caminho com pelo menos 10 arestas
        for v, predecessor in predecessores.items():
            if predecessor is not None and distancias[v] >= 10:
                caminho_com_10_arestas = [v]
                while predecessor is not None:
                    caminho_com_10_arestas.insert(0, predecessor)
                    predecessor = predecessores[predecessor]
                break

        if caminho_com_10_arestas:
            break

    if caminho_com_10_arestas:
        print("c) Caminho com pelo menos 10 arestas:", caminho_com_10_arestas)
    else:
        print("c) Nenhum caminho com pelo menos 10 arestas encontrado.")

    # Caso de Teste d) Um ciclo com uma qtde. de arestas maior ou igual a 5
    for v in d.digrafo:
        ciclo=d.ciclo_5(v)
        if ciclo is not None:
           print("d) Ciclo com pelo menos 5 arestas:",ciclo)
           break
        else:
            print("c) Nenhum  Ciclo com pelo menos 5 arestas encontrado.")

    # Caso de Teste e) O vértice mais distante do vértice 129 e o valor da distância
    distancias, _ = d.dijkstra("129")

    vertice_mais_distante = max(distancias, key=distancias.get)
    distancia_mais_distante = distancias[vertice_mais_distante]

    print("e) Vértice mais distante de 129 é", vertice_mais_distante,"e a distância entre eles é",distancia_mais_distante)
