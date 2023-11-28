from lib_grafo_digrafo import *

def main():
    nome_arquivo="teste.gr"
    g = Grafo()
    d = Digrafo()
    while True:
        print("============================================")
        print("Voce deseja trabalhar com o arquivo como um:")
        print("1.Grafo")
        print("2.Digrafo")
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
        else:
            print("Opção Inválida!")

if __name__ == "__main__":
    main()
