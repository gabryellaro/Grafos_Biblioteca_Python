from lib_grafo_digrafo import *

def main():
    nome_arquivo="teste.gr"
    g = Grafo()
    d = Digrafo()
    while True:
        print("============================================")
        print("1.Operações como Grafo")
        print("2.Operações como Digrafo")
        print("3.Resultado dos testes")
        print("============================================")
        opcao= input("Escolha uma opção: ")
        if opcao =='1':
            if g.ler_arquivo(nome_arquivo):
                menu_grafo(g)
            break
        elif opcao =='2':
            if d.ler_arquivo(nome_arquivo):
                menu_digrafo(d)
            break
        elif opcao=='3':
            if d.ler_arquivo(nome_arquivo):
                d.testes(nome_arquivo)
            break
        else:
            print("Opção Inválida!")

if __name__ == "__main__":
    main()
