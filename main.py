from grafo import DiGrafo

def menu_digrafo(g):
    while True:
        print("1. Obter número de vértices e arestas")
        print("2. Obter vizinhança de um vértice")
        print("3. Obter grau de um vértice")
        print("4. Obter peso de uma aresta")
        print("5. Obter menor grau do grafo")
        print("6. Obter maior grau do grafo")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            print(g.num_vertices())
            print(g.num_arestas())
        elif opcao == "2":
            v = input("Digite o vértice: ")
            print(g.vizinhanca(v))
        elif opcao == "3":
            v = input("Digite o vértice: ")
            print(g.grau_vertice(v))
        elif opcao == "4":
            uv = input("Digite a aresta no formato 'u v': ").split()
            print(g.peso_aresta(uv))
        elif opcao == "5":
            print(g.menor_grau())
        elif opcao == "6":
            print(g.maior_grau())
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

def main():
    g = DiGrafo()
    nome_arquivo='USA-road-d.NY.gr'
    g.ler_arquivo(nome_arquivo)
    g.obter_grafo()
    menu_digrafo(g)

if __name__ == "__main__":
    main()