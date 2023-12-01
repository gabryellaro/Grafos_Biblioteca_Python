from lib_grafo_digrafo import *

def main():
    # Define o nome do arquivo a ser lido
    nome_arquivo = "USA-road-d.NY.gr"
    # Cria uma instância de Grafo e outra de Digrafo
    g = Grafo()
    d = Digrafo()
    while True:
        print("============================================")
        print("1. Operações como Grafo")
        print("2. Operações como Digrafo")
        print("3. Resultado dos testes")
        print("============================================")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            # Se a leitura do arquivo for bem-sucedida, chama o menu_grafo
            if g.ler_arquivo(nome_arquivo):
                menu_grafo(g)
            break
        elif opcao == '2':
            # Se a leitura do arquivo for bem-sucedida, chama o menu_digrafo
            if d.ler_arquivo(nome_arquivo):
                menu_digrafo(d)
            break
        elif opcao == '3':
            # Se a leitura do arquivo for bem-sucedida, executa os testes
            if d.ler_arquivo(nome_arquivo):
                testes(d)
            break
        else:
            print("Opção Inválida!")

if __name__ == "__main__":
    main()
