from grafo import *
from digrafo import *     

def menu_grafo(g):
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
            g.adicionar_arco(origem, destino, peso)
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